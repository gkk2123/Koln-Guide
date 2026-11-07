# Köln Guide — 쾰른 맛집·바·관광지 가이드

쾰른(Köln) 시내 여행용 가이드 데이터와 뷰어입니다. 쾰른 시 경계(우편번호 50667–51149) 안의 장소만 다룹니다. 구글 평점 4.2 이상·리뷰 50개 이상인 식음료(29개 나라 음식), 칵테일바,
관광지, 독일 화이트와인 가이드를 한곳에 모아 **가격·거리·나라·요리·지역·평점** 등으로 걸러 볼 수 있게 만들었습니다.

## 바로 보기

| 보고 싶은 것 | 위치 |
|---|---|
| 필터 웹 뷰어 (목록·실제 지도, **내 주변**: 위치 허용 시 가까운 순·도보 시간·반경, 러닝 코스 지도) — **비밀번호로 잠김** | GitHub Pages: <https://gkk2123.github.io/Koln-Guide/> (Settings → Pages에서 이 브랜치의 `/docs`를 켜면 열려요). 비밀번호는 만든 사람에게 받으세요 |
| 세계 음식 분석 (나라·동네·요리별 추천, 한식) | [`guides/international-food.md`](guides/international-food.md) |
| 이번 시즌 (2026-11~2027-02): 대성당 입장료, 휴관, 11.11 카니발, 크리스마스 마켓 | [`guides/season-2026-11-to-2027-02.md`](guides/season-2026-11-to-2027-02.md) |
| 관광지 입장권·운영시간 (11–12월 요일별 시간, 마지막 입장, 공휴일 휴관, 무료·할인, 예약, 패스) | [`guides/tables/attractions-tickets-hours.md`](guides/tables/attractions-tickets-hours.md) · 웹 뷰어 관광지 탭 "오늘 여는 곳" |
| 벨기에 지구 집중: 독일·쾰른 요리 · 와인바(조용한 곳 표시) · 바·라운지 | [`guides/tables/belgisches-viertel.md`](guides/tables/belgisches-viertel.md) · 웹 뷰어 "벨기에 지구"·"와인바"·"조용한 곳"·"활기찬 곳" 빠른 선택 |
| 가성비 맥주 펍 (브라우하우스·크나이페·크래프트 맥주, 쾰시 가격) | [`guides/beer-pubs.md`](guides/beer-pubs.md) · [표](guides/tables/beer-pubs.md) |
| World's 50 Best Bars & 쾰른 칵테일바 | [`guides/bars-and-worlds-50-best.md`](guides/bars-and-worlds-50-best.md) |
| 미쉐린 2026 쾰른 | [`guides/fine-dining-michelin-2026.md`](guides/fine-dining-michelin-2026.md) |
| 독일 화이트와인 가이드 | [`guides/german-white-wine.md`](guides/german-white-wine.md) |
| 러닝 코스 6개 + 현지인 인기 스폿 (프리젠플라츠 출발·도착, 5.3–13.3 km) | [`guides/running-route.md`](guides/running-route.md) · 구글 마이맵 [`routes/koln-running.kml`](routes/koln-running.kml) · GPX 코스별 `routes/koln-running-*.gpx` |
| 표: 지역별 · 나라·문화권별 · 요리별 · 가격대별 · 바 · 벨기에 지구 · 관광지 · 입장권·운영시간 · 메쎄 근처 · 대성당 근처 · 후보 | [`guides/tables/`](guides/tables/) |

터미널에서도 바로 필터링할 수 있습니다. 한 옵션 안의 값은 OR, 옵션끼리는 AND입니다.

```bash
python3 scripts/filter.py --country KR --country JP                 # 한식 또는 일식
python3 scripts/filter.py --region middle-east --area ehrenfeld     # 에렌펠트의 중동·터키 음식
python3 scripts/filter.py --dish ramen --dish pho                   # 라멘 또는 쌀국수
python3 scripts/filter.py --diet vegan --price 1-2                  # 비건, €~€€
python3 scripts/filter.py --occasion business --area deutz-messe    # 메쎄 근처 비즈니스 식사
python3 scripts/filter.py --kind beer --max-beer 2.6 --sort beer     # 쾰시 €2.60 이하, 싼 순
python3 scripts/filter.py --kind bar --category cocktail-bar
python3 scripts/filter.py --style tapas --style wine-bar --style bistro  # 타파스·와인바·비스트로
python3 scripts/filter.py --kind sight --tag free --tag rainy-day   # 무료 + 비 오는 날
python3 scripts/filter.py --near messe --max-km 1.5 --sort distance # 메쎄 1.5km 이내, 가까운 순
```

## 선정 기준

- **식음료:** 구글 평점 **4.2 이상** + 리뷰 **50개 이상**, 조사 시점(2026-11)에 폐업 신호 없음.
  평점·리뷰 수는 구글 데이터를 보여 주는 집계 사이트(Wanderlog, restaurantguru, werkenntdenbesten 등)에서 출처와 함께 기록했고,
  추정치는 쓰지 않았습니다. 수치를 못 찾았거나 출처 귀속이 애매한 곳은 [후보](guides/tables/candidates.md)로 분리했습니다.
- **관광지:** 평점 기준 없음. 2026년 운영 상태(공사·임시 장소·시즌)를 확인해 표시. 다리·광장·공원 같은 공공장소는 "상시 개방"으로 표시.
  입장권·운영시간은 박물관·성당·시설 공식 사이트를 우선으로 11–12월 기준을 적고, 확인 시점과 신뢰도(공식 2026 / 공식 날짜 미표기 / 참고용)를 함께 남겼습니다.
  출처에서 확인하지 못한 요일·요금은 비워 두고 "미확인"으로 표시합니다.
- **가격대(1인 음식값, 음료 제외):** € ~15 · €€ 15–30 · €€€ 30–60 · €€€€ 60+ (바는 칵테일 1잔 기준).
  카페·간편식·디저트·브라우하우스·파인다이닝은 출처가 없을 때 유형 기준 추정값을 넣고 **"추정"**으로 표시합니다.
- **거리:** 쾰른 대성당 · 중앙역 · 쾰른 메쎄 · 벨기에 지구 기준 직선거리, 또는 웹 뷰어에서 아무 장소나 기준점으로 선택.

## 분류 체계 (v2)

| 필터 | 값 예시 |
|---|---|
| 유형 | 레스토랑 · 파인다이닝 · 브라우하우스 · 간편식·임비스 · 카페 · 베이커리 · 디저트 · 칵테일바 · 맥주바 · 동네 펍(크나이페) · 와인바 |
| 스타일 | 비스트로 · 브라세리 · 트라토리아 · 피자리아 · 이자카야 · 타파스·셰어링 · 메제 · 와인바 · 스테이크하우스 · 그릴·바비큐 · 라멘집 · 스시 · 면 요리집 · 파스타 바 · 버거 · 치킨 · 케밥·되너 · 스트리트 푸드 · 가스트하우스 · 칸티나 · 뷔페 · 아침·브런치 카페 … — 설명 문구에서 자동 분류(`schema.infer_style`) |
| 맥주 | 쾰시·크래프트 맥주, **쾰시 0.2 l 가격**(출처 있는 곳만), 탭 브랜드 |
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
│   ├── attractions.json         관광지·박물관·성당·시즌 이벤트 (쾰른 시내) + 입장권·요일별 운영시간
│   ├── passes.json              쾰른카드·뮤지엄카드 등 패스·콤비 티켓
│   ├── site.json                웹 뷰어 잠금 설정 (암호화 방식·솔트 — 비밀번호는 저장하지 않음)
│   ├── wine.json                와인 품종·산지·용어 (뷰어용)
│   ├── candidates.json          검증 대기·기준 미달 후보
│   ├── routes-spec.json         러닝 코스 경유지 정의 (공개 장소만)
│   └── routes.json              뷰어용 러닝 코스 (생성물)
├── guides/                      사람이 읽는 가이드 + tables/(자동 생성 표)
├── research/
│   ├── methodology.md           조사 방법·한계·다음 단계
│   └── raw/                     조사 원자료(JSON) + 조사 노트 — 1차(fnb-*, bars, attractions, wine-*) · 2차(r2-*) · 3차(r3-*)
│                                · 4차 재확인(r4-verify-*) · 5차 입장권·운영시간(r5-tickets-*)
├── scripts/
│   ├── schema.py                분류 어휘·라벨·v1→v2 변환
│   ├── import_raw.py            research/raw → data/ 병합·중복 제거·기준 적용
│   ├── geocode.py               주소 → 좌표 (OSM Nominatim 또는 Google)
│   ├── verify_google_places.py  Google Places API로 평점·리뷰 수·영업 상태 재검증
│   ├── build.py                 data/ → guides/tables/*.md + docs/
│   ├── build_routes.py          러닝 코스 계산 (OSM 보행 경로) → routes/, data/routes.json
│   ├── filter.py                CLI 필터
│   └── templates/viewer.html    웹 뷰어 템플릿
├── routes/                      러닝 코스 파일 (KML: 구글 마이맵 · GPX: 러닝 앱 · GeoJSON)
└── docs/                        GitHub Pages 웹 뷰어 (생성물: index.html + data.enc.js — 암호화된 데이터)
```

## 데이터 갱신

```bash
python3 scripts/import_raw.py                  # research/raw/*.json → data/*.json
python3 scripts/geocode.py                     # 좌표 채우기 (캐시 사용, 주소가 바뀐 곳만 새로 조회) → 거리 필터
GOOGLE_MAPS_API_KEY=... python3 scripts/verify_google_places.py   # (선택) 구글 평점·가격대 실시간 재검증
python3 scripts/build_routes.py                # (선택) 러닝 코스 다시 계산 → routes/, data/routes.json
KOLN_GUIDE_PASSWORD=... python3 scripts/build.py   # 표와 웹 뷰어 다시 만들기 (비밀번호로 docs/ 암호화)
```

`import_raw.py`는 `research/raw` 기준으로 `data/`를 다시 쓰므로, 손으로 고친 내용은 `research/raw`에도 반영하세요.

**지도·내 위치:** GitHub Pages 뷰어는 OpenStreetMap 지도(타일 © OpenStreetMap 기여자, 라이브러리 Leaflet 1.9.4 — `scripts/vendor/leaflet`)를 씁니다.
"내 주변"을 누르면 브라우저가 위치 권한을 묻고, 허용하면 파란 점과 함께 가까운 순(직선거리·도보 어림 시간)과 500m/1km/2km 반경으로 보여 줘요.
위치는 거리 계산과 지도 표시에만 쓰고 저장하지 않습니다. 쾰른에서 30km 넘게 떨어져 있으면 그 사실을 알려 주고 대성당 기준으로 보여 줘요.
claude.ai 페이지는 외부 지도 이미지를 불러올 수 없어 간단한 약도를 그대로 씁니다.

**웹 뷰어 잠금:** `docs/`에는 가이드 데이터가 AES-256-GCM 암호문(`docs/data.enc.js`)으로만 들어가고, 페이지가 비밀번호를 물어
브라우저 안에서 풀어요(키 = PBKDF2-SHA256 60만 회). 비밀번호는 저장소 어디에도 없고, `KOLN_GUIDE_PASSWORD` 없이 `build.py`를 돌리면
`docs/`는 그대로 둬요(실수로 평문이 올라가지 않게). "이 기기에서 기억하기"를 켜면 그 브라우저는 다음부터 바로 열리고, 맨 아래 "잠그기"로 지울 수 있어요.
단, **이 저장소 자체가 공개**라 `data/`·`guides/`·`research/`의 원자료는 GitHub에서 누구나 볼 수 있어요. 잠금은 웹 뷰어에만 걸립니다.
같은 곳이 여러 조사 파일에 있으면 나중 조사(r2-*)가 우선합니다.

## 진행 상황

<!--STATUS-->
**2026-11-07 기준**

| 항목 | 상태 |
|---|---|
| 식음료 (구글 4.2+/50+) | **식당 113곳 + 카페·디저트 24곳, 29개 나라** · 칵테일·와인바·바 21곳 |
| 맥주 펍 | **34곳** — 브라우하우스 16 · 동네 펍(크나이페) 15 · 크래프트/벨기에 맥주바 3. 쾰시 가격 확인 9곳(€1.60–2.50, 일부 2024년 가격) |
| 관광지 | 61곳 (대성당·성당·박물관·전망·공원·동물원·유람선·크리스마스 마켓·카니발) — 쾰른 시내만 |
| 입장권·운영시간 (2026-11-07) | 39곳 공식 사이트 위주 확인 — 요금 33곳 · 요일별 시간 39곳 · 연말·특별 일정 21곳 · 크리스마스 마켓 6곳 2026 일정 확정 · 패스 6종 — [표](guides/tables/attractions-tickets-hours.md) |
| World's 50 Best Bars | 쾰른 바 없음 (2025·2026, 1–100위). 독일 전체로도 2026년 0곳 |
| 미쉐린 2026 | 쾰른 스타 10곳·빕 구르망 3곳 |
| 독일 화이트와인 가이드 | 완료 (품종 12 · 산지 13 · 라벨 용어 59) |
| 후보 (검증 대기·기준 미달) | 224곳 |
| 좌표 · 거리 필터 | 완료 — 217곳 (OpenStreetMap Nominatim). 대성당·중앙역·메쎄·벨기에 지구·아무 장소 기준 |
| 가격대·스타일 (2026-11-07) | 가격대 176곳 중 141곳(55곳은 유형 기준 추정·약한 근거라 "약" 표시) · 스타일(비스트로·와인바·타파스…) 127곳 · 대표 메뉴 130곳 — [조사 방법](research/methodology.md) |
| 벨기에 지구 집중 (2026-11-07) | 독일·쾰른 요리 7곳 · 와인바 6곳(조용한 곳 표시) · 바·라운지 6곳 추가 — [표](guides/tables/belgisches-viertel.md) |
| 정확도 재확인 (2026-11-07) | 161곳 중 141곳 영업 확인 · 임시휴업 3곳·평점 하락 1곳 제외 · 구글 수치 61곳 갱신 — [보고서](research/verification-2026-11-07.md) |
| 남은 일 | 일반 레스토랑 가격대 일부 · 와인바/와인숍 · 메쎄 방문자 정보 · 대성당·성당 성탄 시간 · 구글 Places API 연동(키 필요) |

조사 방법과 한계는 [`research/methodology.md`](research/methodology.md)에 있습니다.
