#!/usr/bin/env python3
"""Filter the guide from the command line.

Examples
    python3 scripts/filter.py                                    # all food, best rated first
    python3 scripts/filter.py --area belgisches-viertel --price 1-2
    python3 scripts/filter.py --country KR --country JP          # Korean + Japanese
    python3 scripts/filter.py --region middle-east --diet halal
    python3 scripts/filter.py --dish ramen --dish noodles --meal late-night
    python3 scripts/filter.py --occasion business --near messe --max-km 1.5 --sort distance
    python3 scripts/filter.py --kind bar --category cocktail-bar --drink cocktails
    python3 scripts/filter.py --kind beer --max-beer 2.6 --sort beer        # cheap Kölsch first
    python3 scripts/filter.py --kind sight --tag free --tag rainy-day
    python3 scripts/filter.py --feature terrace --format md > /tmp/terrace.md

Within one option, values are OR-ed (--country KR --country JP = Korean or Japanese);
different options are AND-ed. --near takes an anchor id from data/areas.json
(dom, hbf, messe, deutz, belgisches) or "lat,lng". Distances are straight-line km;
walking minutes assume a 1.3 detour at 4.8 km/h.
"""
from __future__ import annotations

import argparse
import json
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from schema import (  # noqa: E402
    AREAS, COUNTRIES, DATA, DIET, DISHES, DRINKS, FEATURES, LABELS_KO, MEALS, OCCASIONS, REGIONS, VIBE,
    haversine_km, load_all, load_json, meets_criteria, walk_minutes,
)

KINDS = {"food": ["restaurants"], "bar": ["bars"], "shop": ["shops"], "sight": ["attractions"],
         "beer": ["restaurants", "bars"],
         "fnb": ["restaurants", "bars", "shops"], "all": ["restaurants", "bars", "shops", "attractions"]}
FACET_ARGS = [  # (option, field, allowed values)
    ("dish", "dishes", DISHES), ("diet", "diet", DIET), ("meal", "meals", MEALS),
    ("occasion", "occasions", OCCASIONS), ("feature", "features", FEATURES), ("drink", "drinks", DRINKS),
    ("vibe", "vibe", VIBE),
]


def parse_price(s: str | None):
    if not s:
        return None
    a, _, b = s.partition("-")
    return int(a), int(b or a)


def any_in(values, wanted) -> bool:
    values = values if isinstance(values, list) else [values]
    return any(v in values for v in wanted)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kind", choices=list(KINDS), default="food")
    ap.add_argument("--area", action="append", choices=AREAS)
    ap.add_argument("--region", action="append", choices=list(REGIONS), help="cuisine region")
    ap.add_argument("--country", action="append", type=str.upper, choices=list(COUNTRIES), help="cuisine country code")
    ap.add_argument("--category", action="append")
    ap.add_argument("--style", action="append", help="bistro, wine-bar, tapas, izakaya, pizzeria, ... (schema.STYLES)")
    for opt, _field, allowed in FACET_ARGS:
        ap.add_argument(f"--{opt}", action="append", choices=list(allowed))
    ap.add_argument("--price", help="price level or range, e.g. 2 or 1-2")
    ap.add_argument("--max-pp", type=int, help="max EUR per person (uses price_pp, else the price level's upper bound)")
    ap.add_argument("--max-beer", type=float, help="max EUR for a 0.2 l Kölsch / cheapest draft")
    ap.add_argument("--min-rating", type=float)
    ap.add_argument("--min-reviews", type=int)
    ap.add_argument("--walk-in", action="store_true", help="no reservation needed")
    ap.add_argument("--card", action="store_true", help="exclude cash-only places")
    ap.add_argument("--tag", action="append", help="attraction tags; all given tags must match")
    ap.add_argument("--near", help="anchor id (dom, hbf, messe, deutz, belgisches) or lat,lng")
    ap.add_argument("--max-km", type=float)
    ap.add_argument("--sort", choices=["rating", "reviews", "distance", "price", "beer", "name"], default="rating")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--format", choices=["table", "md", "json"], default="table")
    args = ap.parse_args()

    origin = None
    if args.near:
        anchors = {a["id"]: a for a in (load_json(DATA / "areas.json", {}) or {}).get("anchors", [])}
        if args.near in anchors:
            origin = (anchors[args.near]["lat"], anchors[args.near]["lng"])
        else:
            try:
                lat, lng = (float(x) for x in args.near.split(","))
                origin = (lat, lng)
            except ValueError:
                ap.error(f"--near: unknown anchor '{args.near}'")
    if args.max_km and not origin:
        ap.error("--max-km needs --near")

    data = load_all()
    price = parse_price(args.price)
    level_cap = {1: 15, 2: 30, 3: 60, 4: 10_000}
    rows = []
    for kind in KINDS[args.kind]:
        for it in data[kind]:
            if kind != "attractions" and not meets_criteria(it):
                continue
            if args.kind == "beer" and it.get("category") not in ("brauhaus", "kneipe", "beer-bar"):
                continue
            if args.max_beer and not (it.get("beer_price_eur") and it["beer_price_eur"] <= args.max_beer):
                continue
            if args.area and it.get("area") not in args.area:
                continue
            if args.region and it.get("cuisine_region") not in args.region:
                continue
            if args.country and not any_in(it.get("cuisine_country") or [], args.country):
                continue
            if args.style and it.get("style") not in args.style:
                continue
            if args.category and it.get("category") not in args.category:
                continue
            if any(getattr(args, opt) and not any_in(it.get(field) or [], getattr(args, opt))
                   for opt, field, _ in FACET_ARGS):
                continue
            if price and not (it.get("price_level") and price[0] <= it["price_level"] <= price[1]):
                continue
            if args.max_pp:
                cap = (it.get("price_pp") or {}).get("max") or level_cap.get(it.get("price_level"))
                if cap is None or cap > args.max_pp:
                    continue
            if args.min_rating and (it.get("google_rating") or 0) < args.min_rating:
                continue
            if args.min_reviews and (it.get("google_reviews") or 0) < args.min_reviews:
                continue
            if args.walk_in and it.get("reservation") in ("required",):
                continue
            if args.card and it.get("payment") == "cash-only":
                continue
            if args.tag and not all(t in (it.get("tags") or []) for t in args.tag):
                continue
            km = None
            if origin and it.get("lat") is not None:
                km = haversine_km(origin[0], origin[1], it["lat"], it["lng"])
            if args.max_km and (km is None or km > args.max_km):
                continue
            rows.append({**it, "_kind": kind, "_km": km})

    keyf = {
        "rating": lambda r: (-(r.get("google_rating") or 0), -(r.get("google_reviews") or 0)),
        "reviews": lambda r: -(r.get("google_reviews") or 0),
        "distance": lambda r: (r["_km"] is None, r["_km"] or 0),
        "price": lambda r: (r.get("price_level") or 9, -(r.get("google_rating") or 0)),
        "beer": lambda r: (r.get("beer_price_eur") or 99, -(r.get("google_rating") or 0)),
        "name": lambda r: r["name"].lower(),
    }[args.sort]
    rows.sort(key=keyf)
    if args.limit:
        rows = rows[: args.limit]

    if args.format == "json":
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return 0

    L = LABELS_KO
    header = ["이름", "유형", "지역", "나라", "가격", "구글", "거리"]
    out = []
    for r in rows:
        dist = f"{r['_km']:.1f}km·도보{walk_minutes(r['_km'])}분" if r["_km"] is not None else "-"
        rating = f"{r['google_rating']} ({r['google_reviews']:,})" if r.get("google_rating") else "-"
        food = "·".join(L["country"].get(c, c) for c in r.get("cuisine_country") or []) or \
            L["region"].get(r.get("cuisine_region"), "")
        out.append([
            r["name"], L["style"].get(r.get("style") or "", "") or L["category"].get(r.get("category"), r.get("category") or ""), r.get("area") or "",
            food if r["_kind"] != "attractions" else "",
            L["price_level"].get(r.get("price_level"), "") if r["_kind"] != "attractions" else (r.get("price_note") or ""),
            rating, dist,
        ])
    if args.format == "md":
        print("| " + " | ".join(header) + " |")
        print("|" + "---|" * len(header))
        for row in out:
            print("| " + " | ".join(str(c).replace("|", "/") for c in row) + " |")
    else:
        widths = [max(len(str(x)) for x in col) for col in zip(header, *out)] if out else [len(h) for h in header]
        print("  ".join(h.ljust(w) for h, w in zip(header, widths)))
        for row in out:
            print("  ".join(str(c).ljust(w) for c, w in zip(row, widths)))
    print(f"\n{len(rows)}곳", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
