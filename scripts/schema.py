"""Shared enums, labels and helpers for the Köln Guide data pipeline.

Mirrors data/SCHEMA.md. Keep the two in sync when adding a value.
"""
from __future__ import annotations

import json
import math
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RAW = ROOT / "research" / "raw"
GUIDES = ROOT / "guides"
DOCS = ROOT / "docs"

MIN_RATING = 4.2
MIN_REVIEWS = 50

AREAS = [
    "dom-altstadt", "belgisches-viertel", "friesenviertel-ehrenstrasse", "kwartier-lateng",
    "ehrenfeld", "suedstadt-rheinauhafen", "agnesviertel-eigelstein", "deutz-messe",
    "other", "day-trip",
]

FOOD_CATEGORIES = ["restaurant", "brauhaus", "cafe", "bakery", "dessert", "streetfood"]
BAR_CATEGORIES = ["cocktail-bar", "wine-bar", "beer-bar", "bar"]
SHOP_CATEGORIES = ["wine-shop"]
FNB_CATEGORIES = FOOD_CATEGORIES + BAR_CATEGORIES + SHOP_CATEGORIES

CUISINE_GROUPS = [
    "german", "italian", "french", "mediterranean", "spanish-portuguese", "greek", "turkish",
    "middle-eastern", "indian-south-asian", "japanese", "korean", "chinese", "vietnamese",
    "thai-southeast-asian", "asian-fusion", "american-burger", "latin-american", "african",
    "modern-european", "vegan-vegetarian", "seafood", "steak-grill", "cafe-bakery",
    "dessert-icecream", "international", "bar-drinks",
]

PLACE_TAGS = [
    "dom-view", "rhine-view", "terrace", "rooftop", "beer-garden", "late-night", "breakfast",
    "brunch", "lunch-deal", "vegan-friendly", "vegetarian-friendly", "reservation-recommended",
    "walk-in", "cash-only", "group-friendly", "solo-friendly", "date-night", "business-dinner",
    "local-favorite", "touristy", "kid-friendly", "takeaway", "koelsch", "craft-beer",
    "natural-wine", "german-wine", "michelin-star", "bib-gourmand", "near-messe", "near-hbf",
    "open-sunday",
]

ATTRACTION_CATEGORIES = [
    "landmark", "church", "museum", "viewpoint", "park-nature", "experience-tour", "shopping",
    "market-event", "nightlife-area", "day-trip",
]

ATTRACTION_TAGS = [
    "unesco", "free", "indoor", "rainy-day", "kid-friendly", "photo-spot", "night-view",
    "must-see", "christmas", "karneval", "dom-view", "romanesque", "roman", "art", "history",
    "chocolate", "river", "nature",
]

ATTRACTION_STATUS = ["open", "closed-renovation", "temporary-location", "seasonal"]
BOOKING = ["not-needed", "recommended", "required"]

LABELS_KO = {
    "category": {
        "restaurant": "레스토랑", "brauhaus": "브라우하우스", "cafe": "카페", "bakery": "베이커리",
        "dessert": "디저트", "streetfood": "길거리·간편식", "cocktail-bar": "칵테일바",
        "wine-bar": "와인바", "beer-bar": "맥주바", "bar": "바·펍", "wine-shop": "와인숍",
        "landmark": "랜드마크", "church": "성당·교회", "museum": "박물관·미술관",
        "viewpoint": "전망·포토스팟", "park-nature": "공원·자연", "experience-tour": "체험·투어",
        "shopping": "쇼핑", "market-event": "시즌 이벤트·마켓", "nightlife-area": "나이트라이프 지역",
        "day-trip": "근교 당일치기",
    },
    "cuisine_group": {
        "german": "독일", "italian": "이탈리아", "french": "프랑스", "mediterranean": "지중해",
        "spanish-portuguese": "스페인·포르투갈", "greek": "그리스", "turkish": "터키",
        "middle-eastern": "중동·레반트", "indian-south-asian": "인도·남아시아", "japanese": "일본",
        "korean": "한국", "chinese": "중국", "vietnamese": "베트남", "thai-southeast-asian": "태국·동남아",
        "asian-fusion": "아시안 퓨전", "american-burger": "미국·버거", "latin-american": "중남미",
        "african": "아프리카", "modern-european": "모던 유러피언", "vegan-vegetarian": "비건·채식",
        "seafood": "해산물", "steak-grill": "스테이크·그릴", "cafe-bakery": "카페·베이커리",
        "dessert-icecream": "디저트·아이스크림", "international": "인터내셔널", "bar-drinks": "주류 중심",
    },
    "price_level": {1: "€", 2: "€€", 3: "€€€", 4: "€€€€"},
    "tag": {
        "dom-view": "대성당 뷰", "rhine-view": "라인강 뷰", "terrace": "테라스", "rooftop": "루프탑",
        "beer-garden": "비어가든", "late-night": "늦게까지", "breakfast": "아침", "brunch": "브런치",
        "lunch-deal": "점심 메뉴", "vegan-friendly": "비건 가능", "vegetarian-friendly": "채식 가능",
        "reservation-recommended": "예약 권장", "walk-in": "워크인", "cash-only": "현금만",
        "group-friendly": "단체", "solo-friendly": "혼밥·혼술", "date-night": "데이트",
        "business-dinner": "비즈니스 디너", "local-favorite": "현지인 단골", "touristy": "관광객 많음",
        "kid-friendly": "아이 동반", "takeaway": "포장", "koelsch": "쾰시", "craft-beer": "크래프트 맥주",
        "natural-wine": "내추럴 와인", "german-wine": "독일 와인", "michelin-star": "미쉐린 스타",
        "bib-gourmand": "빕 구르망", "near-messe": "메쎄 근처", "near-hbf": "중앙역 근처",
        "open-sunday": "일요일 영업",
        "unesco": "유네스코", "free": "무료", "indoor": "실내", "rainy-day": "비 오는 날",
        "photo-spot": "포토스팟", "night-view": "야경", "must-see": "필수", "christmas": "크리스마스",
        "karneval": "카니발", "romanesque": "로마네스크", "roman": "로마 유적", "art": "미술",
        "history": "역사", "chocolate": "초콜릿", "river": "강", "nature": "자연",
    },
}


def slugify(text: str) -> str:
    text = text.replace("ß", "ss")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "item"


def norm_name(text: str) -> str:
    """Loose key for duplicate detection."""
    s = slugify(text or "")
    for junk in ("restaurant-", "cafe-", "brauhaus-", "-koeln", "-cologne", "bar-", "the-"):
        s = s.replace(junk, "")
    return s.replace("-", "")


def street_key(address: str | None) -> str:
    if not address:
        return ""
    first = address.split(",")[0]
    return slugify(first).replace("-", "")


def haversine_km(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    r = 6371.0088
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = p2 - p1
    dlmb = math.radians(lng2 - lng1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlmb / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def walk_minutes(km: float) -> int:
    """Straight-line km -> rough walking minutes (x1.3 detour, 4.8 km/h)."""
    return max(1, round(km * 1.3 / 4.8 * 60))


def meets_criteria(item: dict) -> bool:
    r, n = item.get("google_rating"), item.get("google_reviews")
    return isinstance(r, (int, float)) and isinstance(n, int) and r >= MIN_RATING and n >= MIN_REVIEWS


def load_json(path: Path, default=None):
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


DATA_FILES = {
    "restaurants": DATA / "restaurants.json",
    "bars": DATA / "bars.json",
    "shops": DATA / "shops.json",
    "attractions": DATA / "attractions.json",
}


def load_items(kind: str) -> list[dict]:
    doc = load_json(DATA_FILES[kind], {"items": []})
    return doc.get("items", [])


def load_all() -> dict[str, list[dict]]:
    return {kind: load_items(kind) for kind in DATA_FILES}
