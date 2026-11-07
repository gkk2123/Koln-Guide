#!/usr/bin/env python3
"""Re-check Google rating / review count / business status with the Google Places API (New).

    export GOOGLE_MAPS_API_KEY=...        # a key with "Places API (New)" enabled
    python3 scripts/verify_google_places.py               # all food & drink
    python3 scripts/verify_google_places.py --only bars --limit 10
    python3 scripts/verify_google_places.py --attractions # also refresh attraction ratings

For each item it runs one Text Search (name + address, biased to Cologne) and writes back:
google_rating, google_reviews, google_as_of (today), rating_source, google_place_id,
google_maps_url, business_status, and lat/lng when they were missing.
Items that now fall below the bar (rating < 4.2 or < 50 reviews) or are permanently closed
stay in the file but are left out of the guides and the viewer by scripts/build.py.
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
    "places.rating", "places.userRatingCount", "places.priceLevel", "places.businessStatus",
    "places.googleMapsUri",
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
    args = ap.parse_args()

    key = os.environ.get("GOOGLE_MAPS_API_KEY")
    if not key:
        print("Set GOOGLE_MAPS_API_KEY (Places API (New) enabled) first.")
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
            it["google_rating"] = p.get("rating", it.get("google_rating"))
            it["google_reviews"] = p.get("userRatingCount", it.get("google_reviews"))
            it["google_as_of"] = today
            it["rating_source"] = "Google Places API"
            it["google_place_id"] = p.get("id")
            it["google_maps_url"] = p.get("googleMapsUri")
            it["business_status"] = p.get("businessStatus")
            it["google_match"] = (p.get("displayName") or {}).get("text")
            if p.get("priceLevel") in PRICE:
                it["google_price_level"] = PRICE[p["priceLevel"]]
            loc = p.get("location")
            if loc and it.get("lat") is None:
                it["lat"], it["lng"] = loc["latitude"], loc["longitude"]
                it["coord_source"] = "google-places"
            if before != (it["google_rating"], it["google_reviews"]):
                changed += 1
            if kind != "attractions" and (not meets_criteria(it) or it["business_status"] == "CLOSED_PERMANENTLY"):
                dropped += 1
                print(f"  now excluded: {it['name']} -> {it['google_rating']} ({it['google_reviews']}) {it['business_status']}")
        save_json(DATA_FILES[kind], doc)
    print(f"checked={done} changed={changed} excluded={dropped}. Check 'google_match' for wrong matches, then run scripts/build.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
