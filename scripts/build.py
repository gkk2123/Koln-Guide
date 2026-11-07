#!/usr/bin/env python3
"""Build the generated outputs from data/*.json.

    KOLN_GUIDE_PASSWORD=... python3 scripts/build.py   # guides/tables/*.md + docs/ (encrypted GitHub Pages site)
    python3 scripts/build.py --artifact out.html       # also a single self-contained page (data inlined)

docs/ is password-protected (data/site.json): the guide data is written only as AES-256-GCM ciphertext
(docs/data.enc.js) and the page asks for the password. Without KOLN_GUIDE_PASSWORD, docs/ is left as it is.

Food & drink that no longer meet the bar (Google >= 4.2 and >= 50 reviews) or are marked
CLOSED_PERMANENTLY are left out of every output.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import gzip
import hashlib
import json
import os
import shutil
import re
import sys
import urllib.parse
from collections import defaultdict

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from schema import (  # noqa: E402
    AREAS, BAR_CATEGORIES, DATA, DISHES, DOCS, GUIDES, LABELS_KO, MIN_RATING, MIN_REVIEWS, REGIONS, ROOT,
    haversine_km, load_all, load_json, meets_criteria, walk_minutes,
)

TEMPLATE = ROOT / "scripts" / "templates" / "viewer.html"
TABLES = GUIDES / "tables"
L = LABELS_KO


# ---------------------------------------------------------------- helpers
def esc(s) -> str:
    return re.sub(r"\s+", " ", str(s or "")).replace("|", "/").strip()


def maps_url(it: dict) -> str:
    if it.get("google_maps_url"):
        return it["google_maps_url"]
    q = f"{it['name']} {it.get('address') or 'Köln'}"
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(q)


def rating(it: dict) -> str:
    if it.get("google_rating") is None:
        return "–"
    n = it.get("google_reviews")
    return f"★{it['google_rating']:.1f} ({n:,})" if n else f"★{it['google_rating']:.1f}"


def price(it: dict) -> str:
    return L["price_level"].get(it.get("price_level"), "–")


def km(it: dict, anchor: str) -> str:
    d = (it.get("dist") or {}).get(anchor)
    return f"{d:.1f}km" if d is not None else "–"


def food_label(it: dict) -> str:
    names = [L["country"].get(c, c) for c in it.get("cuisine_country") or []]
    if names:
        return " · ".join(names)
    return L["region"].get(it.get("cuisine_region"), "") if it.get("cuisine_region") else ""


def by_rating(rows: list[dict]) -> list[dict]:
    return sorted(rows, key=lambda i: (-(i.get("google_rating") or 0), -(i.get("google_reviews") or 0)))


DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
DAY_KO = {"mon": "월", "tue": "화", "wed": "수", "thu": "목", "fri": "금", "sat": "토", "sun": "일"}


def hours_summary(h: dict | None) -> str:
    """{'mon': 'closed', 'tue': '10:00-18:00', ...} -> '화–일 10:00–18:00 · 월 휴관'."""
    if not h:
        return ""
    groups = []
    for i, d in enumerate(DAYS):
        v = h.get(d)
        if groups and groups[-1][2] == v and groups[-1][1] == i - 1:
            groups[-1] = (groups[-1][0], i, v)
        else:
            groups.append((i, i, v))
    open_parts, closed = [], []
    for a, b, v in groups:
        if v is None:
            continue
        days = DAY_KO[DAYS[a]] if a == b else f"{DAY_KO[DAYS[a]]}–{DAY_KO[DAYS[b]]}"
        if v == "closed":
            closed.append(days)
        else:
            open_parts.append(f"{days} {v.replace('-', '–').replace(',', ', ')}")
    return " · ".join(open_parts + ([f"{', '.join(closed)} 휴관"] if closed else []))


def md(iso: str) -> str:
    return f"{int(iso[5:7])}/{int(iso[8:10])}"


def date_exceptions_summary(dh: dict | None) -> str:
    """{'2026-11-16'..'2026-11-26': 'closed', '2026-12-03': '11:00-21:00'} -> '11/16–26 휴관 · 12/3 11:00–21:00'."""
    import datetime as _dt
    by_val: dict[str, list] = {}
    for d, v in sorted((dh or {}).items()):
        by_val.setdefault(v, []).append(_dt.date.fromisoformat(d))
    out = []
    for v, ds in by_val.items():
        runs: list[list] = []
        for d in ds:
            if runs and (d - runs[-1][1]).days == 1:
                runs[-1][1] = d
            else:
                runs.append([d, d])
        labels, prev_month = [], None
        for a, b in runs:
            lab = f"{a.month}/{a.day}" if a.month != prev_month else str(a.day)
            if b != a:
                lab += "–" + (f"{b.month}/{b.day}" if b.month != a.month else str(b.day))
            prev_month = b.month
            labels.append(lab)
        what = "휴관" if v == "closed" else "운영(시간 미확인)" if v == "open" else v.replace("-", "–").replace(",", ", ")
        out.append(f"{'·'.join(labels)} {what}")
    return " · ".join(out)


def season_text(i: dict) -> str:
    se = i.get("season") or {}
    if not se.get("start"):
        return ""
    return md(se["start"]) if se.get("end") in (None, se["start"]) else f"{md(se['start'])}–{md(se['end'])}"


CONF_KO = {"high": "공식 2026", "medium": "공식(날짜 미표기)·신뢰 출처", "low": "참고용"}
KEY_DATES = ["2026-12-24", "2026-12-25", "2026-12-26", "2026-12-31", "2027-01-01"]


def eur(x) -> str:
    if x is None:
        return ""
    return "무료" if x == 0 else (f"€{x:.0f}" if float(x).is_integer() else f"€{x:.2f}")


def tickets_summary(t: list | None) -> str:
    return " · ".join(f"{x['label_ko']} {eur(x.get('eur'))}".strip() for x in t or [])


def kind_label(i: dict) -> str:
    """Style (비스트로, 와인바, 타파스 ...) when known, else the broad category."""
    return L["style"].get(i.get("style") or "", "") or L["category"].get(i["category"], i["category"])


def area_name(areas: dict, aid: str) -> str:
    a = areas.get(aid)
    return a["name_ko"] if a else aid


def table(header: list[str], rows: list[list]) -> str:
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(esc(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def banner(title: str, generated: str) -> str:
    return (f"# {title}\n\n"
            f"> 자동 생성 파일입니다 — 직접 고치지 말고 `data/*.json`을 수정한 뒤 `python3 scripts/build.py`를 실행하세요.\n"
            f"> 기준: 구글 평점 {MIN_RATING}+ · 리뷰 {MIN_REVIEWS}+ · 빌드 {generated}. "
            f"거리는 직선거리(km)이며 좌표가 없는 곳은 '–'로 표시됩니다.\n")


# ---------------------------------------------------------------- outputs
def write_tables(data: dict, areas: dict, generated: str) -> list[str]:
    TABLES.mkdir(parents=True, exist_ok=True)
    written = []
    food, bars, sights = data["restaurants"], data["bars"], data["attractions"]

    def name_cell(it):
        return f"[{esc(it['name'])}]({maps_url(it)})"

    # by area
    parts = [banner("지역별 맛집", generated)]
    for aid in AREAS:
        rows = [i for i in food if i["area"] == aid]
        if not rows:
            continue
        a = areas.get(aid, {})
        parts.append(f"\n## {a.get('name_ko', aid)} ({a.get('name_de', '')}) — {len(rows)}곳\n\n{a.get('summary_ko', '')}\n")
        parts.append(table(
            ["이름(지도)", "유형", "나라·음식", "가격", "구글", "대성당", "메쎄", "한 줄 소개", "추천"],
            [[name_cell(i), kind_label(i),
              " · ".join(x for x in (food_label(i), i.get("cuisine")) if x), price(i), rating(i),
              km(i, "dom"), km(i, "messe"), i.get("summary_ko"), ", ".join(i.get("must_try") or [])[:120]] for i in rows]))
    (TABLES / "restaurants-by-area.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    written.append("restaurants-by-area.md")

    # by region -> country
    parts = [banner("나라·문화권별 맛집", generated),
             "\n문화권 → 나라 순서. 카페·디저트처럼 나라 구분이 없는 곳은 [요리 종류별 표](restaurants-by-dish.md)에 있습니다.\n"]
    for rid, rlabel in REGIONS.items():
        rows = [i for i in food if i.get("cuisine_region") == rid]
        if not rows:
            continue
        parts.append(f"\n## {rlabel} — {len(rows)}곳\n")
        by_c = defaultdict(list)
        for i in rows:
            by_c[(i.get("cuisine_country") or ["–"])[0]].append(i)
        for code in sorted(by_c, key=lambda c: -len(by_c[c])):
            if len(by_c) > 1 or code != "INT":
                parts.append(f"\n### {L['country'].get(code, '기타')} ({len(by_c[code])})\n")
            parts.append(table(["이름(지도)", "지역", "유형", "가격", "구글", "요리", "추천"],
                               [[name_cell(i), area_name(areas, i["area"]), kind_label(i), price(i),
                                 rating(i), ", ".join(L["dish"].get(d, d) for d in i.get("dishes") or []),
                                 ", ".join(i.get("must_try") or [])[:120]] for i in by_rating(by_c[code])]))
    (TABLES / "restaurants-by-cuisine.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    written.append("restaurants-by-cuisine.md")

    # by dish
    parts = [banner("요리 종류별", generated)]
    present = [d for d in DISHES if any(d in (i.get("dishes") or []) for i in food)]
    parts.append("\n" + " · ".join(f"{DISHES[d]}" for d in present) + "\n")
    for d in present:
        rows = by_rating([i for i in food if d in (i.get("dishes") or [])])
        parts.append(f"\n## {DISHES[d]} — {len(rows)}곳\n")
        parts.append(table(["이름(지도)", "지역", "나라", "가격", "구글"],
                           [[name_cell(i), area_name(areas, i["area"]), food_label(i), price(i), rating(i)] for i in rows]))
    (TABLES / "restaurants-by-dish.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    written.append("restaurants-by-dish.md")

    # by price
    parts = [banner("가격대별 맛집", generated),
             "\n1인 음식값 기준(음료 제외): € ~15 · €€ 15–30 · €€€ 30–60 · €€€€ 60+\n"]
    for lvl in (1, 2, 3, 4):
        rows = sorted([i for i in food if i.get("price_level") == lvl],
                      key=lambda i: (-(i.get("google_rating") or 0), -(i.get("google_reviews") or 0)))
        if not rows:
            continue
        parts.append(f"\n## {L['price_level'][lvl]} — {len(rows)}곳\n")
        parts.append(table(["이름(지도)", "지역", "음식", "구글", "가격 메모"],
                           [[name_cell(i), area_name(areas, i["area"]), food_label(i),
                             rating(i), i.get("price_note")] for i in rows]))
    (TABLES / "restaurants-by-price.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    written.append("restaurants-by-price.md")

    # bars (+ wine shops)
    parts = [banner("바 (칵테일·맥주·와인)", generated),
             "\n칵테일바 가격대는 칵테일 1잔 기준: € ~10 · €€ 10–14 · €€€ 15–19 · €€€€ 20+\n"]
    for cat in BAR_CATEGORIES + ["wine-shop"]:
        src = data["shops"] if cat == "wine-shop" else bars
        rows = sorted([i for i in src if i["category"] == cat],
                      key=lambda i: (-(i.get("google_rating") or 0), -(i.get("google_reviews") or 0)))
        if not rows:
            continue
        parts.append(f"\n## {L['category'][cat]} — {len(rows)}곳\n")
        parts.append(table(["이름(지도)", "지역", "가격", "구글", "수상·인정", "한 줄 소개"],
                           [[name_cell(i), area_name(areas, i["area"]), f"{price(i)} {i.get('price_note') or ''}",
                             rating(i), "; ".join(i.get("awards") or []), i.get("summary_ko")] for i in rows]))
    (TABLES / "bars.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    written.append("bars.md")

    # attractions
    parts = [banner("관광지", generated).replace(f"기준: 구글 평점 {MIN_RATING}+ · 리뷰 {MIN_REVIEWS}+ · ", "")]
    for cat in L["category"]:
        rows = [i for i in sights if i["category"] == cat]
        if not rows:
            continue
        rows.sort(key=lambda i: (i.get("priority") or 2, i["name"]))
        parts.append(f"\n## {L['category'][cat]} — {len(rows)}곳\n")
        parts.append(table(["이름(지도)", "지역", "요금", "운영(11–12월)", "소요", "상태", "한 줄 소개"],
                           [[f"[{esc(i.get('name_ko') or i['name'])}]({maps_url(i)}) {esc(i['name'])}",
                             area_name(areas, i["area"]),
                             i.get("price_note") or ("무료" if i.get("price_eur") == 0 else "–"),
                             hours_summary(i.get("hours")) or (i.get("hours_note") or "–")[:60],
                             f"{i['duration_min']}분" if i.get("duration_min") else "–",
                             status_text(i), i.get("summary_ko")] for i in rows]))
    (TABLES / "attractions.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    written.append("attractions.md")

    # tickets & opening hours
    parts = [banner("관광지 입장권·운영시간", generated).replace(f"기준: 구글 평점 {MIN_RATING}+ · 리뷰 {MIN_REVIEWS}+ · ", ""),
             "\n운영시간은 2026년 11–12월 기준이에요. 예배 중인 성당, 공휴일(12/24·25·26·31, 1/1)은 달라질 수 있으니 방문 전 공식 사이트를 확인하세요.\n"]
    passes = load_json(DATA / "passes.json", None)
    if passes:
        parts.append("\n## 패스·할인\n")
        parts.append(table(["패스", "가격", "내용", "출처"],
                           [[x.get("name_ko"), x.get("price_ko"), x.get("note_ko"),
                             " ".join(f"[{n + 1}]({u})" for n, u in enumerate(x.get("sources") or []))] for x in passes.get("items", [])]))
    ticketed = [i for i in sights if i.get("tickets") or i.get("hours") or i.get("status") in ("closed-renovation", "temporary-location")]
    mon = sorted((i for i in ticketed if (i.get("hours") or {}).get("mon") == "closed" and i.get("status") in ("open", "temporary-location")
                  and any(v not in (None, "closed") for v in i["hours"].values())), key=lambda i: i["name"])
    if mon:
        parts.append("\n**월요일 휴관:** " + ", ".join(esc(i.get("name_ko") or i["name"]) for i in mon) + "\n")
    holiday = [i for i in ticketed if any(d in (i.get("date_hours") or {}) for d in KEY_DATES)]
    if holiday:
        parts.append("\n## 연말·연초 특별 일정\n\n공식 사이트에 나온 날짜만 적었어요. –는 특별 안내를 찾지 못한 날이에요"
                     "(평소 시간일 수도, 확인이 안 된 것일 수도 있어요). 크리스마스 마켓은 대부분 12/23에 끝나요.\n")
        parts.append(table(["이름"] + [f"{md(d)}" for d in KEY_DATES],
                           [[esc(i.get("name_ko") or i["name"])] +
                            [("휴관" if v == "closed" else "운영(시간 미확인)" if v == "open" else v.replace("-", "–"))
                             if (v := (i["date_hours"] or {}).get(d)) else "–" for d in KEY_DATES]
                            for i in sorted(holiday, key=lambda i: (i.get("priority") or 2, i["name"]))]))
    for cat in L["category"]:
        rows = sorted([i for i in ticketed if i["category"] == cat], key=lambda i: (i.get("priority") or 2, i["name"]))
        if not rows:
            continue
        parts.append(f"\n## {L['category'][cat]}\n")
        parts.append(table(["이름", "입장권", "운영시간", "마지막 입장", "예약", "무료·할인", "메모", "확인"],
                           [[f"[{esc(i.get('name_ko') or i['name'])}]({i.get('website') or maps_url(i)})",
                             tickets_summary(i.get("tickets")) or i.get("price_note") or "–",
                             " · ".join(x for x in (season_text(i), hours_summary(i.get("hours")), date_exceptions_summary(i.get("date_hours"))) if x) or "–",
                             i.get("last_entry") or "–",
                             {"required": "필수", "recommended": "권장", "not-needed": "필요 없음"}.get(i.get("booking"), "–") +
                             (f" · [온라인 예매]({i['booking_url']})" if i.get("booking_url") else ""),
                             i.get("free_note") or "–",
                             ((f"⚠ {i['partial_closure']['what_ko']} ({i['partial_closure']['end']}까지) " if i.get("partial_closure") else "") +
                              (i.get("hours_note") or ""))[:160],
                             (i.get("info_checked") or "") + (f" · {CONF_KO.get(i['info_confidence'], i['info_confidence'])}" if i.get("info_confidence") else "")]
                            for i in rows]))
    (TABLES / "attractions-tickets-hours.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    written.append("attractions-tickets-hours.md")

    # beer pubs
    beer = [i for i in food if i["category"] == "brauhaus"] + [i for i in bars if i["category"] in ("kneipe", "beer-bar")]
    parts = [banner("맥주 펍 — 브라우하우스·크나이페·맥주바", generated),
             "\n쾰시는 0.2 l 잔(Stange) 기준이고, 맥주 가격은 출처가 있는 곳만 적었습니다. "
             "현금만 받는 곳이 많으니 현금을 챙기세요.\n"]
    priced = sorted([i for i in beer if i.get("beer_price_eur")], key=lambda i: (i["beer_price_eur"], -(i.get("google_rating") or 0)))
    if priced:
        parts.append(f"\n## 맥주 싼 순 — {len(priced)}곳\n")
        parts.append(table(["이름(지도)", "지역", "유형", "맥주 가격", "구글", "맥주"],
                           [[name_cell(i), area_name(areas, i["area"]), kind_label(i),
                             f"€{i['beer_price_eur']:.2f}", rating(i), ", ".join(i.get("beers") or [])] for i in priced]))
    for aid in AREAS:
        rows = by_rating([i for i in beer if i["area"] == aid])
        if not rows:
            continue
        parts.append(f"\n## {area_name(areas, aid)} — {len(rows)}곳\n")
        parts.append(table(["이름(지도)", "유형", "맥주", "맥주 가격", "구글", "결제", "특징", "한 줄 소개"],
                           [[name_cell(i), kind_label(i),
                             ", ".join(i.get("beers") or []) or ", ".join(L["drink"].get(d, d) for d in i.get("drinks") or []),
                             f"€{i['beer_price_eur']:.2f}" if i.get("beer_price_eur") else "–", rating(i),
                             "현금만" if i.get("payment") == "cash-only" else "",
                             ", ".join(L["feature"].get(f, f) for f in i.get("features") or []), i.get("summary_ko")] for i in rows]))
    (TABLES / "beer-pubs.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    written.append("beer-pubs.md")

    # Belgian Quarter deep dive (round 7): German/Kölsch food, wine bars, bars & lounges, the rest of the quarter
    def bv_km(i):
        return (i.get("dist") or {}).get("belgisches")

    def near_bv(i, km):
        d = bv_km(i)
        return i["area"] == "belgisches-viertel" or (d is not None and d <= km)

    def bv_rows(rows):
        rows = sorted(rows, key=lambda i: (bv_km(i) if bv_km(i) is not None else 99, -(i.get("google_rating") or 0)))
        return [[name_cell(i), kind_label(i), ", ".join(L["vibe"].get(v, v) for v in i.get("vibe") or []) or "–", price(i), rating(i),
                 f"{bv_km(i):.1f} km" if bv_km(i) is not None else "–", i.get("summary_ko")] for i in rows]

    allp = food + bars
    german = [i for i in allp if near_bv(i, 1.3) and ("DE" in (i.get("cuisine_country") or []) or i["category"] in ("brauhaus", "kneipe"))]
    wine = [i for i in allp if near_bv(i, 1.3) and (i.get("style") == "wine-bar" or i["category"] == "wine-bar")]
    barl = [i for i in bars if near_bv(i, 1.0) and i not in wine and i not in german]
    rest = [i for i in food if i["area"] == "belgisches-viertel" and i not in german and i not in wine]
    hdr = ["이름(지도)", "스타일", "분위기", "가격", "구글", "브뤼셀러 플라츠에서", "한 줄 소개"]
    parts = [banner("벨기에 지구 집중 — 독일·쾰른 요리, 와인바, 바·라운지", generated),
             "\n벨기에 지구(브뤼셀러 플라츠 일대)와 걸어서 갈 만한 주변(직선 1.0–1.3 km)만 모았어요. "
             "거리는 브뤼셀러 플라츠 기준 직선거리, 기준은 다른 표와 같이 구글 ★4.2+ · 리뷰 50+입니다.\n",
             "\n> **브뤼셀러 플라츠 야간 음주 금지:** 2026-04-01부터 매일 21–06시 광장과 맞닿은 교차로에서 공공장소 음주·술 소지가 "
             "금지돼요(질서청 단속·벌금). 키오스크 맥주를 광장에서 마시는 대신 주변 바 안에서 마시세요. "
             "[쾰른시 공지](https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/28306/index.html) · "
             "[조례 PDF](https://www.stadt-koeln.de/mediaasset/content/bekanntmachungen/2026/2026.03.30_0058-01_bruesseler_platz_obv_alkoholverbot.pdf)\n"]
    for title, rows in (("독일·쾰른 요리 (브라우하우스·크나이페 포함)", german), ("와인바", wine),
                        ("바·라운지·칵테일", barl), ("그 밖의 벨기에 지구 식당·카페", rest)):
        parts.append(f"\n## {title} — {len(rows)}곳\n")
        parts.append(table(hdr, bv_rows(rows)) if rows else "_아직 기준을 넘는 곳이 없어요._")
    (TABLES / "belgisches-viertel.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    written.append("belgisches-viertel.md")

    # near Messe / near Dom
    for anchor, title, limit_km, fname in (("messe", "쾰른 메쎄 근처 (가까운 순)", 2.0, "near-messe.md"),
                                           ("dom", "대성당 근처 (가까운 순)", 1.0, "near-dom.md")):
        fnb = food + bars
        with_d = [i for i in fnb if (i.get("dist") or {}).get(anchor) is not None]
        parts = [banner(title, generated)]
        if with_d:
            rows = sorted([i for i in with_d if i["dist"][anchor] <= limit_km], key=lambda i: i["dist"][anchor])
            parts.append(f"\n직선거리 {limit_km:.0f}km 이내 {len(rows)}곳. 도보 시간은 우회 1.3배·시속 4.8km로 어림한 값.\n")
            parts.append(table(["이름(지도)", "유형", "음식", "가격", "구글", "거리", "도보"],
                               [[name_cell(i), kind_label(i), i.get("cuisine"), price(i), rating(i),
                                 f"{i['dist'][anchor]:.2f}km", f"{walk_minutes(i['dist'][anchor])}분"] for i in rows]))
        else:
            area_id = "deutz-messe" if anchor == "messe" else "dom-altstadt"
            rows = [i for i in fnb if i["area"] == area_id]
            parts.append(f"\n아직 좌표가 없어 거리순 정렬을 못 했습니다(`python3 scripts/geocode.py` 실행 필요). "
                         f"우선 '{area_name(areas, area_id)}' 지역 목록을 평점순으로 보여줍니다.\n")
            parts.append(table(["이름(지도)", "유형", "음식", "가격", "구글"],
                               [[name_cell(i), kind_label(i), i.get("cuisine"), price(i), rating(i)]
                                for i in rows]))
        (TABLES / fname).write_text("\n".join(parts) + "\n", encoding="utf-8")
        written.append(fname)

    # candidates
    cands = (load_json(DATA / "candidates.json", {}) or {}).get("items", [])
    parts = [banner("후보 (검증 필요·기준 미달)", generated),
             "\n구글 수치를 확인하지 못했거나 기준(4.2+/50+)에 못 미친 곳. "
             "`scripts/verify_google_places.py`로 재검증하거나 직접 확인 후 `data/*.json`에 옮기세요.\n"]
    parts.append(table(["이름", "지역", "사유", "확인된 정보"],
                       [[c.get("name"), area_name(areas, c.get("area")), c.get("reason"), c.get("found")] for c in cands]))
    (TABLES / "candidates.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    written.append("candidates.md")
    return written


def status_text(i: dict) -> str:
    s = i.get("status") or "open"
    label = {"open": "운영", "closed-renovation": "휴관(공사)", "temporary-location": "임시 장소",
             "seasonal": "시즌"}.get(s, s)
    season = i.get("season") or {}
    if season.get("start"):
        label += f" {season['start'][5:]}~{(season.get('end') or '')[5:]}"
    return label


def viewer_payload(data: dict, areas_doc: dict, generated: str) -> dict:
    return {
        "generated": generated,
        "criteria": {"min_google_rating": MIN_RATING, "min_google_reviews": MIN_REVIEWS},
        "anchors": areas_doc.get("anchors", []),
        "areas": areas_doc.get("areas", []),
        "labels": {k: {str(kk): vv for kk, vv in v.items()} for k, v in L.items()},
        "restaurants": data["restaurants"],
        "bars": data["bars"],
        "shops": data["shops"],
        "attractions": data["attractions"],
        "wine": load_json(DATA / "wine.json", None),
        "routes": load_json(DATA / "routes.json", None),
    }


def render_viewer(payload: dict, mode: str) -> str:
    """mode 'site' -> full HTML document loading data.js; 'protected' -> same, but the data is the encrypted
    data.enc.js behind a password screen; 'artifact' -> fragment with inline data."""
    tpl = TEMPLATE.read_text(encoding="utf-8")
    head, body = tpl.split("<!--BODY-->", 1)
    head = head.replace("<!--HEAD-->", "")
    site = mode in ("site", "protected")
    config = json.dumps({"geolocation": site, "downloads": site, "tiles": site})
    data_js = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    if site:
        src = "data.enc.js" if mode == "protected" else "data.js"
        body = body.replace("<!--DATA-->", f'<script>window.KOLN_CONFIG={config};</script>\n<script src="{src}"></script>')
        attrs = ""
        extra = ('<link rel="stylesheet" href="vendor/leaflet/leaflet.css">\n'  # real map (tiles) on the website only
                 '<script src="vendor/leaflet/leaflet.js"></script>\n')
        if mode == "protected":  # start locked so nothing flashes before the script runs; keep it out of search engines
            body = body.replace('<div class="gate" id="gate" hidden>', '<div class="gate" id="gate">', 1)
            attrs, extra = ' class="locked"', '<meta name="robots" content="noindex, nofollow">\n' + extra
        return ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                f"{extra}{head.strip()}\n</head>\n<body{attrs}>\n{body.strip()}\n</body>\n</html>\n")
    body = body.replace("<!--DATA-->", f"<script>window.KOLN_CONFIG={config};window.KOLN_GUIDE={data_js};</script>")
    return f"{head.strip()}\n{body.strip()}\n"


def encrypt_site(payload: dict, site: dict, password: str) -> str:
    """Guide data + route files -> gzip -> AES-256-GCM (key = PBKDF2-SHA256(password, salt)) -> data.enc.js text."""
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM  # pip install cryptography (only for this step)

    files = {f"routes/{f.name}": f.read_text(encoding="utf-8")
             for f in sorted((ROOT / "routes").glob("*")) if f.suffix in (".kml", ".gpx")}
    plain = json.dumps({"guide": payload, "files": files}, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    salt = base64.b64decode(site["salt"])
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, int(site["iterations"]), dklen=32)
    iv = os.urandom(12)
    ct = AESGCM(key).encrypt(iv, gzip.compress(plain, mtime=0), None)  # ciphertext || 16-byte tag, as WebCrypto expects
    enc = {"v": 1, "kdf": "PBKDF2-SHA256", "iter": int(site["iterations"]), "salt": site["salt"],
           "iv": base64.b64encode(iv).decode(), "ct": base64.b64encode(ct).decode()}
    return "window.KOLN_ENC = " + json.dumps(enc) + ";\n"


VENDOR = ROOT / "scripts" / "vendor"


def copy_vendor() -> None:
    """Map library (Leaflet, BSD-2-Clause) served from docs/vendor so the site does not depend on a CDN."""
    for f in VENDOR.rglob("*"):
        if f.is_file():
            dst = DOCS / "vendor" / f.relative_to(VENDOR)
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(f.read_bytes())


def write_site(payload: dict) -> str:
    """docs/ for GitHub Pages. With data/site.json password_protected, only ciphertext is written."""
    site = load_json(DATA / "site.json", {}) or {}
    DOCS.mkdir(exist_ok=True)
    copy_vendor()
    if not site.get("password_protected"):
        (DOCS / "data.js").write_text("window.KOLN_GUIDE = " + json.dumps(payload, ensure_ascii=False, indent=1) + ";\n",
                                      encoding="utf-8")
        routes_dir = ROOT / "routes"
        if routes_dir.exists():  # serve the route files next to the GitHub Pages viewer
            (DOCS / "routes").mkdir(exist_ok=True)
            for f in routes_dir.glob("*.*"):
                (DOCS / "routes" / f.name).write_bytes(f.read_bytes())
        (DOCS / "index.html").write_text(render_viewer(payload, "site"), encoding="utf-8")
        return "docs/ written (open)"
    env = site.get("password_env", "KOLN_GUIDE_PASSWORD")
    password = os.environ.get(env, "")
    if not password:
        return f"docs/ NOT rebuilt: the site is password-protected — run with {env}=<password> to rebuild it"
    (DOCS / "data.enc.js").write_text(encrypt_site(payload, site, password), encoding="utf-8")
    (DOCS / "index.html").write_text(render_viewer(payload, "protected"), encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    (DOCS / "data.js").unlink(missing_ok=True)  # never leave readable copies next to the encrypted site
    shutil.rmtree(DOCS / "routes", ignore_errors=True)
    return "docs/ written (encrypted, password required)"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--artifact", help="also write a single self-contained page to this path")
    args = ap.parse_args()

    generated = dt.date.today().isoformat()
    areas_doc = load_json(DATA / "areas.json", {}) or {}
    areas = {a["id"]: a for a in areas_doc.get("areas", [])}
    anchors = areas_doc.get("anchors", [])

    data = load_all()
    for kind in ("restaurants", "bars", "shops"):
        data[kind] = [i for i in data[kind] if meets_criteria(i) and i.get("business_status") != "CLOSED_PERMANENTLY"]
    for kind, items in data.items():
        for it in items:
            if it.get("lat") is not None:
                it["dist"] = {a["id"]: round(haversine_km(a["lat"], a["lng"], it["lat"], it["lng"]), 2) for a in anchors}

    written = write_tables(data, areas, generated)
    payload = viewer_payload(data, areas_doc, generated)
    site_msg = "docs/ skipped (no template)"
    if TEMPLATE.exists():
        site_msg = write_site(payload)
        if args.artifact:
            with open(args.artifact, "w", encoding="utf-8") as f:
                f.write(render_viewer(payload, "artifact"))

    counts = {k: len(v) for k, v in data.items()}
    with_coords = sum(1 for v in data.values() for i in v if i.get("lat") is not None)
    print(f"built: {counts}; with coordinates: {with_coords}")
    print("tables:", ", ".join(written))
    print(site_msg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
