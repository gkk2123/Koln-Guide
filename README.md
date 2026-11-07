# Köln Guide — 쾰른 맛집·바·관광지 가이드

쾰른 여행용 가이드 데이터와 뷰어입니다. 구글 평점 4.2 이상·리뷰 50개 이상인 식음료, 칵테일바, 관광지,
독일 화이트와인 가이드를 한곳에 모아 **가격·거리·나라 음식·지역·평점**으로 걸러 볼 수 있게 만들었습니다.

## 바로 보기

| 보고 싶은 것 | 위치 |
|---|---|
| 필터 웹 뷰어 (가격·거리·나라 음식·지역·평점·태그) | [`docs/index.html`](docs/index.html) — 브라우저로 열기. GitHub Pages로 올리려면 Settings → Pages → Branch `/docs` |
| 지역별 / 나라·스타일별 / 가격대별 표 | [`guides/tables/`](guides/tables/) |
| 메쎄 근처 · 대성당 근처 | [`guides/tables/near-messe.md`](guides/tables/near-messe.md) · [`guides/tables/near-dom.md`](guides/tables/near-dom.md) |
| World's 50 Best Bars & 쾰른 칵테일바 | [`guides/bars-and-worlds-50-best.md`](guides/bars-and-worlds-50-best.md) |
| 독일 화이트와인 가이드 | [`guides/german-white-wine.md`](guides/german-white-wine.md) |
| 검증 대기 후보 | [`guides/tables/candidates.md`](guides/tables/candidates.md) |

터미널에서 바로 필터링할 수도 있습니다.

```bash
python3 scripts/filter.py --area belgisches-viertel --price 1-2       # 벨기에 지구, €~€€
python3 scripts/filter.py --cuisine korean --cuisine japanese         # 한식·일식
python3 scripts/filter.py --near messe --max-km 1.5 --sort distance   # 메쎄 1.5km 이내, 가까운 순 (좌표 필요)
python3 scripts/filter.py --kind bar --category cocktail-bar
python3 scripts/filter.py --kind sight --tag free --tag rainy-day     # 무료 + 비 오는 날 관광지
```

## 선정 기준

- **식음료:** 구글 평점 **4.2 이상** + 리뷰 **50개 이상**, 조사 시점(2026-11)에 폐업 신호 없음.
  평점·리뷰 수는 구글 데이터를 보여주는 집계 사이트에서 출처와 함께 기록했고, 추정치는 쓰지 않았습니다.
  수치를 못 찾았거나 출처 귀속이 애매한 곳은 본 목록이 아니라 [후보](guides/tables/candidates.md)로 분리했습니다.
- **관광지:** 평점 기준 없음. 2026년 운영 상태(공사·임시 장소·시즌)를 확인해 표시.
- **가격대(1인 음식값, 음료 제외):** € ~15 · €€ 15–30 · €€€ 30–60 · €€€€ 60+ (바는 칵테일 1잔 기준)
- **거리:** 쾰른 대성당 · 중앙역 · 쾰른 메쎄 · 벨기에 지구 기준 직선거리. 웹 뷰어에서 기준점을 바꿀 수 있습니다.

## 지역

| id | 지역 | 성격 |
|---|---|---|
| `dom-altstadt` | 대성당·구시가 | 대성당·중앙역·라인강변. 전통 브라우하우스 밀집, 관광객 최다 |
| `belgisches-viertel` | 벨기에 지구 | 브뤼셀 광장 중심의 카페·편집숍·바 동네 |
| `friesenviertel-ehrenstrasse` | 프리젠 지구·에렌슈트라세 | 쇼핑 거리 + 바 씬의 중심 |
| `kwartier-lateng` | 크바르티어 라텡 | 대학가. 가성비 맛집·펍, 카니발 인파 중심 |
| `ehrenfeld` | 에렌펠트 | 다문화·스트리트아트·클럽, 터키·중동 음식 |
| `suedstadt-rheinauhafen` | 쥐트슈타트·라인아우하펜 | 토박이 동네 + 강변 신시가(초콜릿 박물관) |
| `agnesviertel-eigelstein` | 아그네스 지구·아이겔슈타인 | 중앙역 북쪽, 로컬 술집과 조용한 레스토랑 |
| `deutz-messe` | 도이츠·메쎄(강 건너) | 쾰른 메쎄·LANXESS arena, 대성당 야경 명소 |

지역 경계와 기준점 좌표는 [`data/areas.json`](data/areas.json)에 있습니다.

## 폴더 구조

```
Koln-Guide/
├── README.md
├── data/                        정제 데이터 (사람이 직접 고치는 원본)
│   ├── SCHEMA.md                필드·enum 정의
│   ├── areas.json               지역 정의 + 거리 기준점
│   ├── restaurants.json         레스토랑·브라우하우스·카페·디저트 (기준 충족)
│   ├── bars.json                칵테일바·맥주바·와인바 (기준 충족)
│   ├── shops.json               와인숍
│   ├── attractions.json         관광지·박물관·성당·시즌 이벤트·근교
│   ├── wine.json                와인 품종·산지·용어 (뷰어용)
│   └── candidates.json          검증 대기·기준 미달 후보
├── guides/
│   ├── bars-and-worlds-50-best.md
│   ├── german-white-wine.md
│   └── tables/                  자동 생성 표 (scripts/build.py)
├── research/
│   ├── methodology.md           조사 방법·한계·다음 단계
│   └── raw/                     지역·주제별 조사 원자료(JSON) + 조사 노트
├── scripts/
│   ├── import_raw.py            research/raw → data/ 병합·중복 제거·기준 적용
│   ├── geocode.py               주소 → 좌표 (OSM Nominatim 또는 Google)
│   ├── verify_google_places.py  Google Places API로 평점·리뷰 수·영업 상태 재검증
│   ├── build.py                 data/ → guides/tables/*.md + docs/
│   ├── filter.py                CLI 필터
│   └── templates/viewer.html    웹 뷰어 템플릿
└── docs/
    ├── index.html               필터 웹 뷰어 (생성물)
    └── data.js                  뷰어 데이터 (생성물)
```

## 데이터 갱신

```bash
python3 scripts/import_raw.py                  # research/raw/*.json → data/*.json
python3 scripts/geocode.py                     # (선택) 좌표 채우기 → 거리 필터 활성화
GOOGLE_MAPS_API_KEY=... python3 scripts/verify_google_places.py   # (선택) 구글 평점 실시간 재검증
python3 scripts/build.py                       # 표와 웹 뷰어 다시 만들기
```

`data/*.json`을 직접 고쳐도 됩니다. 단, `import_raw.py`를 다시 돌리면 `research/raw` 기준으로 덮어쓰니
손으로 고친 내용은 `research/raw`에도 반영하세요. 필드 정의는 [`data/SCHEMA.md`](data/SCHEMA.md).

## 진행 상황

<!--STATUS-->
**1차 조사 (2026-11-07)**

| 항목 | 상태 |
|---|---|
| 폴더 구조 · 스키마 · 빌드/필터/검증 스크립트 · 웹 뷰어 | 완료 |
| World's 50 Best Bars 확인 | 완료 — 쾰른 바 없음 (2025·2026, 1–100위). [상세](guides/bars-and-worlds-50-best.md) |
| 미쉐린 2026 쾰른 목록 | 완료 — 스타 10곳·빕 구르망 3곳. [상세](guides/fine-dining-michelin-2026.md) |
| 맛집 구글 평점 검증 | 진행 중 — 12곳 확정, 후보 125곳 검증 대기 |
| 바 구글 평점 검증 | 진행 중 — 후보 11곳 |
| 독일 화이트와인 가이드 · 관광지 | 조사 중 |
| 좌표(거리 필터) | 대기 — 지오코딩 호스트 접근 필요 |

1차 조사는 웹 검색 한도(한 번의 요청당 200회, 모든 조사 에이전트 공유)에 걸려 후보 발굴까지만 진행됐습니다.
조사 방법과 한계는 [`research/methodology.md`](research/methodology.md)에 정리합니다.
