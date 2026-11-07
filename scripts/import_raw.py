#!/usr/bin/env python3
"""Merge research/raw/*.json into the curated data files.

    python3 scripts/import_raw.py            # write data/*.json
    python3 scripts/import_raw.py --dry-run  # only print the report

- Food & drink that meet the bar (Google >= 4.2 and >= 50 reviews) go to
  data/restaurants.json, data/bars.json or data/shops.json by category.
- Everything below the bar or without verified Google numbers goes to data/candidates.json.
- Attractions go to data/attractions.json.
- Duplicates (same id, or same name + street) are merged.
- Coordinates already present in data/*.json or data/geocode-cache.json are kept.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from schema import (  # noqa: E402
    AREAS, ATTRACTION_CATEGORIES, ATTRACTION_STATUS, ATTRACTION_TAGS, BAR_CATEGORIES, BOOKING,
    COUNTRIES, DATA, DATA_FILES, FACETS, FNB_CATEGORIES, FOOD_CATEGORIES, PAYMENT, RAW, REGIONS,
    RESERVATION, SHOP_CATEGORIES, STYLES, V1_CUISINE_GROUP, V1_TAGS, award_flags, infer_countries, infer_dishes, infer_style,
    in_cologne, is_area_wide, load_json, meets_criteria, norm_name, region_for, save_json, slugify, street_key,
)

TODAY = dt.date.today().isoformat()

CATEGORY_SYNONYMS = {
    "pub": "kneipe", "brewpub": "brauhaus", "brewery": "brauhaus",
    "ice-cream": "dessert", "icecream": "dessert", "coffee": "cafe", "coffee-shop": "cafe",
    "imbiss": "streetfood", "fast-food": "streetfood", "wine-store": "wine-shop",
    "cocktail": "cocktail-bar", "cocktailbar": "cocktail-bar", "winebar": "wine-bar",
    "finedining": "fine-dining", "fine-dining-restaurant": "fine-dining", "street-food": "streetfood",
}

warnings: list[str] = []


def warn(msg: str) -> None:
    warnings.append(msg)


def as_list(v) -> list:
    if v is None:
        return []
    if isinstance(v, list):
        return [x for x in v if x not in (None, "")]
    return [v]


def as_int(v):
    if v is None or v == "":
        return None
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return int(v)
    digits = re.sub(r"[^0-9]", "", str(v))
    return int(digits) if digits else None


def as_float(v):
    if v is None or v == "":
        return None
    try:
        return round(float(str(v).replace(",", ".")), 1)
    except ValueError:
        return None


def clean_tags(tags, allowed, where):
    out = []
    for t in as_list(tags):
        t = slugify(str(t))
        if t == "kolsch":
            t = "koelsch"
        if t in allowed:
            if t not in out:
                out.append(t)
        else:
            warn(f"{where}: unknown tag '{t}' dropped")
    return out


def beer_price(v, where: str):
    """EUR for a 0.2 l Kölsch / cheapest draft; plausible range only."""
    try:
        x = None if v in (None, "") else round(float(str(v).replace(",", ".").replace("€", "")), 2)
    except ValueError:
        x = None
    if x is not None and not 1.0 <= x <= 9.0:
        warn(f"{where}: beer_price_eur {x} out of range -> null")
        x = None
    return x


def clean_enum_list(values, allowed: dict, where: str, field: str) -> list[str]:
    out = []
    for v in as_list(values):
        v = slugify(str(v))
        if v in allowed:
            if v not in out:
                out.append(v)
        else:
            warn(f"{where}: unknown {field} '{v}' dropped")
    return out


def normalize_fnb(p: dict, agent: str) -> dict:
    name = (p.get("name") or "").strip()
    where = f"[{agent}] {name}"
    cat = slugify(p.get("category") or "restaurant")
    cat = CATEGORY_SYNONYMS.get(cat, cat)
    if cat not in FNB_CATEGORIES:
        warn(f"{where}: unknown category '{cat}' -> restaurant")
        cat = "restaurant"
    area = p.get("area")
    if area not in AREAS:
        warn(f"{where}: unknown area '{area}' -> other")
        area = "other"

    facets = {k: clean_enum_list(p.get(k), allowed, where, k) for k, allowed in FACETS.items()}
    reservation = p.get("reservation") if p.get("reservation") in RESERVATION else "unknown"
    payment = p.get("payment") if p.get("payment") in PAYMENT else "unknown"
    countries = []
    for c in as_list(p.get("cuisine_country")):
        c = str(c).strip().upper()
        if c in COUNTRIES:
            countries.append(c)
        else:
            warn(f"{where}: unknown cuisine_country '{c}' dropped")
    region = p.get("cuisine_region") if p.get("cuisine_region") in REGIONS else None
    awards = as_list(p.get("awards"))
    flags, location = award_flags(awards), []

    # v1 -> v2: tags and cuisine_group
    for t in as_list(p.get("tags")):
        t = slugify(str(t))
        t = "koelsch" if t == "kolsch" else t
        if t not in V1_TAGS:
            warn(f"{where}: unknown v1 tag '{t}' dropped")
            continue
        facet, val = V1_TAGS[t]
        if facet in facets and val not in facets[facet]:
            facets[facet].append(val)
        elif facet == "reservation" and reservation == "unknown":
            reservation = val
        elif facet == "payment":
            payment = val
        elif facet == "location":
            location.append(val)
        elif facet == "award" and val not in flags:
            flags.append(val)
    fallback_region = None
    cg = slugify(p["cuisine_group"]) if p.get("cuisine_group") else ""
    if cg in V1_CUISINE_GROUP:
        c_list, fallback_region, dish_list, diet_list = V1_CUISINE_GROUP[cg]
        if not countries:
            countries = list(c_list)
        facets["dishes"] += [d for d in dish_list if d not in facets["dishes"]]
        facets["diet"] += [d for d in diet_list if d not in facets["diet"]]
    elif cg:
        warn(f"{where}: unknown v1 cuisine_group '{cg}'")
    cuisine = (p.get("cuisine") or "").strip() or None
    if cat in FOOD_CATEGORIES and not countries and cat not in ("cafe", "bakery", "dessert"):
        countries = infer_countries(cuisine or "")
    if not facets["dishes"]:
        facets["dishes"] = infer_dishes(cuisine, name, " ".join(map(str, as_list(p.get("must_try")))))
    region = region or region_for(countries, fallback_region)
    if cat == "restaurant" and "michelin-star" in flags:
        cat = "fine-dining"
    if cat == "fine-dining" and "tasting-menu" not in facets["dishes"]:
        facets["dishes"].append("tasting-menu")

    pl = as_int(p.get("price_level"))
    if pl is not None and not 1 <= pl <= 4:
        warn(f"{where}: price_level {pl} out of range -> null")
        pl = None
    price_estimated = False
    if pl is None:  # category-based estimate where German prices are predictable; regular restaurants stay null
        est = {"streetfood": 1, "bakery": 1, "dessert": 1, "brauhaus": 2, "fine-dining": 4}.get(cat)
        if cat == "cafe":
            est = 2 if "brunch-plates" in facets["dishes"] or "brunch" in facets["meals"] else 1
        if est:
            pl, price_estimated = est, True
    ppp = p.get("price_pp") if isinstance(p.get("price_pp"), dict) else None
    if ppp:
        ppp = {k: as_int(ppp.get(k)) for k in ("min", "max") if as_int(ppp.get(k)) is not None} or None
    out = {
        "id": slugify(p.get("id") or name),
        "name": name,
        "category": cat,
        "area": area,
        "address": (p.get("address") or "").strip() or None,
        "lat": None,
        "lng": None,
        "cuisine": cuisine,
        "cuisine_country": countries,
        "cuisine_region": region,
        **facets,
        "reservation": reservation,
        "payment": payment,
        "location": location,
        "price_level": pl,
        "price_estimated": price_estimated,
        "price_pp": ppp,
        "price_note": p.get("price_note"),
        "beer_price_eur": beer_price(p.get("beer_price_eur"), where),
        "beer_price_note": p.get("beer_price_note"),
        "beers": as_list(p.get("beers")),
        "google_rating": as_float(p.get("google_rating")),
        "google_reviews": as_int(p.get("google_reviews")),
        "google_as_of": p.get("google_as_of"),
        "rating_source": p.get("rating_source"),
        "summary_ko": p.get("summary_ko"),
        "must_try": as_list(p.get("must_try")),
        "tips_ko": p.get("tips_ko"),
        "website": p.get("website"),
        "awards": awards,
        "award_flags": flags,
        "sources": as_list(p.get("sources")),
        "confidence": p.get("confidence") if p.get("confidence") in ("high", "medium", "low") else "medium",
        "research": agent,
        "checked": TODAY,
    }
    if not out["address"]:
        warn(f"{where}: missing address")
    return out


def normalize_attraction(p: dict, agent: str) -> dict:
    name = (p.get("name") or "").strip()
    where = f"[{agent}] {name}"
    cat = slugify(p.get("category") or "landmark")
    if cat not in ATTRACTION_CATEGORIES:
        warn(f"{where}: unknown attraction category '{cat}' -> landmark")
        cat = "landmark"
    area = p.get("area")
    if area not in AREAS:
        warn(f"{where}: unknown area '{area}' -> other")
        area = "other"
    status = p.get("status") if p.get("status") in ATTRACTION_STATUS else "open"
    booking = p.get("booking") if p.get("booking") in BOOKING else "not-needed"
    price = p.get("price_eur")
    try:
        price = None if price is None else round(float(price), 2)
    except (TypeError, ValueError):
        price = None
    prio = as_int(p.get("priority")) or 2
    return {
        "id": slugify(p.get("id") or name),
        "name": name,
        "name_ko": p.get("name_ko"),
        "category": cat,
        "area": area,
        "address": (p.get("address") or "").strip() or None,
        "lat": None,
        "lng": None,
        "summary_ko": p.get("summary_ko"),
        "tips_ko": p.get("tips_ko"),
        "price_eur": price,
        "price_note": p.get("price_note"),
        "duration_min": as_int(p.get("duration_min")),
        "hours_note": p.get("hours_note"),
        "booking": booking,
        "status": status,
        "season": p.get("season") if isinstance(p.get("season"), dict) else None,
        "priority": min(3, max(1, prio)),
        "tags": clean_tags(p.get("tags"), ATTRACTION_TAGS, where),
        "google_rating": as_float(p.get("google_rating")),
        "google_reviews": as_int(p.get("google_reviews")),
        "google_as_of": p.get("google_as_of"),
        "rating_source": p.get("rating_source"),
        "travel_time_min": as_int(p.get("travel_time_min")),
        "website": p.get("website"),
        "sources": as_list(p.get("sources")),
        "verification": p.get("verification") if p.get("verification") in ("sourced", "public-space", "annual-event")
        else ("sourced" if p.get("sources") else "unverified"),
        **ticket_fields(p),
        "research": agent,
        "checked": TODAY,
    }


DAYS = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
_RANGE = re.compile(r"^\d{1,2}:\d{2}-\d{1,2}:\d{2}(,\d{1,2}:\d{2}-\d{1,2}:\d{2})*$")


def clean_hours(h) -> dict | None:
    if not isinstance(h, dict):
        return None
    out = {}
    for d in DAYS:
        v = h.get(d)
        if isinstance(v, str):
            v = v.strip().replace("–", "-").replace(" ", "")
            v = "closed" if v.lower() in ("closed", "geschlossen", "휴관", "-") else v
            if v != "closed" and not _RANGE.match(v):
                warn(f"hours: unparsed value '{v}' for {d} -> null")
                v = None
        else:
            v = None
        out[d] = v
    return out if any(out.values()) else None


def clean_tickets(t) -> list:
    out = []
    for x in t if isinstance(t, list) else []:
        if isinstance(x, dict) and x.get("label_ko"):
            eur = x.get("eur")
            try:
                eur = None if eur is None else round(float(eur), 2)
            except (TypeError, ValueError):
                eur = None
            out.append({"label_ko": x["label_ko"], "eur": eur, "note_ko": x.get("note_ko")})
    return out


_ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def clean_date_hours(d) -> dict | None:
    """Date exceptions, e.g. {"2026-12-24": "closed", "2026-12-31": "10:00-14:00", "2026-12-27": "open"}.
    "open" = open that day but the times are not confirmed."""
    if not isinstance(d, dict):
        return None
    out = {}
    for k, v in sorted(d.items()):
        if not (isinstance(k, str) and _ISO.match(k) and isinstance(v, str)):
            warn(f"date_hours: dropped {k!r}: {v!r}")
            continue
        v = v.strip().replace("–", "-").replace(" ", "")
        v = "closed" if v.lower() in ("closed", "geschlossen", "휴관") else "open" if v.lower() == "open" else v
        if v not in ("closed", "open") and not _RANGE.match(v):
            warn(f"date_hours: unparsed value '{v}' for {k}")
            continue
        out[k] = v
    return out or None


def clean_closure(c) -> dict | None:
    """Part of a place closed for a while: {"what_ko", "start", "end", "note_ko"}."""
    if not (isinstance(c, dict) and c.get("what_ko") and _ISO.match(str(c.get("end") or ""))):
        return None
    return {"what_ko": c["what_ko"], "start": c.get("start") if _ISO.match(str(c.get("start") or "")) else None,
            "end": c["end"], "note_ko": c.get("note_ko")}


def ticket_fields(p: dict) -> dict:
    return {"tickets": clean_tickets(p.get("tickets")), "hours": clean_hours(p.get("hours")),
            "date_hours": clean_date_hours(p.get("date_hours")), "partial_closure": clean_closure(p.get("partial_closure")),
            "schedule": p.get("schedule") if p.get("schedule") in ("departures",) else None,
            "last_entry": p.get("last_entry"), "free_note": p.get("free_note"), "booking_url": p.get("booking_url"),
            "info_checked": p.get("checked") or p.get("info_checked"),
            "info_confidence": (p.get("confidence") or p.get("info_confidence")) if (p.get("checked") or p.get("info_checked")) else None}


def apply_attraction_updates(items: list[dict], updates: dict) -> None:
    """Round-5 ticket/hours research: fields present in an update replace the stored ones."""
    for it in items:
        u = updates.get(it["id"])
        if not u:
            continue
        tf = ticket_fields(u)
        for k, v in tf.items():
            if v not in (None, [], ""):
                it[k] = {**(it.get(k) or {}), **v} if k == "date_hours" else v
        for k in ("price_note", "hours_note", "status", "season", "booking"):
            if u.get(k) not in (None, ""):
                if k == "status" and u[k] not in ATTRACTION_STATUS:
                    continue
                if k == "booking" and u[k] not in BOOKING:
                    continue
                it[k] = u[k]
        if u.get("price_eur") is not None:
            try:
                it["price_eur"] = round(float(u["price_eur"]), 2)
            except (TypeError, ValueError):
                pass
        if u.get("website") and not it.get("website"):
            it["website"] = u["website"]
        if u.get("rename"):  # official name changed (e.g. a market renamed); the id stays
            it["name"] = u.get("name") or it["name"]
            it["name_ko"] = u.get("name_ko") or it.get("name_ko")
        for url in as_list(u.get("sources")):
            if url not in it["sources"]:
                it["sources"].append(url)
        if u.get("confidence"):
            it["info_confidence"] = u["confidence"]
            if it.get("verification") in ("annual-event", "unverified") and u.get("confidence") in ("high", "medium"):
                it["verification"] = "sourced"  # this year's dates are now confirmed


def apply_price_updates(items: list[dict], updates: dict) -> None:
    """Round-6 price research for places that had no price: level, per-person range, Kölsch price, style, dishes."""
    for it in items:
        u = updates.get(it["id"])
        if not u:
            continue
        where = f"[{u.get('_file')}] {it['name']}"
        conf = u.get("confidence")
        pl = as_int(u.get("price_level"))
        if pl is not None and 1 <= pl <= 4:
            it["price_level"] = pl
            it["price_estimated"] = conf == "low"  # weak evidence stays marked as an estimate
        elif pl is not None:
            warn(f"{where}: price_level {pl} out of range")
        pp = u.get("price_pp") if isinstance(u.get("price_pp"), dict) else None
        if pp:
            pp = {k: as_int(pp.get(k)) for k in ("min", "max") if as_int(pp.get(k)) is not None} or None
            if pp:
                it["price_pp"] = pp
        if u.get("price_note_ko") and pl is not None:
            it["price_note"] = u["price_note_ko"]
        bp = beer_price(u.get("beer_price_eur"), where)
        if bp:
            it["beer_price_eur"] = bp
            it["beer_price_note"] = u.get("beer_price_note_ko") or it.get("beer_price_note")
        if u.get("style_hint") in STYLES:
            it["style_hint"] = u["style_hint"]
        sig = [x.strip() for x in as_list(u.get("signature_ko")) if isinstance(x, str) and x.strip()]
        if sig and not it.get("must_try"):
            it["must_try"] = sig[:3]
        for url in as_list(u.get("sources")):
            if url not in it["sources"]:
                it["sources"].append(url)
        it["price_checked"] = u.get("checked")


def is_attraction(p: dict) -> bool:
    cat = slugify(p.get("category") or "")
    return cat in ATTRACTION_CATEGORIES or ("name_ko" in p and cat not in FNB_CATEGORIES)


def merge_into(primary: dict, other: dict) -> dict:
    def empty(x) -> bool:
        return x in (None, "", [], "unknown") or (isinstance(x, str) and len(x) < 20 and ("미확인" in x or "unknown" in x.lower()))

    for k, v in other.items():
        if empty(primary.get(k)) and not empty(v):
            primary[k] = v
    for k in ("awards", "award_flags", "sources", "must_try", "cuisine_country", "location", "beers", *FACETS):
        seen = list(primary.get(k) or [])
        for v in other.get(k) or []:
            if v not in seen:
                seen.append(v)
        primary[k] = seen
    primary["research"] = ", ".join(sorted(set(f"{primary['research']}, {other['research']}".split(", "))))
    return primary


def dedupe(items: list[dict], kind: str) -> list[dict]:
    by_key: dict[str, dict] = {}
    alias: dict[str, str] = {}
    for it in items:
        k_id = it["id"]
        k_ns = f"{norm_name(it['name'])}|{street_key(it.get('address'))}"
        existing_key = alias.get(k_id) or alias.get(k_ns)
        if existing_key:
            cur = by_key[existing_key]
            a, b = (cur, it) if (cur.get("google_reviews") or 0) >= (it.get("google_reviews") or 0) else (it, cur)
            warn(f"duplicate {kind}: '{it['name']}' ({it['research']}) merged with '{cur['name']}' ({cur['research']})")
            by_key[existing_key] = merge_into(dict(a), b)
        else:
            by_key[k_id] = it
            existing_key = k_id
        alias[k_id] = existing_key
        alias[k_ns] = existing_key
    # make ids unique (different places that share a slug)
    out, used = [], Counter()
    for it in by_key.values():
        used[it["id"]] += 1
        if used[it["id"]] > 1:
            it["id"] = f"{it['id']}-{it['area']}"
        out.append(it)
    return out


def price_level_from_pp(pp: dict | None):
    mx = (pp or {}).get("max") or (pp or {}).get("min")
    if not mx:
        return None
    return 1 if mx <= 15 else 2 if mx <= 30 else 3 if mx <= 60 else 4


def apply_verifications(items: list[dict], verifications: dict, candidates: list) -> list[dict]:
    """Overlay round-4 accuracy checks: closures leave the list, fresher Google numbers win."""
    kept = []
    for it in items:
        v = verifications.get(it["id"])
        if not v:
            kept.append(it)
            continue
        status = v.get("status") or "unknown"
        it["verified_at"] = TODAY
        it["verification_status"] = status
        it["verification_note"] = v.get("notes_ko")
        it["latest_review"] = v.get("latest_review")
        for u in as_list(v.get("sources")):
            if u not in it["sources"]:
                it["sources"].append(u)
        if status in ("closed-permanently", "closed-temporarily"):
            candidates.append({"name": it["name"], "area": it["area"], "address": it["address"],
                               "category": it["category"], "reason": f"{status} (확인 {TODAY})",
                               "found": v.get("notes_ko") or "", "sources": as_list(v.get("sources")),
                               "research": v["_file"]})
            warn(f"verification: {it['name']} -> {status}, moved to candidates")
            continue
        if v.get("address") and v["address"] != it.get("address"):
            warn(f"verification: {it['name']} address {it.get('address')} -> {v['address']}")
            it["address"], it["lat"], it["lng"] = v["address"], None, None
        r, n = as_float(v.get("google_rating")), as_int(v.get("google_reviews"))
        if r is not None and n is not None:
            if n >= (it.get("google_reviews") or 0) or v.get("google_as_of"):
                if (r, n) != (it.get("google_rating"), it.get("google_reviews")):
                    it["google_previous"] = f"{it.get('google_rating')} ({it.get('google_reviews')})"
                it["google_rating"], it["google_reviews"] = r, n
                it["google_as_of"] = v.get("google_as_of") or it.get("google_as_of")
                it["rating_source"] = v.get("rating_source") or it.get("rating_source")
        pp = v.get("price_pp") if isinstance(v.get("price_pp"), dict) else None
        if pp and it["category"] in FOOD_CATEGORIES:
            lvl = price_level_from_pp(pp)
            if lvl:
                it["price_pp"], it["price_level"], it["price_estimated"] = pp, lvl, False
                it["price_note"] = v.get("price_note") or it.get("price_note")
        if not meets_criteria(it):
            candidates.append({"name": it["name"], "area": it["area"], "address": it["address"],
                               "category": it["category"], "reason": f"below-criteria after check {TODAY}",
                               "found": f"Google {it['google_rating']} ({it['google_reviews']}) via {it.get('rating_source')}",
                               "sources": it["sources"], "research": v["_file"]})
            warn(f"verification: {it['name']} now below criteria ({it['google_rating']}, {it['google_reviews']})")
            continue
        kept.append(it)
    return kept


def area_rank(area: str) -> int:
    return AREAS.index(area) if area in AREAS else len(AREAS)


def keep_coords(items: list[dict], kind: str, cache: dict) -> None:
    old = {i["id"]: i for i in (load_json(DATA_FILES[kind], {"items": []}).get("items", []))}
    for it in items:
        if is_area_wide(it.get("address")):
            continue
        prev = old.get(it["id"])
        if prev and prev.get("lat") is not None:
            it["lat"], it["lng"] = prev["lat"], prev["lng"]
            for k in ("coord_source", "google_place_id", "google_maps_url"):
                if prev.get(k):
                    it[k] = prev[k]
        elif it.get("address") and it["address"] in cache:
            c = cache[it["address"]]
            if c.get("lat") is not None:
                it["lat"], it["lng"], it["coord_source"] = c["lat"], c["lng"], c.get("provider")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    files = sorted(p for p in RAW.glob("*.json") if not p.name.endswith("-data.json") and not p.name.startswith("r4-verify"))
    verify_files = sorted(RAW.glob("r4-verify*.json"))
    if not files:
        print("no research/raw/*.json files found")
        return 1

    buckets: dict[str, list[dict]] = defaultdict(list)
    candidates: list[dict] = []
    dropped_outside: list[str] = []
    for f in files:
        doc = load_json(f, {})
        agent = doc.get("agent") or f.stem
        for p in doc.get("places", []):
            if not p.get("name"):
                warn(f"[{agent}] entry without name skipped")
                continue
            if not in_cologne(p.get("address"), p.get("area")):
                dropped_outside.append(f"{p['name']} ({p.get('address')})")
                continue
            if is_attraction(p):
                buckets["attractions"].append(normalize_attraction(p, agent))
                continue
            it = normalize_fnb(p, agent)
            low_conf = it["confidence"] == "low"
            if not meets_criteria(it) or low_conf:
                reason = ("google-numbers-low-confidence" if low_conf and meets_criteria(it)
                          else "below-criteria" if it["google_rating"] is not None else "google-numbers-missing")
                candidates.append({
                    "name": it["name"], "area": it["area"], "address": it["address"],
                    "category": it["category"], "reason": reason,
                    "found": f"Google {it['google_rating']} ({it['google_reviews']}) via {it['rating_source']}",
                    "sources": it["sources"], "research": agent,
                })
                continue
            kind = ("restaurants" if it["category"] in FOOD_CATEGORIES
                    else "bars" if it["category"] in BAR_CATEGORIES else "shops")
            buckets[kind].append(it)
        for c in doc.get("candidates", []):
            if not in_cologne(c.get("address"), c.get("area")):
                dropped_outside.append(f"{c.get('name')} ({c.get('address')})")
                continue
            c = dict(c)
            c["research"] = agent
            candidates.append(c)

    cache = load_json(DATA / "geocode-cache.json", {}) or {}
    report = []
    attraction_updates = {}
    for f in files:
        for u in (load_json(f, {}) or {}).get("updates", []):
            if not u.get("id"):
                continue
            prev = attraction_updates.get(u["id"])
            if prev:  # several files may touch one attraction: later keys win, date exceptions and sources add up
                merged = {**prev, **{k: v for k, v in u.items() if v not in (None, "", [])}}
                merged["date_hours"] = {**(prev.get("date_hours") or {}), **(u.get("date_hours") or {})}
                merged["sources"] = as_list(prev.get("sources")) + [x for x in as_list(u.get("sources")) if x not in as_list(prev.get("sources"))]
                if u.get("confidence") is None:
                    merged["confidence"] = prev.get("confidence")
                u = merged
            attraction_updates[u["id"]] = u
    price_updates = {}
    for f in files:
        for u in (load_json(f, {}) or {}).get("price_updates", []):
            if u.get("id"):
                price_updates[u["id"]] = {**u, "_file": f.stem}
    verifications = {}
    for vf in verify_files:
        for v in (load_json(vf, {}) or {}).get("verifications", []):
            if v.get("id"):
                verifications[v["id"]] = {**v, "_file": vf.stem}
    for kind in DATA_FILES:
        items = dedupe(buckets.get(kind, []), kind)
        keep_coords(items, kind, cache)
        if kind != "attractions" and verifications:
            items = apply_verifications(items, verifications, candidates)
        if kind != "attractions" and price_updates:
            apply_price_updates(items, price_updates)
        if kind != "attractions":
            for it in items:  # format of the place (bistro, wine bar, tapas ...), see schema.STYLES
                it["style"] = it.pop("style_hint", None) or infer_style(it)
        if kind == "attractions" and attraction_updates:
            apply_attraction_updates(items, attraction_updates)
        if kind == "attractions":
            items.sort(key=lambda i: (area_rank(i["area"]), i["priority"], i["name"]))
        else:
            items.sort(key=lambda i: (area_rank(i["area"]), -(i.get("google_rating") or 0), -(i.get("google_reviews") or 0)))
        buckets[kind] = items
        report.append(f"{kind:12s} {len(items):4d}")

    # candidates: drop the ones that ended up in the main lists, dedupe by name.
    # Later research files win (r2-* after round 1), and "Seiberts" matches "Seiberts Classic Bar".
    GENERIC = {"cafe", "restaurant", "bar", "the", "brauhaus", "koeln", "cologne", "pizzeria", "ristorante",
               "imbiss", "kebap", "kebab", "grill", "haus", "und", "am", "im", "in", "der", "die", "das", "de", "la"}

    def sig(name: str) -> set:
        return {t for t in slugify(name).split("-") if len(t) >= 4 and t not in GENERIC}

    def same(a: tuple, b: tuple) -> bool:
        (ka, ta, aa), (kb, tb, ab) = a, b
        if ka == kb or (min(len(ka), len(kb)) >= 6 and (ka.startswith(kb) or kb.startswith(ka))):
            return True
        return bool(aa and aa == ab and ta and tb and (ta <= tb or tb <= ta))

    def ident(x: dict) -> tuple:
        return norm_name(x.get("name", "")), sig(x.get("name", "")), x.get("area")

    main_ids = [ident(i) for k in DATA_FILES for i in buckets[k]]
    seen, cands = [], []
    for c in reversed(candidates):
        me = ident(c)
        if not me[0] or any(same(me, m) for m in main_ids) or any(same(me, x) for x in seen):
            continue
        seen.append(me)
        cands.append(c)
    cands.reverse()
    report.append(f"{'candidates':12s} {len(cands):4d}")

    meta = {"generated": TODAY, "criteria": {"min_google_rating": 4.2, "min_google_reviews": 50},
            "research_files": [f.name for f in files]}
    if not args.dry_run:
        for kind in DATA_FILES:
            save_json(DATA_FILES[kind], {"meta": {**meta, "count": len(buckets[kind])}, "items": buckets[kind]})
        save_json(DATA / "candidates.json", {"meta": {**meta, "count": len(cands)}, "items": cands})
        wine = RAW / "wine-guide-data.json"
        if wine.exists():
            save_json(DATA / "wine.json", load_json(wine))

    print("\n".join(report))
    if dropped_outside:
        print(f"left out (outside Cologne): {len(dropped_outside)} — " + "; ".join(dropped_outside))
    by_area = Counter(i["area"] for k in ("restaurants", "bars", "shops") for i in buckets[k])
    print("F&B by area:", dict(sorted(by_area.items(), key=lambda kv: area_rank(kv[0]))))
    if warnings:
        print(f"\n{len(warnings)} warnings:")
        for w in warnings:
            print("  -", w)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
