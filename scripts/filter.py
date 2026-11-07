#!/usr/bin/env python3
"""Filter the guide from the command line.

Examples
    python3 scripts/filter.py                                   # all food, best rated first
    python3 scripts/filter.py --area belgisches-viertel --price 1-2
    python3 scripts/filter.py --cuisine korean --cuisine japanese
    python3 scripts/filter.py --near messe --max-km 1.5 --sort distance
    python3 scripts/filter.py --kind bar --category cocktail-bar --min-rating 4.6
    python3 scripts/filter.py --kind sight --tag free --tag rainy-day
    python3 scripts/filter.py --tag koelsch --format md > /tmp/koelsch.md

--near accepts an anchor id from data/areas.json (dom, hbf, messe, deutz, belgisches)
or "lat,lng". Distances are straight-line km; walking minutes assume a 1.3 detour at 4.8 km/h.
"""
from __future__ import annotations

import argparse
import json
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from schema import (  # noqa: E402
    AREAS, CUISINE_GROUPS, DATA, LABELS_KO, haversine_km, load_all, load_json, meets_criteria, walk_minutes,
)

KINDS = {"food": ["restaurants"], "bar": ["bars"], "shop": ["shops"], "sight": ["attractions"],
         "fnb": ["restaurants", "bars", "shops"], "all": ["restaurants", "bars", "shops", "attractions"]}


def parse_price(s: str | None):
    if not s:
        return None
    if "-" in s:
        a, b = s.split("-", 1)
        return int(a), int(b)
    return int(s), int(s)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kind", choices=list(KINDS), default="food")
    ap.add_argument("--area", action="append", choices=AREAS)
    ap.add_argument("--cuisine", action="append", choices=CUISINE_GROUPS)
    ap.add_argument("--category", action="append")
    ap.add_argument("--price", help="price level or range, e.g. 2 or 1-2")
    ap.add_argument("--min-rating", type=float)
    ap.add_argument("--min-reviews", type=int)
    ap.add_argument("--tag", action="append", help="all given tags must match")
    ap.add_argument("--near", help="anchor id (dom, hbf, messe, deutz, belgisches) or lat,lng")
    ap.add_argument("--max-km", type=float)
    ap.add_argument("--sort", choices=["rating", "reviews", "distance", "price", "name"], default="rating")
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
    rows = []
    for kind in KINDS[args.kind]:
        for it in data[kind]:
            if kind != "attractions" and not meets_criteria(it):
                continue
            if args.area and it.get("area") not in args.area:
                continue
            if args.cuisine and it.get("cuisine_group") not in args.cuisine:
                continue
            if args.category and it.get("category") not in args.category:
                continue
            if price and not (it.get("price_level") and price[0] <= it["price_level"] <= price[1]):
                continue
            if args.min_rating and (it.get("google_rating") or 0) < args.min_rating:
                continue
            if args.min_reviews and (it.get("google_reviews") or 0) < args.min_reviews:
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
        "name": lambda r: r["name"].lower(),
    }[args.sort]
    rows.sort(key=keyf)
    if args.limit:
        rows = rows[: args.limit]

    if args.format == "json":
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return 0

    L = LABELS_KO
    header = ["이름", "유형", "지역", "음식", "가격", "구글", "거리"]
    out = []
    for r in rows:
        dist = f"{r['_km']:.1f}km·도보{walk_minutes(r['_km'])}분" if r["_km"] is not None else "-"
        rating = f"{r['google_rating']} ({r['google_reviews']:,})" if r.get("google_rating") else "-"
        out.append([
            r["name"], L["category"].get(r.get("category"), r.get("category") or ""), r.get("area") or "",
            L["cuisine_group"].get(r.get("cuisine_group"), "") if r["_kind"] != "attractions" else "",
            L["price_level"].get(r.get("price_level"), "") if r["_kind"] != "attractions"
            else (r.get("price_note") or ""),
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
