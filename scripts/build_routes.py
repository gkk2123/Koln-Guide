#!/usr/bin/env python3
"""Build the running routes from data/routes-spec.json.

    python3 scripts/build_routes.py            # fetch walking geometry and write all outputs

For each route it asks the OpenStreetMap foot router (routing.openstreetmap.de, the same service
openstreetmap.org uses) for a path through the stops in order, then writes
  routes/koln-running.kml          Google My Maps import (mymaps.google.com -> Create -> Import)
  routes/koln-running-<id>.gpx     running apps / watches (Strava, Garmin, Komoot …)
  routes/koln-running.geojson      full geometry
  data/routes.json                 simplified geometry + stops + km markers + Google Maps links for the viewer
Only public places are used. Map data © OpenStreetMap contributors (ODbL).
"""
from __future__ import annotations

import json
import math
import sys
import time
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
from schema import DATA, ROOT, load_json, save_json  # noqa: E402

ROUTER = "https://routing.openstreetmap.de/routed-foot/route/v1/driving/"
UA = {"User-Agent": "koln-guide/0.1 (running-route build; https://github.com/gkk2123/koln-guide)"}
OUT = ROOT / "routes"


def hav(a, b) -> float:
    r = 6371008.8
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    dp, dl = p2 - p1, math.radians(b[1] - a[1])
    x = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(x))


def simplify(pts: list, tol_m: float = 4.0) -> list:
    """Douglas-Peucker on lat/lng in metres (equirectangular, fine at city scale)."""
    if len(pts) < 3:
        return pts
    k = math.cos(math.radians(pts[0][0]))
    xy = [((p[1]) * 111320 * k, p[0] * 110540) for p in pts]

    def dist(i, a, b):
        (x, y), (x1, y1), (x2, y2) = xy[i], xy[a], xy[b]
        dx, dy = x2 - x1, y2 - y1
        if dx == dy == 0:
            return math.hypot(x - x1, y - y1)
        t = max(0, min(1, ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)))
        return math.hypot(x - (x1 + t * dx), y - (y1 + t * dy))

    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        best, idx = 0.0, None
        for i in range(a + 1, b):
            d = dist(i, a, b)
            if d > best:
                best, idx = d, i
        if idx is not None and best > tol_m:
            keep[idx] = True
            stack += [(a, idx), (idx, b)]
    return [p for p, k_ in zip(pts, keep) if k_]


def fetch(coords: list) -> dict:
    url = ROUTER + ";".join(f"{lng:.6f},{lat:.6f}" for lat, lng in coords) + \
        "?overview=full&geometries=geojson&steps=false"
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return json.loads(r.read())["routes"][0]


def sun_times(day, lat=50.9413, lng=6.9583, tz=1) -> tuple[str, str]:
    """Sunrise/sunset (NOAA approximation, local CET)."""
    n = day.timetuple().tm_yday
    g = 2 * math.pi / 365 * (n - 1)
    eq = 229.18 * (0.000075 + 0.001868 * math.cos(g) - 0.032077 * math.sin(g) - 0.014615 * math.cos(2 * g) - 0.040849 * math.sin(2 * g))
    decl = (0.006918 - 0.399912 * math.cos(g) + 0.070257 * math.sin(g) - 0.006758 * math.cos(2 * g)
            + 0.000907 * math.sin(2 * g) - 0.002697 * math.cos(3 * g) + 0.00148 * math.sin(3 * g))
    ha = math.degrees(math.acos(math.cos(math.radians(90.833)) / (math.cos(math.radians(lat)) * math.cos(decl))
                                - math.tan(math.radians(lat)) * math.tan(decl)))
    out = []
    for sign in (1, -1):
        m = 720 - 4 * (lng + sign * ha) - eq + tz * 60
        out.append(f"{int(m // 60):02d}:{int(m % 60):02d}")
    return out[0], out[1]


def gmaps_links(stops: list) -> list:
    """Google Maps walking directions; Maps URLs take at most 9 waypoints, so long loops are split."""
    links, i = [], 0
    while i < len(stops) - 1:
        seg = stops[i:i + 11]  # origin + up to 9 waypoints + destination
        o, d, w = seg[0], seg[-1], seg[1:-1]
        url = ("https://www.google.com/maps/dir/?api=1&travelmode=walking"
               f"&origin={o['lat']},{o['lng']}&destination={d['lat']},{d['lng']}")
        if w:
            url += "&waypoints=" + "%7C".join(f"{s['lat']},{s['lng']}" for s in w)
        links.append({"label": f"{o['name_ko']} → {d['name_ko']}", "url": url})
        i += len(seg) - 1
    return links


def main() -> int:
    spec = load_json(DATA / "routes-spec.json")
    attractions = {a["id"] for a in (load_json(DATA / "attractions.json", {}) or {}).get("items", [])}
    stops = spec["stops"]
    for sid, s in stops.items():
        if s.get("attraction_id") and s["attraction_id"] not in attractions:
            print(f"  note: stop {sid} links to unknown attraction id {s['attraction_id']}")
            s["attraction_id"] = None

    OUT.mkdir(exist_ok=True)
    viewer, features, kml_folders = [], [], []
    for rt in spec["routes"]:
        seq = []
        for k in rt["order"]:  # a [lat, lng] entry is a hidden via point that only shapes the path
            seq.append({"id": None, "lat": k[0], "lng": k[1], "hidden": True} if isinstance(k, list) else dict(stops[k], id=k))
        r = fetch([(s["lat"], s["lng"]) for s in seq])
        time.sleep(1.5)
        geom = [[c[1], c[0]] for c in r["geometry"]["coordinates"]]  # -> [lat, lng]
        # cumulative distance along the geometry and 1 km markers
        cum, markers, next_km = [0.0], [], 1000
        for a, b in zip(geom, geom[1:]):
            seg = hav(a, b)
            while cum[-1] + seg >= next_km:
                t = (next_km - cum[-1]) / seg
                markers.append({"km": next_km // 1000, "lat": round(a[0] + t * (b[0] - a[0]), 6),
                                "lng": round(a[1] + t * (b[1] - a[1]), 6)})
                next_km += 1000
            cum.append(cum[-1] + seg)
        total = cum[-1]
        legs, km = [], 0.0
        for leg in r["legs"]:
            km += leg["distance"]
            legs.append(round(km / 1000, 2))
        route_stops, n_vis = [], 0
        for i, s in enumerate(seq):
            if s.get("hidden"):
                continue
            route_stops.append({"n": n_vis, "id": s["id"], "name_ko": s["name_ko"], "name": s["name"], "type": s["type"],
                                "desc_ko": s["desc_ko"], "attraction_id": s.get("attraction_id"),
                                "lat": s["lat"], "lng": s["lng"], "km": 0.0 if i == 0 else legs[i - 1]})
            n_vis += 1
        viewer.append({"id": rt["id"], "name_ko": rt["name_ko"], "color": rt["color"],
                       **{k: rt.get(k) for k in ("label_ko", "token", "tags", "surface_ko", "best_ko", "local_ko", "sources")},
                       "distance_km": round(total / 1000, 2), "router_km": round(r["distance"] / 1000, 2),
                       "stops": route_stops, "km_markers": markers,
                       "path": [[round(p[0], 6), round(p[1], 6)] for p in simplify(geom)],
                       "gmaps": gmaps_links(route_stops)})
        features.append({"type": "Feature", "properties": {"id": rt["id"], "name": rt["name_ko"],
                                                           "distance_km": round(total / 1000, 2)},
                         "geometry": {"type": "LineString", "coordinates": [[p[1], p[0]] for p in geom]}})
        for s in route_stops[:-1]:
            features.append({"type": "Feature", "properties": {"route": rt["id"], "n": s["n"], "name": s["name_ko"],
                                                               "km": s["km"]},
                             "geometry": {"type": "Point", "coordinates": [s["lng"], s["lat"]]}})

        # KML folder
        line = " ".join(f"{p[1]:.6f},{p[0]:.6f},0" for p in geom)
        pms = [f"""      <Placemark><name>{escape(rt['name_ko'])} ({total / 1000:.1f} km)</name><styleUrl>#line-{rt['id']}</styleUrl>
        <LineString><tessellate>1</tessellate><coordinates>{line}</coordinates></LineString></Placemark>"""]
        for s in route_stops[:-1]:
            label = "출발·도착" if s["n"] == 0 else f"{s['n']}"
            pms.append(f"""      <Placemark><name>{escape(label)}. {escape(s['name_ko'])} ({escape(s['name'])})</name>
        <description>{escape(s['type'])} · 출발점에서 {s['km']:.1f} km. {escape(s['desc_ko'])}</description>
        <styleUrl>#stop-{rt['id']}</styleUrl><Point><coordinates>{s['lng']:.6f},{s['lat']:.6f},0</coordinates></Point></Placemark>""")
        kml_folders.append(f"""    <Folder><name>{escape(rt['name_ko'])} — {total / 1000:.1f} km</name>
{chr(10).join(pms)}
    </Folder>""")

        # GPX
        trkpts = "\n".join(f'      <trkpt lat="{p[0]:.6f}" lon="{p[1]:.6f}"/>' for p in geom)
        wpts = "\n".join(f'  <wpt lat="{s["lat"]:.6f}" lon="{s["lng"]:.6f}"><name>{escape(s["name_ko"])}</name>'
                         f'<desc>{escape(s["type"])} · {s["km"]:.1f} km</desc></wpt>' for s in route_stops[:-1])
        (OUT / f"koln-running-{rt['id']}.gpx").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="koln-guide" xmlns="http://www.topografix.com/GPX/1/1">
  <metadata><name>Köln running — {escape(rt['name_ko'])}</name>
    <copyright author="OpenStreetMap contributors"><license>https://opendatacommons.org/licenses/odbl/</license></copyright></metadata>
{wpts}
  <trk><name>{escape(rt['name_ko'])} ({total / 1000:.1f} km)</name><trkseg>
{trkpts}
  </trkseg></trk>
</gpx>
""", encoding="utf-8")
        print(f"{rt['id']}: {total / 1000:.2f} km, {len(geom)} points -> {len(viewer[-1]['path'])} simplified, "
              f"{len(markers)} km markers, {len(viewer[-1]['gmaps'])} Google Maps link(s)")

    styles = "\n".join(f"""    <Style id="line-{rt['id']}"><LineStyle><color>ff{rt['color'][4:6]}{rt['color'][2:4]}{rt['color'][0:2]}</color><width>5</width></LineStyle></Style>
    <Style id="stop-{rt['id']}"><IconStyle><scale>1.0</scale></IconStyle></Style>""" for rt in spec["routes"])
    (OUT / "koln-running.kml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>쾰른 러닝 코스 (Köln running routes)</name>
    <description>프리젠플라츠 출발·도착. 경로: OpenStreetMap 보행 경로 (© OpenStreetMap contributors, ODbL).</description>
{styles}
{chr(10).join(kml_folders)}
  </Document>
</kml>
""", encoding="utf-8")
    (OUT / "koln-running.geojson").write_text(json.dumps({"type": "FeatureCollection", "features": features},
                                                         ensure_ascii=False), encoding="utf-8")
    import datetime as dt
    today = dt.date.today()
    sun = []
    for d in range(0, 50, 7):
        day = today + dt.timedelta(days=d)
        rise, sett = sun_times(day)
        sun.append({"date": day.isoformat(), "sunrise": rise, "sunset": sett})
    save_json(DATA / "routes.json", {"meta": {"source": "OpenStreetMap foot routing (routing.openstreetmap.de)",
                                              "attribution": "© OpenStreetMap contributors (ODbL)",
                                              "sun": "NOAA approximation for Köln (CET)"},
                                     "rhine": spec.get("rhine", []), "sun": sun, "routes": viewer,
                                     "local_spots": spec.get("local_spots", [])})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
