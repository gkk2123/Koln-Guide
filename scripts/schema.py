"""Shared vocabulary, labels and helpers for the Köln Guide data pipeline (schema v2).

Mirrors data/SCHEMA.md. Keep the two in sync when adding a value.
v1 research files (tags, cuisine_group) are migrated by `migrate_v1()`.
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
    "nippes", "suelz-lindenthal", "muelheim-kalk",
    "other", "day-trip",
]

FOOD_CATEGORIES = ["restaurant", "fine-dining", "brauhaus", "streetfood", "cafe", "bakery", "dessert"]
BAR_CATEGORIES = ["cocktail-bar", "wine-bar", "beer-bar", "kneipe", "bar"]
SHOP_CATEGORIES = ["wine-shop"]
FNB_CATEGORIES = FOOD_CATEGORIES + BAR_CATEGORIES + SHOP_CATEGORIES

REGIONS = {  # id -> Korean label, in display order
    "east-asia": "동아시아", "southeast-asia": "동남아시아", "south-asia": "남아시아",
    "middle-east": "중동·터키·북아프리카", "southern-europe": "남유럽", "western-europe": "서유럽",
    "central-europe": "독일·중부유럽", "eastern-europe": "동유럽·코카서스", "americas": "아메리카",
    "africa": "아프리카", "international": "퓨전·인터내셔널",
}

COUNTRIES = {  # code -> (Korean label, region)
    "KR": ("한국", "east-asia"), "JP": ("일본", "east-asia"), "CN": ("중국", "east-asia"),
    "TW": ("대만", "east-asia"), "HK": ("홍콩", "east-asia"), "MN": ("몽골", "east-asia"),
    "VN": ("베트남", "southeast-asia"), "TH": ("태국", "southeast-asia"), "ID": ("인도네시아", "southeast-asia"),
    "MY": ("말레이시아", "southeast-asia"), "MM": ("미얀마", "southeast-asia"), "PH": ("필리핀", "southeast-asia"),
    "SG": ("싱가포르", "southeast-asia"), "KH": ("캄보디아", "southeast-asia"), "LA": ("라오스", "southeast-asia"),
    "IN": ("인도", "south-asia"), "NP": ("네팔", "south-asia"), "LK": ("스리랑카", "south-asia"),
    "PK": ("파키스탄", "south-asia"), "BD": ("방글라데시", "south-asia"),
    "TR": ("터키", "middle-east"), "LB": ("레바논", "middle-east"), "SY": ("시리아", "middle-east"),
    "IL": ("이스라엘", "middle-east"), "PS": ("팔레스타인", "middle-east"), "JO": ("요르단", "middle-east"),
    "IR": ("이란", "middle-east"), "IQ": ("이라크", "middle-east"), "AF": ("아프가니스탄", "middle-east"),
    "MA": ("모로코", "middle-east"), "TN": ("튀니지", "middle-east"), "EG": ("이집트", "middle-east"),
    "IT": ("이탈리아", "southern-europe"), "ES": ("스페인", "southern-europe"), "PT": ("포르투갈", "southern-europe"),
    "GR": ("그리스", "southern-europe"), "HR": ("크로아티아", "southern-europe"),
    "FR": ("프랑스", "western-europe"), "BE": ("벨기에", "western-europe"), "NL": ("네덜란드", "western-europe"),
    "GB": ("영국", "western-europe"), "IE": ("아일랜드", "western-europe"),
    "DE": ("독일", "central-europe"), "AT": ("오스트리아", "central-europe"), "CH": ("스위스", "central-europe"),
    "PL": ("폴란드", "central-europe"), "CZ": ("체코", "central-europe"), "HU": ("헝가리", "central-europe"),
    "GE": ("조지아", "eastern-europe"), "UA": ("우크라이나", "eastern-europe"), "RU": ("러시아", "eastern-europe"),
    "AM": ("아르메니아", "eastern-europe"),
    "US": ("미국", "americas"), "MX": ("멕시코", "americas"), "PE": ("페루", "americas"),
    "AR": ("아르헨티나", "americas"), "BR": ("브라질", "americas"), "CU": ("쿠바", "americas"),
    "CO": ("콜롬비아", "americas"), "VE": ("베네수엘라", "americas"),
    "ET": ("에티오피아", "africa"), "ER": ("에리트레아", "africa"), "ZA": ("남아공", "africa"),
    "NG": ("나이지리아", "africa"), "SN": ("세네갈", "africa"), "GH": ("가나", "africa"),
    "INT": ("퓨전·인터내셔널", "international"),
}

DISHES = {
    "pizza": "피자", "pasta": "파스타", "ramen": "라멘", "sushi": "스시", "noodles": "면 요리",
    "dumplings": "만두·딤섬", "korean-bbq": "고기구이", "hotpot": "훠궈·전골", "fried-chicken": "치킨",
    "curry": "커리", "pho": "쌀국수", "banh-mi": "반미", "kebab": "케밥·되너", "falafel": "팔라펠",
    "mezze": "메제", "grill": "그릴·숯불구이", "burger": "버거", "steak": "스테이크", "seafood": "해산물",
    "tapas": "타파스·작은 접시", "tacos": "타코", "schnitzel": "슈니첼", "rhineland-classics": "쾰른 향토 요리",
    "flammkuchen": "플람쿠헨", "tasting-menu": "코스 요리", "bowls": "볼·샐러드", "sandwiches": "샌드위치",
    "brunch-plates": "브런치", "bread-pastry": "빵·페이스트리", "cake": "케이크", "ice-cream": "아이스크림",
    "coffee": "커피",
}
DIET = {"vegan": "비건", "vegetarian": "채식", "halal": "할랄", "gluten-free": "글루텐프리"}
MEALS = {"breakfast": "아침", "brunch": "브런치", "lunch": "점심", "dinner": "저녁", "late-night": "심야"}
OCCASIONS = {"date": "데이트", "business": "비즈니스", "group": "단체", "solo": "혼밥·혼술", "family": "가족·아이",
             "quick": "빠른 한 끼"}
FEATURES = {"dom-view": "대성당 뷰", "rhine-view": "라인강 뷰", "terrace": "테라스", "rooftop": "루프탑",
            "beer-garden": "비어가든", "live-music": "라이브 음악", "open-sunday": "일요일 영업", "takeaway": "포장"}
DRINKS = {"koelsch": "쾰시", "craft-beer": "크래프트 맥주", "cocktails": "칵테일", "wine-list": "와인 리스트",
          "natural-wine": "내추럴 와인", "german-wine": "독일 와인", "specialty-coffee": "스페셜티 커피", "tea": "차"}
VIBE = {"local-favorite": "현지인 단골", "touristy": "관광객 많음", "trendy": "트렌디", "traditional": "전통",
        "hidden-gem": "숨은 맛집", "lively": "활기찬", "quiet": "조용한"}
RESERVATION = {"required": "예약 필수", "recommended": "예약 권장", "walk-in": "워크인", "unknown": "확인 필요"}
PAYMENT = {"card": "카드 가능", "cash-only": "현금만", "unknown": "확인 필요"}
AWARD_FLAGS = {"michelin-star": "미쉐린 스타", "bib-gourmand": "빕 구르망", "michelin-guide": "미쉐린 셀렉티드",
               "other-award": "기타 수상·선정"}

FACETS = {  # v2 multi-value facets on places
    "dishes": DISHES, "diet": DIET, "meals": MEALS, "occasions": OCCASIONS,
    "features": FEATURES, "drinks": DRINKS, "vibe": VIBE,
}

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

# Neighbourhoods added in round 8; places filed as "other" move here by postcode.
AREA_BY_POSTCODE = {
    "50733": "nippes", "50735": "nippes",
    "50931": "suelz-lindenthal", "50935": "suelz-lindenthal", "50937": "suelz-lindenthal", "50939": "suelz-lindenthal",
    "51063": "muelheim-kalk", "51065": "muelheim-kalk", "51103": "muelheim-kalk", "51105": "muelheim-kalk",
}


def refine_area(area: str | None, address: str | None) -> str | None:
    if area not in (None, "", "other"):
        return area
    m = re.search(r"\b(5\d{4})\b", address or "")
    return AREA_BY_POSTCODE.get(m.group(1), area) if m else area


# What kind of place it is (format), separate from cuisine/nationality: shown as "인도네시아 · 비스트로 · €€".
STYLES = {
    "fine-dining": "파인다이닝", "bistro": "비스트로", "brasserie": "브라세리", "trattoria": "트라토리아",
    "pizzeria": "피자리아", "izakaya": "이자카야", "tapas": "타파스·셰어링", "mezze": "메제(소량 전채)",
    "wine-bar": "와인바", "cocktail-bar": "칵테일바", "brauhaus": "브라우하우스", "kneipe": "동네 펍",
    "beer-bar": "맥주바", "steakhouse": "스테이크하우스", "burger": "버거", "ramen-bar": "라멘집", "sushi-bar": "스시",
    "noodle-bar": "면 요리집", "pasta-bar": "파스타 바", "kebab": "케밥·되너", "grill": "그릴·고기구이", "chicken": "치킨",
    "buffet": "뷔페", "gasthaus": "가스트하우스(향토 식당)", "cantina": "칸티나(멕시칸 바)", "streetfood": "스트리트 푸드·임비스", "brunch": "아침·브런치 카페",
    "home-cooking": "가정식", "casual": "캐주얼 식당", "curry-house": "커리 하우스", "sharing": "셰어 플래터",
    "asian-kitchen": "아시안 키친", "veggie": "채식·비건", "modern": "모던 다이닝", "ristorante": "리스토란테",
    "traditional": "정통 식당", "hotel-restaurant": "호텔 레스토랑",
    "lounge": "라운지", "cafe": "카페", "bakery": "베이커리", "ice-cream": "젤라토·아이스크림", "dessert": "디저트", "bar": "바",
}
STYLE_RULES = [  # first match wins; matched against the English/German cuisine text and the name
    ("izakaya", r"izakaya"),
    ("tapas", r"\btapas\b|sharing plates?|small plates?"),
    ("mezze", r"\bmezz?e\b"),
    ("wine-bar", r"wine ?bar|weinbar|weinstube|vinothek|enoteca"),
    ("bistro", r"bistro"),
    ("brasserie", r"brasserie"),
    ("trattoria", r"trattoria|osteria"),
    ("pizzeria", r"pizz"),
    ("burger", r"burger"),
    ("ramen-bar", r"ramen"),
    ("sushi-bar", r"sushi|omakase"),
    ("steakhouse", r"steak|churrasc|asado|parrilla"),
    ("kebab", r"kebab|kebap|döner|doner|dürüm|durum"),
    ("noodle-bar", r"noodle (shop|bar|house)|nudel(bar|haus)|biang|pho specialist"),
    ("pasta-bar", r"pasta ?bar"),
    ("kneipe", r"kneipe"),
    ("gasthaus", r"gasthaus|wirtshaus|gaststätte"),
    ("cantina", r"cantina"),
    ("chicken", r"^korean fried chicken|fried chicken (shop|bar)"),
    ("grill", r"\bbbq\b|barbecue|grill"),
    ("buffet", r"buffet|all-you-can-eat"),
    ("streetfood", r"street ?food|imbiss"),
    ("ice-cream", r"ice cream|gelato|gelateria|eiscaf"),
    ("bakery", r"bakery|bäckerei|backhaus|patisserie|pâtisserie"),
    ("brunch", r"brunch|breakfast|frühstück"),
    ("lounge", r"lounge"),
    ("hotel-restaurant", r"hotel restaurant"),
    ("modern", r"market cuisine|marktküche|modern european"),
    ("veggie", r"^vegan|vegetarian & vegan|100% vegan|vegetarian restaurant"),
    ("home-cooking", r"home cooking|home-style|hausmannskost"),
    ("casual", r"comfort food"),
    ("asian-kitchen", r"pan-asian"),
    ("curry-house", r"curr(y|ies)"),
    ("sharing", r"ethiopian|eritrean"),
    ("traditional", r"^traditional"),
]
DISH_STYLE = [("mezze", "mezze"), ("grill", "grill"), ("pho", "noodle-bar")]  # last resort: the signature dish
CATEGORY_STYLE = {"fine-dining": "fine-dining", "cocktail-bar": "cocktail-bar", "wine-bar": "wine-bar",
                  "brauhaus": "brauhaus", "kneipe": "kneipe", "beer-bar": "beer-bar"}
FALLBACK_STYLE = {"cafe": "cafe", "bakery": "bakery", "dessert": "dessert", "streetfood": "streetfood", "bar": "bar"}


def infer_style(it: dict) -> str | None:
    """Format of a food/drink place from its category and description; None = plain restaurant."""
    cat = it.get("category")
    text = f"{it.get('cuisine') or ''} {it.get('name') or ''}".lower()
    if cat in ("cocktail-bar", "bar") and re.search(r"lounge|hotel bar", text):
        return "lounge"
    if cat in CATEGORY_STYLE:
        return CATEGORY_STYLE[cat]
    allowed = {"cafe": ("bistro", "brunch", "bakery", "ice-cream"), "bakery": (), "dessert": ("ice-cream",)}.get(cat)
    for style, rx in STYLE_RULES:
        if (allowed is None or style in allowed) and re.search(rx, text):
            return style
    if cat == "restaurant":
        for dish, style in DISH_STYLE:
            if dish in (it.get("dishes") or []):
                return style
    return FALLBACK_STYLE.get(cat)


LABELS_KO = {
    "category": {
        "restaurant": "레스토랑", "fine-dining": "파인다이닝", "brauhaus": "브라우하우스", "streetfood": "간편식·임비스",
        "cafe": "카페", "bakery": "베이커리", "dessert": "디저트", "cocktail-bar": "칵테일바",
        "wine-bar": "와인바", "beer-bar": "맥주바", "kneipe": "동네 펍(크나이페)", "bar": "바·펍", "wine-shop": "와인숍",
        "landmark": "랜드마크", "church": "성당·교회", "museum": "박물관·미술관",
        "viewpoint": "전망·포토스팟", "park-nature": "공원·자연", "experience-tour": "체험·투어",
        "shopping": "쇼핑", "market-event": "시즌 이벤트·마켓", "nightlife-area": "나이트라이프 지역",
        "day-trip": "근교 당일치기",
    },
    "region": REGIONS,
    "country": {k: v[0] for k, v in COUNTRIES.items()},
    "dish": DISHES, "diet": DIET, "meal": MEALS, "occasion": OCCASIONS, "feature": FEATURES,
    "drink": DRINKS, "vibe": VIBE, "reservation": RESERVATION, "payment": PAYMENT, "award": AWARD_FLAGS,
    "price_level": {1: "€", 2: "€€", 3: "€€€", 4: "€€€€"},
    "style": STYLES,
    "tag": {
        "unesco": "유네스코", "free": "무료", "indoor": "실내", "rainy-day": "비 오는 날", "kid-friendly": "아이 동반",
        "photo-spot": "포토스팟", "night-view": "야경", "must-see": "필수", "christmas": "크리스마스",
        "karneval": "카니발", "dom-view": "대성당 뷰", "romanesque": "로마네스크", "roman": "로마 유적",
        "art": "미술", "history": "역사", "chocolate": "초콜릿", "river": "강", "nature": "자연",
    },
}

# ------------------------------------------------------------------ v1 -> v2 migration
V1_TAGS = {
    "dom-view": ("features", "dom-view"), "rhine-view": ("features", "rhine-view"),
    "terrace": ("features", "terrace"), "rooftop": ("features", "rooftop"),
    "beer-garden": ("features", "beer-garden"), "open-sunday": ("features", "open-sunday"),
    "takeaway": ("features", "takeaway"), "late-night": ("meals", "late-night"),
    "breakfast": ("meals", "breakfast"), "brunch": ("meals", "brunch"), "lunch-deal": ("meals", "lunch"),
    "vegan-friendly": ("diet", "vegan"), "vegetarian-friendly": ("diet", "vegetarian"),
    "group-friendly": ("occasions", "group"), "solo-friendly": ("occasions", "solo"),
    "date-night": ("occasions", "date"), "business-dinner": ("occasions", "business"),
    "kid-friendly": ("occasions", "family"), "local-favorite": ("vibe", "local-favorite"),
    "touristy": ("vibe", "touristy"), "koelsch": ("drinks", "koelsch"), "craft-beer": ("drinks", "craft-beer"),
    "natural-wine": ("drinks", "natural-wine"), "german-wine": ("drinks", "german-wine"),
    "reservation-recommended": ("reservation", "recommended"), "walk-in": ("reservation", "walk-in"),
    "cash-only": ("payment", "cash-only"), "near-messe": ("location", "near-messe"),
    "near-hbf": ("location", "near-hbf"), "michelin-star": ("award", "michelin-star"),
    "bib-gourmand": ("award", "bib-gourmand"),
}
V1_CUISINE_GROUP = {  # -> (countries, region, dishes, diet)
    "german": (["DE"], None, [], []), "italian": (["IT"], None, [], []), "french": (["FR"], None, [], []),
    "mediterranean": ([], "southern-europe", [], []), "spanish-portuguese": (["ES"], None, [], []),
    "greek": (["GR"], None, [], []), "turkish": (["TR"], None, [], []),
    "middle-eastern": ([], "middle-east", [], []), "indian-south-asian": ([], "south-asia", [], []),
    "japanese": (["JP"], None, [], []), "korean": (["KR"], None, [], []), "chinese": (["CN"], None, [], []),
    "vietnamese": (["VN"], None, [], []), "thai-southeast-asian": ([], "southeast-asia", [], []),
    "asian-fusion": (["INT"], None, [], []), "american-burger": (["US"], None, ["burger"], []),
    "latin-american": ([], "americas", [], []), "african": ([], "africa", [], []),
    "modern-european": (["INT"], None, [], []), "vegan-vegetarian": ([], None, [], ["vegan"]),
    "seafood": ([], None, ["seafood"], []), "steak-grill": ([], None, ["steak"], []),
    "cafe-bakery": ([], None, ["coffee"], []), "dessert-icecream": ([], None, ["cake"], []),
    "international": (["INT"], None, [], []), "bar-drinks": ([], None, [], []),
}
COUNTRY_KEYWORDS = [  # checked in order against the English `cuisine` text
    ("south african", "ZA"), ("korean", "KR"), ("japan", "JP"), ("sushi", "JP"), ("ramen", "JP"),
    ("izakaya", "JP"), ("taiwan", "TW"), ("sichuan", "CN"), ("szechuan", "CN"), ("cantonese", "CN"),
    ("chinese", "CN"), ("mongolian", "MN"), ("vietnam", "VN"), ("thai", "TH"), ("indonesia", "ID"),
    ("balinese", "ID"), ("burmese", "MM"), ("myanmar", "MM"), ("malaysia", "MY"), ("filipino", "PH"),
    ("nepal", "NP"), ("sri lank", "LK"), ("pakistan", "PK"), ("indian", "IN"), ("turkish", "TR"),
    ("kebab", "TR"), ("kebap", "TR"), ("döner", "TR"), ("tantuni", "TR"), ("kumpir", "TR"), ("lahmacun", "TR"),
    ("leban", "LB"), ("syria", "SY"), ("palestin", "PS"), ("israel", "IL"), ("persian", "IR"), ("iran", "IR"),
    ("afghan", "AF"), ("moroc", "MA"), ("ethiopia", "ET"), ("eritrea", "ER"), ("greek", "GR"),
    ("neapolitan", "IT"), ("sardinian", "IT"), ("italian", "IT"), ("pizza", "IT"), ("pasta", "IT"),
    ("trattoria", "IT"), ("spanish", "ES"), ("tapas", "ES"), ("portug", "PT"), ("french", "FR"),
    ("brasserie", "FR"), ("georgian", "GE"), ("austrian", "AT"), ("mexican", "MX"), ("peru", "PE"),
    ("argentin", "AR"), ("brazil", "BR"), ("cuban", "CU"), ("burger", "US"), ("american", "US"),
    ("brauhaus", "DE"), ("kölsch", "DE"), ("koelsch", "DE"), ("rhineland", "DE"), ("german", "DE"),
]
DISH_KEYWORDS = [
    ("pizza", "pizza"), ("pasta", "pasta"), ("ramen", "ramen"), ("sushi", "sushi"), ("poke", "bowls"),
    ("noodle", "noodles"), ("nudel", "noodles"), ("udon", "noodles"), ("dumpling", "dumplings"),
    ("dim sum", "dumplings"), ("gyoza", "dumplings"), ("korean bbq", "korean-bbq"), ("hot pot", "hotpot"),
    ("hotpot", "hotpot"), ("fried chicken", "fried-chicken"), ("curry", "curry"), ("pho", "pho"),
    ("banh mi", "banh-mi"), ("bánh mì", "banh-mi"), ("kebab", "kebab"), ("kebap", "kebab"), ("döner", "kebab"),
    ("dürüm", "kebab"), ("shawarma", "kebab"), ("tantuni", "kebab"), ("falafel", "falafel"), ("mezze", "mezze"),
    ("meze", "mezze"), ("grill", "grill"), ("bbq", "grill"), ("barbecue", "grill"), ("burger", "burger"),
    ("steak", "steak"), ("seafood", "seafood"), ("fish", "seafood"), ("tapas", "tapas"),
    ("small plates", "tapas"), ("taco", "tacos"), ("schnitzel", "schnitzel"), ("brauhaus", "rhineland-classics"),
    ("rhineland", "rhineland-classics"), ("flammkuchen", "flammkuchen"), ("tasting menu", "tasting-menu"),
    ("fine dining", "tasting-menu"), ("bowl", "bowls"), ("salad", "bowls"), ("sandwich", "sandwiches"),
    ("bagel", "sandwiches"), ("brunch", "brunch-plates"), ("bakery", "bread-pastry"), ("bäckerei", "bread-pastry"),
    ("croissant", "bread-pastry"), ("pastry", "bread-pastry"), ("patisserie", "cake"), ("cake", "cake"),
    ("kuchen", "cake"), ("gelato", "ice-cream"), ("ice cream", "ice-cream"), ("eiscafé", "ice-cream"),
    ("coffee", "coffee"), ("espresso", "coffee"), ("roaster", "coffee"),
]
_STAR = re.compile(r"(\bstar|stern|★|\b[12]-star|two-star|one-star)", re.I)


def award_flags(awards: list[str]) -> list[str]:
    flags = []
    for a in awards or []:
        s = str(a)
        if re.search(r"michelin", s, re.I) and _STAR.search(s) and not re.search(r"bib", s, re.I):
            f = "michelin-star"
        elif re.search(r"bib gourmand", s, re.I):
            f = "bib-gourmand"
        elif re.search(r"michelin", s, re.I):
            f = "michelin-guide"
        else:
            f = "other-award"
        if f not in flags:
            flags.append(f)
    return flags


def region_for(countries: list[str], fallback: str | None = None) -> str | None:
    for c in countries or []:
        if c in COUNTRIES:
            return COUNTRIES[c][1]
    return fallback if fallback in REGIONS else None


def infer_countries(text: str) -> list[str]:
    t = (text or "").lower()
    out = []
    for kw, code in COUNTRY_KEYWORDS:
        if kw in t and code not in out:
            out.append(code)
    return out[:2]


def infer_dishes(*texts: str) -> list[str]:
    t = " ".join(x for x in texts if x).lower()
    out = []
    for kw, dish in DISH_KEYWORDS:
        if re.search(r"(?<![a-zäöü])" + re.escape(kw), t) and dish not in out:
            out.append(dish)
    return out[:5]


# ------------------------------------------------------------------ helpers
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


def in_cologne(address: str | None, area: str | None) -> bool:
    """City-only guide: drop day trips and anything with a postcode outside Köln (50667-51149)."""
    if area == "day-trip":
        return False
    m = re.search(r"\b(\d{5})\b", address or "")
    return not m or 50667 <= int(m.group(1)) <= 51149


def is_area_wide(address: str | None) -> bool:
    """Addresses that describe a route or a whole district, not a point (e.g. a parade route)."""
    return not address or bool(re.search(r"zugweg|stadtweit|stadtgebiet|^innenstadt", address, re.I))


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
