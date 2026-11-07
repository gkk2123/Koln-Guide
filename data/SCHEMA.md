# 데이터 스키마 v2 (Data Schema)

모든 데이터 파일은 UTF-8 JSON입니다. `research/raw/*.json`(조사 원자료)을 `scripts/import_raw.py`가 합쳐서
`data/*.json`(정제본)을 만들고, `scripts/build.py`가 그걸로 `guides/tables/`의 표와 `docs/`의 웹 뷰어를 생성합니다.
v1 원자료(`tags`, `cuisine_group`)는 import 단계에서 v2 필드로 자동 변환됩니다.

## 선정 기준 (식음료)

| 항목 | 기준 |
|---|---|
| 구글 평점 | `google_rating >= 4.2` |
| 구글 리뷰 수 | `google_reviews >= 50` |
| 영업 상태 | 조사 시점(2026-11)에 폐업 신호 없음 |
| 근거 | 평점·리뷰 수는 반드시 출처(`rating_source`)와 함께. 추정치·기억에 의존한 숫자 금지. 출처 귀속이 애매하면 `confidence: "low"` → 후보로 분류 |

## 분류 체계 (v2)

v1은 `cuisine_group` 하나에 나라(이탈리아)와 스타일(비건·해산물·카페)이 섞여 있었습니다. v2는 축을 나눕니다.

| 축 | 필드 | 질문 | 값 |
|---|---|---|---|
| 유형 | `category` | 어떤 가게? | 아래 표 |
| 나라 | `cuisine_country` | 어느 나라 음식? (배열, 대표 먼저) | ISO 국가 코드 + `INT` |
| 문화권 | `cuisine_region` | 어느 문화권? | 국가 코드에서 자동 계산 (직접 써도 됨) |
| 요리 | `dishes` | 무슨 요리? | 아래 목록 |
| 식단 | `diet` | 식단 제약 대응 | `vegan` `vegetarian` `halal` `gluten-free` |
| 시간대 | `meals` | 언제 가나? | `breakfast` `brunch` `lunch` `dinner` `late-night` |
| 상황 | `occasions` | 누구와/왜? | `date` `business` `group` `solo` `family` `quick` |
| 특징 | `features` | 공간·서비스 | `dom-view` `rhine-view` `terrace` `rooftop` `beer-garden` `live-music` `open-sunday` `takeaway` |
| 음료 | `drinks` | 마실 것 | `koelsch` `craft-beer` `cocktails` `wine-list` `natural-wine` `german-wine` `specialty-coffee` `tea` |
| 분위기 | `vibe` | 어떤 느낌? | `local-favorite` `touristy` `trendy` `traditional` `hidden-gem` `lively` `quiet` |
| 예약 | `reservation` | | `required` `recommended` `walk-in` `unknown` |
| 결제 | `payment` | | `card` `cash-only` `unknown` |
| 가격 | `price_level`, `price_pp` | 1인 음식값 | 1–4, `{"min": 15, "max": 25}` (EUR, 선택) |

### `category` — 가게 유형

`restaurant`(레스토랑) · `fine-dining`(파인다이닝·코스) · `brauhaus`(쾰시 맥주홀·양조장 직영) · `streetfood`(간편식·임비스) ·
`cafe` · `bakery` · `dessert` · `cocktail-bar` · `wine-bar` · `beer-bar`(크래프트·수입 맥주 바) · `kneipe`(쾰시를 파는 동네 펍, 양조장 직영 아님) · `bar` · `wine-shop`

**쾰른 시내만** 다룹니다. 우편번호 50667–51149 밖이거나 `area: day-trip`인 항목은 import 때 빠집니다.

### `cuisine_country` — 나라 코드

ISO 3166-1 alpha-2를 씁니다. 하나로 정할 수 없는 퓨전·모던 유러피언은 `INT`.

| 문화권 `cuisine_region` | 코드 |
|---|---|
| `east-asia` 동아시아 | KR 한국 · JP 일본 · CN 중국 · TW 대만 · HK 홍콩 · MN 몽골 |
| `southeast-asia` 동남아시아 | VN 베트남 · TH 태국 · ID 인도네시아 · MY 말레이시아 · MM 미얀마 · PH 필리핀 · SG 싱가포르 · KH 캄보디아 · LA 라오스 |
| `south-asia` 남아시아 | IN 인도 · NP 네팔 · LK 스리랑카 · PK 파키스탄 · BD 방글라데시 |
| `middle-east` 중동·터키·북아프리카 | TR 터키 · LB 레바논 · SY 시리아 · IL 이스라엘 · PS 팔레스타인 · JO 요르단 · IR 이란 · IQ 이라크 · AF 아프가니스탄 · MA 모로코 · TN 튀니지 · EG 이집트 |
| `southern-europe` 남유럽 | IT 이탈리아 · ES 스페인 · PT 포르투갈 · GR 그리스 · HR 크로아티아 |
| `western-europe` 서유럽 | FR 프랑스 · BE 벨기에 · NL 네덜란드 · GB 영국 · IE 아일랜드 |
| `central-europe` 독일·중부유럽 | DE 독일 · AT 오스트리아 · CH 스위스 · PL 폴란드 · CZ 체코 · HU 헝가리 |
| `eastern-europe` 동유럽·코카서스 | GE 조지아 · UA 우크라이나 · RU 러시아 · AM 아르메니아 |
| `americas` 아메리카 | US 미국 · MX 멕시코 · PE 페루 · AR 아르헨티나 · BR 브라질 · CU 쿠바 · CO 콜롬비아 · VE 베네수엘라 |
| `africa` 아프리카 | ET 에티오피아 · ER 에리트레아 · ZA 남아공 · NG 나이지리아 · SN 세네갈 · GH 가나 |
| `international` 퓨전·인터내셔널 | INT |

카페·바·와인숍처럼 특정 나라 음식이 아닌 곳은 `cuisine_country`를 비워 둡니다.

### `dishes` — 요리 종류

`pizza` 피자 · `pasta` 파스타 · `ramen` 라멘 · `sushi` 스시 · `noodles` 면 요리 · `dumplings` 만두·딤섬 ·
`korean-bbq` 고기구이 · `hotpot` 훠궈·전골 · `fried-chicken` 치킨 · `curry` 커리 · `pho` 쌀국수 · `banh-mi` 반미 ·
`kebab` 케밥·되너 · `falafel` 팔라펠 · `mezze` 메제(중동식 소량 요리) · `grill` 그릴·숯불구이 · `burger` 버거 ·
`steak` 스테이크 · `seafood` 해산물 · `tapas` 타파스·작은 접시 · `tacos` 타코 · `schnitzel` 슈니첼 ·
`rhineland-classics` 쾰른 향토 요리 · `flammkuchen` 플람쿠헨 · `tasting-menu` 코스 요리 · `bowls` 볼·샐러드 ·
`sandwiches` 샌드위치 · `brunch-plates` 브런치 · `bread-pastry` 빵·페이스트리 · `cake` 케이크 · `ice-cream` 아이스크림 · `coffee` 커피

### `price_level` — 1인 음식값(음료 제외)

| 값 | 표기 | 1인 |
|---|---|---|
| 1 | € | ~€15 |
| 2 | €€ | €15–30 |
| 3 | €€€ | €30–60 |
| 4 | €€€€ | €60 이상 |

바는 칵테일 1잔 기준: 1 = €10 미만, 2 = €10–14, 3 = €15–19, 4 = €20 이상. `price_note`에 실제 가격을 적습니다.

### `area` — 지역

| id | 한국어 | 범위 |
|---|---|---|
| `dom-altstadt` | 대성당·구시가 | 쾰른 대성당, 중앙역(Hbf), 구시가(Alter Markt·Heumarkt·Fischmarkt·Martinsviertel·라인강변), Hohe Straße·Schildergasse~Neumarkt |
| `belgisches-viertel` | 벨기에 지구 | Hohenzollernring/Habsburgerring 서쪽~Stadtgarten·Aachener Weiher: Brüsseler Platz, Aachener Str.(초입), Antwerpener·Brabanter·Maastrichter·Lütticher·Flandrische Str., Bismarckstr., Venloer Str.(Bahnhof West까지) |
| `friesenviertel-ehrenstrasse` | 프리젠 지구·에렌슈트라세 | Friesenplatz, Friesenstr., Ehrenstraße, Apostelnviertel, Rudolfplatz/Hahnentor, Mittelstraße, 링(Ringe) 북쪽 구간 |
| `kwartier-lateng` | 크바르티어 라텡(쥘피허 지구) | Zülpicher Str., Zülpicher Platz, Rathenauplatz, Kyffhäuserstr., Roonstr., Engelbertstr., 대학가, Barbarossaplatz |
| `ehrenfeld` | 에렌펠트 | 귀르텔(Gürtel) 바깥 Venloer Str., Körnerstr., Subbelrather Str., Neuehrenfeld, Helios 일대 |
| `suedstadt-rheinauhafen` | 쥐트슈타트·라인아우하펜 | Severinsviertel(Severinstr.), Chlodwigplatz, Volksgarten, Alteburger Str., Elsaßstr., Bonner Str. 북쪽, Rheinauhafen, Pantaleonsviertel |
| `agnesviertel-eigelstein` | 아그네스 지구·아이겔슈타인 | Eigelstein, Agnesviertel, Neustadt-Nord(Ebertplatz, Neusser Str. 안쪽), 중앙역 북쪽 Kunibertsviertel |
| `deutz-messe` | 도이츠·메쎄(강 건너) | 라인강 동안 Deutz, 쾰른 메쎄(Koelnmesse), LANXESS arena, Deutzer Freiheit, Rheinboulevard, Rheinpark, KölnTriangle |
| `other` | 기타 시내 | Lindenthal, Sülz, Nippes, Mülheim, Riehl, Bayenthal, Porz 등 |

## Place (식음료: `data/restaurants.json`, `data/bars.json`, `data/shops.json`)

```jsonc
{
  "id": "nuvola-napoli",                 // kebab-case, 전체에서 유일
  "name": "Nuvola Napoli",
  "category": "restaurant",
  "area": "deutz-messe",
  "address": "Deutzer Freiheit 66a, 50679 Köln",   // 번지+우편번호까지 (좌표 계산용)
  "lat": null, "lng": null,              // scripts/geocode.py가 채움 (임의 추정 금지)
  "cuisine": "Neapolitan pizza",         // 짧은 영어 설명
  "cuisine_country": ["IT"],
  "cuisine_region": "southern-europe",   // 생략하면 자동 계산
  "dishes": ["pizza"],
  "diet": ["vegetarian"],
  "meals": ["lunch", "dinner"],
  "occasions": ["group", "quick"],
  "features": ["terrace"],
  "drinks": [],
  "vibe": ["local-favorite"],
  "reservation": "recommended",
  "payment": "unknown",
  "price_level": 2,
  "price_pp": {"min": 12, "max": 20},    // 선택
  "price_note": "피자 €9–16",
  "beer_price_eur": 2.4,                 // 맥주 펍: 쾰시 0.2 l(또는 가장 싼 생맥주) 가격, 출처 있을 때만
  "beer_price_note": "Kölsch 0.2 l €2.40 (2026-03, express.de)",
  "beers": ["Päffgen Kölsch"],           // 탭에 있는 대표 맥주·브랜드
  "google_rating": 4.8,
  "google_reviews": 1172,
  "google_as_of": "2026-05",             // 출처에 표시된 기준 시점 (없으면 null)
  "rating_source": "werkenntdenbesten.de",
  "summary_ko": "한두 문장 설명",
  "must_try": ["Pizza Margherita (마르게리타)"],
  "tips_ko": "예약/현금/웨이팅 팁",
  "website": "https://…",
  "awards": ["Michelin Bib Gourmand 2026"],
  "sources": ["https://…"],
  "confidence": "high"                   // high | medium | low
}
```

## Attraction (관광지: `data/attractions.json`)

```jsonc
{
  "id": "koelner-dom",
  "name": "Kölner Dom",
  "name_ko": "쾰른 대성당",
  "category": "landmark",               // landmark | church | museum | viewpoint | park-nature | experience-tour | shopping | market-event | nightlife-area
  "area": "dom-altstadt",
  "address": "Domkloster 4, 50667 Köln",
  "lat": null, "lng": null,
  "summary_ko": "…", "tips_ko": "…",
  "price_eur": 0,                       // 성인 기본 입장료, 무료=0, 다양하면 null
  "price_note": "성당 무료 / 탑 €…",
  "duration_min": 60,
  "hours_note": "…",
  "booking": "not-needed",              // not-needed | recommended | required
  "status": "open",                     // open | closed-renovation | temporary-location | seasonal
  "season": null,                       // 시즌 이벤트면 {"start": "2026-11-16", "end": "2026-12-23"}
  "priority": 1,                        // 1=첫 방문 필수, 2=추천, 3=취향
  "tags": ["unesco", "free", "must-see"],
  "google_rating": 4.8, "google_reviews": 90000, "google_as_of": null, "rating_source": "…",
  "website": "https://…",
  "sources": ["https://…"]
}
```

관광지 `tags`: `unesco` · `free` · `indoor` · `rainy-day` · `kid-friendly` · `photo-spot` · `night-view` · `must-see` · `christmas` · `karneval` · `dom-view` · `romanesque` · `roman` · `art` · `history` · `chocolate` · `river` · `nature`
