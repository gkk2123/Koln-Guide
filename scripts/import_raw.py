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
    CUISINE_GROUPS, DATA, DATA_FILES, FNB_CATEGORIES, FOOD_CATEGORIES, PLACE_TAGS, RAW,
    SHOP_CATEGORIES, load_json, meets_criteria, norm_name, save_json, slugify, street_key,
)

TODAY = dt.date.today().isoformat()

CATEGORY_SYNONYMS = {
    "pub": "bar", "kneipe": "bar", "brewpub": "brauhaus", "brewery": "brauhaus",
    "ice-cream": "dessert", "icecream": "dessert", "coffee": "cafe", "coffee-shop": "cafe",
    "imbiss": "streetfood", "fast-food": "streetfood", "wine-store": "wine-shop",
    "cocktail": "cocktail-bar", "cocktailbar": "cocktail-bar", "winebar": "wine-bar",
}
CUISINE_SYNONYMS = {
    "burger": "american-burger", "american": "american-burger", "levantine": "middle-eastern",
    "lebanese": "middle-eastern", "syrian": "middle-eastern", "israeli": "middle-eastern",
    "vegan": "vegan-vegetarian", "vegetarian": "vegan-vegetarian", "cafe": "cafe-bakery",
    "bakery": "cafe-bakery", "dessert": "dessert-icecream", "ice-cream": "dessert-icecream",
    "thai": "thai-southeast-asian", "indian": "indian-south-asian", "spanish": "spanish-portuguese",
    "portuguese": "spanish-portuguese", "mexican": "latin-american", "peruvian": "latin-american",
    "steak": "steak-grill", "grill": "steak-grill", "fusion": "asian-fusion",
    "drinks": "bar-drinks", "bar": "bar-drinks", "rhineland": "german", "koelsch": "german",
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
    cg = slugify(p.get("cuisine_group") or "")
    cg = CUISINE_SYNONYMS.get(cg, cg)
    if cg not in CUISINE_GROUPS:
        fallback = "bar-drinks" if cat in BAR_CATEGORIES + SHOP_CATEGORIES else "international"
        warn(f"{where}: unknown cuisine_group '{cg}' -> {fallback}")
        cg = fallback
    pl = as_int(p.get("price_level"))
    if pl is not None and not 1 <= pl <= 4:
        warn(f"{where}: price_level {pl} out of range -> null")
        pl = None
    out = {
        "id": slugify(p.get("id") or name),
        "name": name,
        "category": cat,
        "area": area,
        "address": (p.get("address") or "").strip() or None,
        "lat": None,
        "lng": None,
        "cuisine": (p.get("cuisine") or "").strip() or None,
        "cuisine_group": cg,
        "price_level": pl,
        "price_note": p.get("price_note"),
        "google_rating": as_float(p.get("google_rating")),
        "google_reviews": as_int(p.get("google_reviews")),
        "google_as_of": p.get("google_as_of"),
        "rating_source": p.get("rating_source"),
        "summary_ko": p.get("summary_ko"),
        "must_try": as_list(p.get("must_try")),
        "tags": clean_tags(p.get("tags"), PLACE_TAGS, where),
        "tips_ko": p.get("tips_ko"),
        "website": p.get("website"),
        "awards": as_list(p.get("awards")),
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
        "research": agent,
        "checked": TODAY,
    }


def is_attraction(p: dict) -> bool:
    cat = slugify(p.get("category") or "")
    return cat in ATTRACTION_CATEGORIES or ("name_ko" in p and cat not in FNB_CATEGORIES)


def merge_into(primary: dict, other: dict) -> dict:
    for k, v in other.items():
        if primary.get(k) in (None, "", []) and v not in (None, "", []):
            primary[k] = v
    for k in ("tags", "awards", "sources", "must_try"):
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


def area_rank(area: str) -> int:
    return AREAS.index(area) if area in AREAS else len(AREAS)


def keep_coords(items: list[dict], kind: str, cache: dict) -> None:
    old = {i["id"]: i for i in (load_json(DATA_FILES[kind], {"items": []}).get("items", []))}
    for it in items:
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

    files = sorted(p for p in RAW.glob("*.json") if not p.name.endswith("-data.json"))
    if not files:
        print("no research/raw/*.json files found")
        return 1

    buckets: dict[str, list[dict]] = defaultdict(list)
    candidates: list[dict] = []
    for f in files:
        doc = load_json(f, {})
        agent = doc.get("agent") or f.stem
        for p in doc.get("places", []):
            if not p.get("name"):
                warn(f"[{agent}] entry without name skipped")
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
            c = dict(c)
            c["research"] = agent
            candidates.append(c)

    cache = load_json(DATA / "geocode-cache.json", {}) or {}
    report = []
    for kind in DATA_FILES:
        items = dedupe(buckets.get(kind, []), kind)
        keep_coords(items, kind, cache)
        if kind == "attractions":
            items.sort(key=lambda i: (area_rank(i["area"]), i["priority"], i["name"]))
        else:
            items.sort(key=lambda i: (area_rank(i["area"]), -(i.get("google_rating") or 0), -(i.get("google_reviews") or 0)))
        buckets[kind] = items
        report.append(f"{kind:12s} {len(items):4d}")

    # candidates: drop the ones that ended up in the main lists, dedupe by name
    main_names = {norm_name(i["name"]) for k in ("restaurants", "bars", "shops") for i in buckets[k]}
    seen, cands = set(), []
    for c in candidates:
        key = norm_name(c.get("name", ""))
        if not key or key in main_names or key in seen:
            continue
        seen.add(key)
        cands.append(c)
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
    by_area = Counter(i["area"] for k in ("restaurants", "bars", "shops") for i in buckets[k])
    print("F&B by area:", dict(sorted(by_area.items(), key=lambda kv: area_rank(kv[0]))))
    if warnings:
        print(f"\n{len(warnings)} warnings:")
        for w in warnings:
            print("  -", w)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
