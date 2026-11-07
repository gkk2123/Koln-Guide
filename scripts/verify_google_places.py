#!/usr/bin/env python3
"""Check every place against the Google Places API (New) and store its place ID.

    export GOOGLE_MAPS_API_KEY=...        # a key with "Places API (New)" enabled
    python3 scripts/verify_google_places.py                    # food & drink: place IDs + report
    python3 scripts/verify_google_places.py --store-snapshot   # also overwrite rating/reviews/price
    python3 scripts/verify_google_places.py --only bars --limit 10 --attractions

In a Claude cloud session where the key is saved as a network secret for places.googleapis.com
(header X-Goog-Api-Key), run with --proxy-key: the proxy injects the real key.

For each item it runs one Text Search (name + address, biased to Cologne). By default it stores only
what Google's terms let you keep (google_place_id, google_maps_url built from it, and whether the place
is permanently closed) and prints rating/review/price differences for you to review. Google's terms
restrict caching other Places content (ratings, reviews, photos), so --store-snapshot is opt-in.
Places that are permanently closed or below the bar (4.2 / 50) are left out by scripts/build.py.
Run scripts/build.py afterwards.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.request

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from schema import DATA_FILES, load_json, meets_criteria, save_json  # noqa: E402

ENDPOINT = "https://places.googleapis.com/v1/places:searchText"
FIELDS = ",".join([
    "places.id", "places.displayName", "places.formattedAddress", "places.location",
    "places.rating", "places.userRatingCount", "places.priceLevel", "places.priceRange",
    "places.businessStatus", "places.googleMapsUri",
])
COLOGNE = {"latitude": 50.9375, "longitude": 6.9603}
PRICE = {"PRICE_LEVEL_INEXPENSIVE": 1, "PRICE_LEVEL_MODERATE": 2, "PRICE_LEVEL_EXPENSIVE": 3,
         "PRICE_LEVEL_VERY_EXPENSIVE": 4}


def search(query: str, key: str) -> dict | None:
    body = json.dumps({
        "textQuery": query, "languageCode": "de", "regionCode": "DE", "pageSize": 1,
        "locationBias": {"circle": {"center": COLOGNE, "radius": 20000.0}},
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=body, headers={
        "Content-Type": "application/json", "X-Goog-Api-Key": key, "X-Goog-FieldMask": FIELDS})
    with urllib.request.urlopen(req, timeout=20) as r:
        places = json.loads(r.read().decode()).get("places", [])
    return places[0] if places else None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", choices=["restaurants", "bars", "shops", "attractions"], action="append")
    ap.add_argument("--attractions", action="store_true", help="include attractions")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--store-snapshot", action="store_true", help="also store rating, reviews, price (see Google terms)")
    ap.add_argument("--proxy-key", action="store_true", help="send a placeholder; a network proxy injects the real key")
    args = ap.parse_args()

    key = os.environ.get("GOOGLE_MAPS_API_KEY") or ("injected-by-proxy" if args.proxy_key else None)
    if not key:
        print("Set GOOGLE_MAPS_API_KEY (Places API (New) enabled) first, or use --proxy-key in a session that injects it.")
        return 2

    kinds = args.only or ["restaurants", "bars", "shops"] + (["attractions"] if args.attractions else [])
    today = dt.date.today().isoformat()
    done = changed = dropped = 0
    for kind in kinds:
        doc = load_json(DATA_FILES[kind], None)
        if not doc:
            continue
        for it in doc["items"]:
            if args.limit and done >= args.limit:
                break
            query = f"{it['name']}, {it.get('address') or 'Köln'}"
            try:
                p = search(query, key)
            except Exception as e:
                print(f"request failed for {it['name']}: {e}")
                save_json(DATA_FILES[kind], doc)
                return 3
            done += 1
            time.sleep(0.2)
            if not p:
                print(f"  no match: {query}")
                it["google_match"] = "not-found"
                continue
            before = (it.get("google_rating"), it.get("google_reviews"))
            now = (p.get("rating"), p.get("userRatingCount"))
            it["google_place_id"] = p.get("id")
            it["google_maps_url"] = f"https://www.google.com/maps/place/?q=place_id:{p.get('id')}"
            it["business_status"] = p.get("businessStatus")
            it["google_match"] = (p.get("displayName") or {}).get("text")
            it["verified_at"] = today
            rng = p.get("priceRange") or {}
            lo, hi = (rng.get("startPrice") or {}).get("units"), (rng.get("endPrice") or {}).get("units")
            if before != now:
                changed += 1
                print(f"  {it['name']}: Google {before} -> {now}" + (f", price €{lo}–{hi}" if lo else ""))
            if args.store_snapshot:
                it["google_rating"], it["google_reviews"] = now[0] or it.get("google_rating"), now[1] or it.get("google_reviews")
                it["google_as_of"], it["rating_source"] = today, "Google Places API"
                if lo:
                    it["price_pp"] = {"min": int(lo), "max": int(hi) if hi else None}
                if p.get("priceLevel") in PRICE:
                    it["google_price_level"] = PRICE[p["priceLevel"]]
            if kind != "attractions" and (not meets_criteria(it) or it["business_status"] == "CLOSED_PERMANENTLY"):
                dropped += 1
                print(f"  now excluded: {it['name']} -> {it['google_rating']} ({it['google_reviews']}) {it['business_status']}")
        save_json(DATA_FILES[kind], doc)
    print(f"checked={done} changed={changed} excluded={dropped}. Check 'google_match' for wrong matches, then run scripts/build.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
