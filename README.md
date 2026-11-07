# Köln Guide — 쾰른 맛집·바·관광지 가이드

쾰른 여행용 가이드 데이터와 뷰어입니다. 구글 평점 4.2 이상·리뷰 50개 이상인 식음료(30개 나라 음식), 칵테일바,
관광지, 독일 화이트와인 가이드를 한곳에 모아 **가격·거리·나라·요리·지역·평점** 등으로 걸러 볼 수 있게 만들었습니다.

## 바로 보기

| 보고 싶은 것 | 위치 |
|---|---|
| 필터 웹 뷰어 | [`docs/index.html`](docs/index.html) — 브라우저로 열기. GitHub Pages로 올리려면 Settings → Pages → Branch `/docs` |
| 세계 음식 분석 (나라·동네·요리별 추천, 한식) | [`guides/international-food.md`](guides/international-food.md) |
| 이번 시즌 (2026-11~2027-02): 대성당 입장료, 휴관, 11.11 카니발, 크리스마스 마켓 | [`guides/season-2026-11-to-2027-02.md`](guides/season-2026-11-to-2027-02.md) |
| World's 50 Best Bars & 쾰른 칵테일바 | [`guides/bars-and-worlds-50-best.md`](guides/bars-and-worlds-50-best.md) |
| 미쉐린 2026 쾰른 | [`guides/fine-dining-michelin-2026.md`](guides/fine-dining-michelin-2026.md) |
| 독일 화이트와인 가이드 | [`guides/german-white-wine.md`](guides/german-white-wine.md) |
| 표: 지역별 · 나라·문화권별 · 요리별 · 가격대별 · 바 · 관광지 · 메쎄 근처 · 대성당 근처 · 후보 | [`guides/tables/`](guides/tables/) |

터미널에서도 바로 필터링할 수 있습니다. 한 옵션 안의 값은 OR, 옵션끼리는 AND입니다.

```bash
python3 scripts/filter.py --country KR --country JP                 # 한식 또는 일식
python3 scripts/filter.py --region middle-east --area ehrenfeld     # 에렌펠트의 중동·터키 음식
python3 scripts/filter.py --dish ramen --dish pho                   # 라멘 또는 쌀국수
python3 scripts/filter.py --diet vegan --price 1-2                  # 비건, €~€€
python3 scripts/filter.py --occasion business --area deutz-messe    # 메쎄 근처 비즈니스 식사
python3 scripts/filter.py --kind bar --category cocktail-bar
python3 scripts/filter.py --kind sight --tag free --tag rainy-day   # 무료 + 비 오는 날
python3 scripts/filter.py --near messe --max-km 1.5 --sort distance # 메쎄 1.5km 이내 (좌표 필요)
```

## 선정 기준

- **식음료:** 구글 평점 **4.2 이상** + 리뷰 **50개 이상**, 조사 시점(2026-11)에 폐업 신호 없음.
  평점·리뷰 수는 구글 데이터를 보여 주는 집계 사이트(Wanderlog, restaurantguru, werkenntdenbesten 등)에서 출처와 함께 기록했고,
  추정치는 쓰지 않았습니다. 수치를 못 찾았거나 출처 귀속이 애매한 곳은 [후보](guides/tables/candidates.md)로 분리했습니다.
- **관광지:** 평점 기준 없음. 2026년 운영 상태(공사·임시 장소·시즌)를 확인해 표시. 다리·광장·공원 같은 공공장소는 "상시 개방"으로 표시.
- **가격대(1인 음식값, 음료 제외):** € ~15 · €€ 15–30 · €€€ 30–60 · €€€€ 60+ (바는 칵테일 1잔 기준).
  카페·간편식·디저트·브라우하우스·파인다이닝은 출처가 없을 때 유형 기준 추정값을 넣고 **"추정"**으로 표시합니다.
- **거리:** 쾰른 대성당 · 중앙역 · 쾰른 메쎄 · 벨기에 지구 기준 직선거리, 또는 웹 뷰어에서 아무 장소나 기준점으로 선택.

## 분류 체계 (v2)

| 필터 | 값 예시 |
|---|---|
| 유형 | 레스토랑 · 파인다이닝 · 브라우하우스 · 간편식·임비스 · 카페 · 베이커리 · 디저트 · 칵테일바 · 맥주바 · 와인바 |
| 문화권 → 나라 | 동아시아(한국·일본·중국…) · 동남아 · 남아시아 · 중동·터키·북아프리카 · 남유럽 · 서유럽 · 독일·중부유럽 · 동유럽 · 아메리카 · 아프리카 · 퓨전 |
| 요리 | 라멘 · 스시 · 쌀국수 · 케밥·되너 · 팔라펠 · 메제 · 피자 · 타코 · 고기구이 · 치킨 · 만두·딤섬 · 쾰른 향토 요리 · 코스 요리 · 브런치 · 케이크 … (32종) |
| 식단 / 시간대 / 상황 | 비건·채식·할랄·글루텐프리 / 아침·브런치·점심·저녁·심야 / 데이트·비즈니스·단체·혼밥·가족·빠른 한 끼 |
| 공간·분위기·음료 | 대성당 뷰·라인강 뷰·테라스·루프탑·일요일 영업 / 현지인 단골·관광객 많음·숨은 맛집 / 쾰시·크래프트 맥주·칵테일 |
| 예약 · 결제 · 수상 | 예약 필수·워크인 / 현금만 / 미쉐린 스타·빕 구르망·셀렉티드 |
| 가격 · 평점 · 지역 · 거리 | 위 기준 참고 |

필드 정의는 [`data/SCHEMA.md`](data/SCHEMA.md). 1차 조사 데이터(v1 `tags`·`cuisine_group`)는 import 단계에서 자동 변환됩니다.

## 지역

| id | 지역 | 성격 |
|---|---|---|
| `dom-altstadt` | 대성당·구시가 | 대성당·중앙역·라인강변. 전통 브라우하우스 밀집, 관광객 최다 |
| `belgisches-viertel` | 벨기에 지구 | 브뤼셀 광장 중심의 카페·편집숍·바, 라멘·스시 밀집 |
| `friesenviertel-ehrenstrasse` | 프리젠 지구·에렌슈트라세 | 쇼핑 거리 + 바 씬의 중심 |
| `kwartier-lateng` | 크바르티어 라텡 | 대학가. 저렴한 다국적 음식·펍, 카니발 인파 중심 |
| `ehrenfeld` | 에렌펠트 | 다문화·스트리트아트·클럽, 쾰른 터키·중동 음식의 중심 |
| `suedstadt-rheinauhafen` | 쥐트슈타트·라인아우하펜 | 토박이 동네 + 강변 신시가, 파인다이닝 |
| `agnesviertel-eigelstein` | 아그네스 지구·아이겔슈타인 | 중앙역 북쪽, 로컬 술집과 아시아 식당 |
| `deutz-messe` | 도이츠·메쎄(강 건너) | 쾰른 메쎄·LANXESS arena, 대성당 야경 명소 |

지역 경계와 기준점 좌표는 [`data/areas.json`](data/areas.json)에 있습니다.

## 폴더 구조

```
Koln-Guide/
├── README.md
├── data/                        정제 데이터 (사람이 직접 고치는 원본)
│   ├── SCHEMA.md                필드·분류 정의 (v2)
│   ├── areas.json               지역 정의 + 거리 기준점
│   ├── restaurants.json         레스토랑·파인다이닝·브라우하우스·간편식·카페·디저트
│   ├── bars.json                칵테일바·맥주바·바
│   ├── shops.json               와인숍
│   ├── attractions.json         관광지·박물관·성당·시즌 이벤트·근교
│   ├── wine.json                와인 품종·산지·용어 (뷰어용)
│   └── candidates.json          검증 대기·기준 미달 후보
├── guides/                      사람이 읽는 가이드 + tables/(자동 생성 표)
├── research/
│   ├── methodology.md           조사 방법·한계·다음 단계
│   └── raw/                     조사 원자료(JSON) + 조사 노트 — 1차(fnb-*, bars, attractions, wine-*) · 2차(r2-*)
├── scripts/
│   ├── schema.py                분류 어휘·라벨·v1→v2 변환
│   ├── import_raw.py            research/raw → data/ 병합·중복 제거·기준 적용
│   ├── geocode.py               주소 → 좌표 (OSM Nominatim 또는 Google)
│   ├── verify_google_places.py  Google Places API로 평점·리뷰 수·영업 상태 재검증
│   ├── build.py                 data/ → guides/tables/*.md + docs/
│   ├── filter.py                CLI 필터
│   └── templates/viewer.html    웹 뷰어 템플릿
└── docs/                        필터 웹 뷰어 (생성물: index.html, data.js)
```

## 데이터 갱신

```bash
python3 scripts/import_raw.py                  # research/raw/*.json → data/*.json
python3 scripts/geocode.py                     # (선택) 좌표 채우기 → 거리 필터 활성화
GOOGLE_MAPS_API_KEY=... python3 scripts/verify_google_places.py   # (선택) 구글 평점·가격대 실시간 재검증
python3 scripts/build.py                       # 표와 웹 뷰어 다시 만들기
```

`import_raw.py`는 `research/raw` 기준으로 `data/`를 다시 쓰므로, 손으로 고친 내용은 `research/raw`에도 반영하세요.
같은 곳이 여러 조사 파일에 있으면 나중 조사(r2-*)가 우선합니다.

## 진행 상황

<!--STATUS-->
**2026-11-07 기준**

| 항목 | 상태 |
|---|---|
| 식음료 (구글 4.2+/50+) | **식당 99곳 + 카페·디저트 26곳, 30개 나라** · 바 14곳 |
| 관광지 | 60곳 (대성당·성당·박물관·전망·공원·크리스마스 마켓·카니발·근교 4곳) |
| World's 50 Best Bars | 쾰른 바 없음 (2025·2026, 1–100위). 독일 전체로도 2026년 0곳 |
| 미쉐린 2026 | 쾰른 스타 10곳·빕 구르망 3곳 |
| 독일 화이트와인 가이드 | 완료 (품종 12 · 산지 13 · 라벨 용어 59) |
| 후보 (검증 대기·기준 미달) | 202곳 |
| 남은 일 | 좌표(거리 필터) · 일반 레스토랑 67곳 가격대 · 와인바/와인숍 · 메쎄 방문자 정보 검증 |

조사 방법과 한계는 [`research/methodology.md`](research/methodology.md)에 있습니다.
