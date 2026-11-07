# 데이터 스키마 (Data Schema)

모든 데이터 파일은 UTF-8 JSON입니다. `research/raw/*.json`(조사 원자료)을 `scripts/merge_raw.py`가 합쳐서
`data/*.json`(정제본)을 만들고, `scripts/build.py`가 그걸로 `guides/`의 표와 `docs/`의 웹 뷰어 데이터를 생성합니다.

## 선정 기준 (F&B)

| 항목 | 기준 |
|---|---|
| 구글 평점 | `google_rating >= 4.2` |
| 구글 리뷰 수 | `google_reviews >= 50` |
| 영업 상태 | 조사 시점(2026-11)에 폐업 신호가 없을 것 |
| 근거 | 평점·리뷰 수는 반드시 출처(`rating_source`)와 함께 기록. 추정치·기억에 의존한 숫자 금지 |

기준을 충족하지 못했거나 구글 수치를 확인하지 못한 곳은 `candidates`(후보)로 분리합니다.

## 공통 enum

### `area` — 지역

| id | 한국어 | 범위 |
|---|---|---|
| `dom-altstadt` | 대성당·구시가 | 쾰른 대성당, 중앙역(Hbf), 구시가(Alter Markt·Heumarkt·Fischmarkt·Martinsviertel·라인강변), Hohe Straße·Schildergasse~Neumarkt |
| `belgisches-viertel` | 벨기에 지구 | Hohenzollernring/Habsburgerring 서쪽~Stadtgarten·Aachener Weiher: Brüsseler Platz, Aachener Str.(초입), Antwerpener·Brabanter·Maastrichter·Lütticher·Flandrische Str., Bismarckstr., Venloer Str.(Bahnhof West까지) |
| `friesenviertel-ehrenstrasse` | 프리젠 지구·에렌슈트라세 | Friesenplatz, Friesenstr., Ehrenstraße, Apostelnviertel, Rudolfplatz/Hahnentor, Mittelstraße, 링(Ringe) 북쪽 구간 |
| `kwartier-lateng` | 크바르티어 라텡(쥘피허 지구) | Zülpicher Str., Zülpicher Platz, Rathenauplatz, Kyffhäuserstr., Roonstr., Engelbertstr., 대학가, Barbarossaplatz |
| `ehrenfeld` | 에렌펠트 | 귀르텔(Gürtel) 바깥 Venloer Str., Körnerstr., Subbelrather Str., Neuehrenfeld, Helios 일대 |
| `suedstadt-rheinauhafen` | 쥐트슈타트·라인아우하펜 | Severinsviertel(Severinstr.), Chlodwigplatz, Volksgarten, Alteburger Str., Elsaßstr., Bonner Str. 북쪽, Rheinauhafen(크란하우스·초콜릿 박물관) |
| `agnesviertel-eigelstein` | 아그네스 지구·아이겔슈타인 | Eigelstein, Agnesviertel, Neustadt-Nord(Ebertplatz, Neusser Str. 안쪽), 중앙역 북쪽 Kunibertsviertel |
| `deutz-messe` | 도이츠·메쎄(강 건너) | 라인강 동안(東岸) Deutz, 쾰른 메쎄(Koelnmesse), LANXESS arena, Deutzer Freiheit, Rheinboulevard, Rheinpark, KölnTriangle |
| `other` | 기타 시내 | Lindenthal, Sülz, Nippes, Mülheim, Riehl, Bayenthal, Porz 등 |
| `day-trip` | 근교 당일치기 | 본, 브륄, 뒤셀도르프, 아헨, 아르 계곡 등 (관광지 전용) |

### `category` — 식음료 유형

`restaurant` · `brauhaus`(쾰시 맥주홀) · `cafe` · `bakery` · `dessert` · `streetfood` · `cocktail-bar` · `wine-bar` · `beer-bar` · `bar` · `wine-shop`

### `cuisine_group` — 나라/스타일별 음식 (필터용)

`german` · `italian` · `french` · `mediterranean` · `spanish-portuguese` · `greek` · `turkish` · `middle-eastern` · `indian-south-asian` · `japanese` · `korean` · `chinese` · `vietnamese` · `thai-southeast-asian` · `asian-fusion` · `american-burger` · `latin-american` · `african` · `modern-european` · `vegan-vegetarian` · `seafood` · `steak-grill` · `cafe-bakery` · `dessert-icecream` · `international` · `bar-drinks`

### `price_level` — 1인 기준 음식값(음료 제외)

| 값 | 표기 | 1인 |
|---|---|---|
| 1 | € | ~€15 미만 |
| 2 | €€ | €15–30 |
| 3 | €€€ | €30–60 |
| 4 | €€€€ | €60 이상 (파인다이닝 코스 등) |

바(bar)는 칵테일 1잔 가격을 `price_note`에 적고, `price_level`은 1잔 기준 1=€10 미만, 2=€10–14, 3=€15–19, 4=€20 이상으로 씁니다.

### `tags`

`dom-view` · `rhine-view` · `terrace` · `rooftop` · `beer-garden` · `late-night` · `breakfast` · `brunch` · `lunch-deal` · `vegan-friendly` · `vegetarian-friendly` · `reservation-recommended` · `walk-in` · `cash-only` · `group-friendly` · `solo-friendly` · `date-night` · `business-dinner` · `local-favorite` · `touristy` · `kid-friendly` · `takeaway` · `koelsch` · `craft-beer` · `natural-wine` · `german-wine` · `michelin-star` · `bib-gourmand` · `near-messe` · `near-hbf` · `open-sunday`

## Place (식음료: `data/restaurants.json`, `data/bars.json`)

```jsonc
{
  "id": "peters-brauhaus",              // kebab-case, 전체에서 유일
  "name": "Peters Brauhaus",            // 공식 표기
  "category": "brauhaus",
  "area": "dom-altstadt",
  "address": "Mühlengasse 1, 50667 Köln",
  "lat": null, "lng": null,             // scripts/geocode.py가 채움 (임의 추정 금지)
  "cuisine": "Rhineland / Kölsch brauhaus",
  "cuisine_group": "german",
  "price_level": 2,
  "price_note": "메인 €16–26",
  "google_rating": 4.4,
  "google_reviews": 8395,
  "google_as_of": "2026-05",            // 출처에 표시된 기준 시점 (없으면 null)
  "rating_source": "werkenntdenbesten.de",
  "summary_ko": "한두 문장 설명",
  "must_try": ["Himmel un Ääd (감자퓌레+사과+피순대)"],
  "tags": ["koelsch", "group-friendly"],
  "tips_ko": "예약/현금/웨이팅 팁",
  "website": "https://…",
  "awards": ["Michelin Bib Gourmand 2026"],
  "sources": ["https://…"],
  "confidence": "high"                  // high | medium | low
}
```

## Attraction (관광지: `data/attractions.json`)

```jsonc
{
  "id": "koelner-dom",
  "name": "Kölner Dom",
  "name_ko": "쾰른 대성당",
  "category": "landmark",               // landmark | church | museum | viewpoint | park-nature | experience-tour | shopping | market-event | nightlife-area | day-trip
  "area": "dom-altstadt",
  "address": "Domkloster 4, 50667 Köln",
  "lat": null, "lng": null,
  "summary_ko": "…",
  "tips_ko": "…",
  "price_eur": 0,                       // 성인 기본 입장료, 무료=0, 다양하면 null
  "price_note": "성당 무료 / 탑 €… ",
  "duration_min": 60,
  "hours_note": "…",
  "booking": "not-needed",              // not-needed | recommended | required
  "status": "open",                     // open | closed-renovation | temporary-location | seasonal
  "season": null,                       // 시즌 이벤트면 {"start": "2026-11-16", "end": "2026-12-23"}
  "priority": 1,                        // 1=첫 방문 필수, 2=추천, 3=취향
  "tags": ["unesco", "free", "must-see"],
  "google_rating": 4.8, "google_reviews": 90000, "google_as_of": null, "rating_source": "…",
  "travel_time_min": null,              // day-trip만: 쾰른 중앙역 기준 편도
  "website": "https://…",
  "sources": ["https://…"]
}
```

관광지 `tags`: `unesco` · `free` · `indoor` · `rainy-day` · `kid-friendly` · `photo-spot` · `night-view` · `must-see` · `christmas` · `karneval` · `dom-view` · `romanesque` · `roman` · `art` · `history` · `chocolate` · `river` · `nature`
