#!/usr/bin/env python3
"""Fill lat/lng in data/*.json from each item's address.

    python3 scripts/geocode.py                     # OpenStreetMap Nominatim (no key, 1 request/s)
    GOOGLE_MAPS_API_KEY=... python3 scripts/geocode.py --provider google
    python3 scripts/geocode.py --only restaurants --limit 20

Results are cached in data/geocode-cache.json (address -> coordinates), so re-runs are cheap.
Points outside the Cologne area are rejected unless the item is a day trip.
Needs outbound access to nominatim.openstreetmap.org (or maps.googleapis.com).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from schema import DATA, DATA_FILES, is_area_wide, load_json, save_json  # noqa: E402

CACHE = DATA / "geocode-cache.json"
USER_AGENT = "koln-guide/0.1 (travel-guide data build; https://github.com/gkk2123/koln-guide)"
# Cologne city limits, generously padded
BBOX = (50.80, 51.12, 6.75, 7.20)  # lat_min, lat_max, lng_min, lng_max


def in_cologne(lat: float, lng: float) -> bool:
    return BBOX[0] <= lat <= BBOX[1] and BBOX[2] <= lng <= BBOX[3]


def http_json(url: str, data: bytes | None = None, headers: dict | None = None):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": USER_AGENT, **(headers or {})})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))


def nominatim(query: str):
    q = urllib.parse.urlencode({"q": query, "format": "jsonv2", "limit": 1, "countrycodes": "de",
                                "accept-language": "de"})
    for wait in (20, 60, 120, None):  # HTTP 429 = slow down: back off and retry a few times
        try:
            res = http_json(f"https://nominatim.openstreetmap.org/search?{q}")
            break
        except urllib.error.HTTPError as e:
            if e.code != 429 or wait is None:
                raise
            print(f"  rate-limited by Nominatim, waiting {wait}s …", flush=True)
            time.sleep(wait)
    time.sleep(1.5)  # usage policy: max 1 request per second
    if res:
        return float(res[0]["lat"]), float(res[0]["lon"]), res[0].get("display_name")
    return None


def google(query: str, key: str):
    q = urllib.parse.urlencode({"address": query, "key": key, "region": "de", "language": "de"})
    res = http_json(f"https://maps.googleapis.com/maps/api/geocode/json?{q}")
    if res.get("status") == "OK":
        top = res["results"][0]
        loc = top["geometry"]["location"]
        return loc["lat"], loc["lng"], top.get("formatted_address")
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--provider", choices=["nominatim", "google"], default="nominatim")
    ap.add_argument("--only", choices=list(DATA_FILES), action="append")
    ap.add_argument("--limit", type=int, default=0, help="stop after N lookups (0 = no limit)")
    ap.add_argument("--force", action="store_true", help="re-geocode items that already have coordinates")
    args = ap.parse_args()

    key = os.environ.get("GOOGLE_MAPS_API_KEY")
    if args.provider == "google" and not key:
        print("GOOGLE_MAPS_API_KEY is not set")
        return 2

    cache = load_json(CACHE, {}) or {}
    lookups = updated = failed = 0
    for kind in args.only or list(DATA_FILES):
        doc = load_json(DATA_FILES[kind], None)
        if not doc:
            continue
        for it in doc["items"]:
            if it.get("lat") is not None and not args.force:
                continue
            addr = it.get("address")
            if is_area_wide(addr):
                it["lat"] = it["lng"] = None
                continue
            queries = [q for q in (addr, f"{it['name']}, Köln" if it.get("area") != "day-trip" else it["name"]) if q]
            hit = None
            for q in queries:
                if q in cache and not args.force:
                    c = cache[q]
                    hit = (c["lat"], c["lng"], c.get("display_name")) if c.get("lat") is not None else None
                else:
                    if args.limit and lookups >= args.limit:
                        break
                    lookups += 1
                    try:
                        hit = google(q, key) if args.provider == "google" else nominatim(q)
                    except Exception as e:  # network errors, HTTP 403 from a proxy, ...
                        print(f"lookup failed ({e}); is the geocoding host reachable?")
                        save_json(CACHE, cache)
                        return 3
                    if hit and it.get("area") != "day-trip" and not in_cologne(hit[0], hit[1]):
                        print(f"  outside Cologne, ignored: {q} -> {hit[:2]}")
                        hit = None
                    cache[q] = {"lat": hit[0] if hit else None, "lng": hit[1] if hit else None,
                                "display_name": hit[2] if hit else None, "provider": args.provider,
                                "date": dt.date.today().isoformat()}
                if hit:
                    break
            if hit:
                it["lat"], it["lng"] = round(hit[0], 6), round(hit[1], 6)
                it["coord_source"] = args.provider
                updated += 1
            else:
                failed += 1
                print(f"  not found: {it['name']} | {addr}")
        save_json(DATA_FILES[kind], doc)
    save_json(CACHE, cache)
    print(f"lookups={lookups} updated={updated} not_found={failed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
