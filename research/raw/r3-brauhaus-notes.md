# r3-brauhaus 조사 노트 (2026-11-07)

범위: 쾰른 시내 쾰시 브라우하우스(category `brauhaus`). 0.2 l 쾰시 가격 조사, r1 브라우하우스 후보 21곳의 구글 수치·주소·영업 여부 검증, 이미 검증된 브라우하우스 7곳 재출력(쾰시 가격·맥주·결제 정보 병합용).

- 검색: **35/35회 사용** (4번째는 도메인 제한 검색이 API 오류로 거절됨. express.de·ksta.de·rundschau-online.de·wdr.de는 크롤러 접근 불가). 15번째부터는 `extended` 모드를 썼더니 구글 수치가 훨씬 잘 나왔다.
- 결과: places 13곳 (신규 통과 6 + 재출력 7), candidates 15곳.
- `python3 scripts/import_raw.py --dry-run`: r3 관련 경고는 재출력 7곳의 의도된 중복 병합뿐이다. enum 오류는 없다. 후보 15곳은 모두 살아남고, 같은 업소의 r1 후보 항목은 대체된다(r1의 found 내용은 r3 항목에 옮겨 적었다).

## 1. 신규 통과 (구글 ≥ 4.2, ≥ 50건)

| 업소 | 지역 | 주소 | 구글 | 출처 | 맥주 | 신뢰도 |
|---|---|---|---|---|---|---|
| Sünner im Walfisch | dom-altstadt | Salzgasse 13, 50667 | 4.5 (3,540) | 11880 google.de (교차: restaurantguru Google 4.5/3,424, Wanderlog 4.5/3,646, tripexpert Google 4.4/2,615) | Sünner Kölsch | high |
| Max Stark | agnesviertel-eigelstein | Unter Kahlenhausen 47, 50668 | 4.6 (3,953) | yably.de (날짜 없음) | Päffgen Kölsch | medium |
| Früh em Veedel | suedstadt-rheinauhafen | Chlodwigplatz 28, 50678 | 4.6 (1,327) | yably.de의 출처별 내역 | Früh Kölsch | medium |
| Brauhaus Pütz | kwartier-lateng | Engelbertstraße 67, 50674 | 4.5 (739) | restaurantguru (페이지 약 4년 전) | Mühlen Kölsch | medium |
| FRÜH "Em Jan von Werth" | friesenviertel-ehrenstrasse | Christophstraße 44, 50670 | 4.4 (1,090) | Wanderlog (r1 restaurantguru Google 4.4/1,163과 일치) | Früh Kölsch | medium |
| Gilden im Zims | dom-altstadt | Heumarkt 77, 50667 | 4.3 (9,551) | yably.de | Gilden Kölsch | medium |

- **Em Jan von Werth는 알터 마르크트가 아니다.** 과제에는 'Alter Markt'로 적혀 있었지만 정확한 주소는 Christophstraße 44, 50670 Köln이다(online-tischreservierung, trip.com, koeln.de). 알터 마르크트 46–48의 'Chocolaterie Jan von Werth'와 Jan-von-Werth-Brunnen(분수)은 다른 곳이다.
- yably.de는 'X bewertungen auf Google, Durchschnitt Y'처럼 구글이라고 명시하지만 날짜가 없고 출처가 하나뿐이라 medium으로 두었다.
- Wanderlog 상세 페이지는 숫자에 플랫폼 이름을 붙이지 않는다. 그래도 첫 번째 값(건수가 큰 쪽)이 다른 구글 출처와 일치했다(Sünner, Em Jan von Werth). 두 번째 값은 트립어드바이저와 비슷하다.

## 2. 후보 (기준 미달·미확인)

| 업소 | 판정 | 확인한 값 |
|---|---|---|
| Brauerei Päffgen (Friesenstr. 64–66, 50670) | 미달 | restaurantguru Google 3.9 (1,987), 11880 google.de 3.8 (2,272). verliebtinkoeln: 소란을 제지당한 파티 손님들이 낮은 평점을 남겼다는 기사 |
| Gaffel am Dom (Bahnhofsvorplatz 1, 50667) | 구글 없음 | r1의 '3.5'는 spinach.guide 자체 점수와 Yelp 3.5(227)로 구글이 아니다. '4.3'의 출처도 못 찾았다. TA 4.0 (~2,420), OpenTable 4.7 (902) |
| Brauhaus Sion (Unter Taschenmacher 5–7, 50667) | 미달 | werkenntdenbesten google.de 4.00 (7,644), Stand 2026-05-30 |
| Bierhaus en d'r Salzgass | 미달 | Wanderlog 3.9 (957), ProvenExpert 3.90 (750). Päffgen을 낸다. 주소가 검색 요약에는 Salzgasse **5–7**, r1 시드에는 5–11 |
| Haxenhaus zum Rheingarten (Frankenwerft 19, 50667) | 구글 없음 | TA 3.5 (830), Yelp 3.0 (80), TheFork 8.9/10 |
| Schreckenskammer (Ursulagartenstr. 11–15, 50668) | 구글 없음 | speisekarte.menu 약 4.0 (5,661, 구글 아님). 주말 예약 권장 |
| Em Kölsche Boor | 미달(귀속 불명) | reviewhero 4.1 (1,125). 번지는 이번에도 미검증 |
| Brauerei zum Pfaffen (Heumarkt 62, 50667) | 경계 | Google 4.1 (2,950) vs 4.20 (2,896), Wanderlog 4.2 (2,683). 건수가 가장 많은 값이 4.1이라 후보로 둠 |
| Hellers Brauhaus (Roonstr. 33) | 근사치뿐 | Wanderlog '약 4.2, 약 1,400건'. Yelp 2026-05/06 갱신(월 17–02시)이라 영업 중. 오래된 리뷰에 현금만 받는다는 말 |
| Brauhaus Johann Schäfer (Elsaßstr. 6, 50677) | 구글 없음 | Falstaff 84점, Feinschmecker 등재, 채식·비건 메뉴 |
| Brauhaus Reissdorf am Griechenmarkt (Kleiner Griechenmarkt 40, 50676) | 구글 단독 값 없음 | yably 4.36 (2,263, 4개 출처 합산), goto-where 4.4 (1,952, 귀속 불명) |
| Sion Bräues / Antik Brauhaus (Deutzer Freiheit 85–87) | 구글 없음 | restaurantguru 자체 4.0 (205). reviewhero 'Antik Brauhaus' 4.3 (661)이 이곳인지는 미확인. 현재 이름은 'Antik Brauhaus'라는 리뷰 |
| Gaffel Haus, Peters am Hahnentor, Gertrudenhof | 미조회 | 검색 예산 소진. Peters am Hahnentor는 업소가 있는지조차 확인 못 함 |

## 3. 쾰시 0.2 l 가격

| 업소 | 0.2 l | 기준 시점 | 출처 | JSON 반영 |
|---|---|---|---|---|
| FRÜH am Dom | **€2.50** | 메뉴에 'Oktober 2026' 표기 | frueh-am-dom.de 브라우하우스 메뉴 PDF ('FRÜH Kölsch vom Fass 0,2 l € 2,50') | `beer_price_eur` 2.5 |
| Peters Brauhaus | 약 €2.30 | 2025년 가을 | colognecitybreaks.com 'Kölner Kölsch-Brauhaus-Guide 2026' (검색 요약 기준, '약') | 2.3 |
| Brauerei zur Malzmühle | 약 €2.40 | 2025년 가을 | 같은 가이드 | 2.4 |
| Hellers Brauhaus (후보) | 약 €2.30 | 2025년 가을 | 같은 가이드 | 후보 found에만 |
| FRÜH "Em Jan von Werth" | €1.90 | **날짜 미확인** | t-online 'Kölsch-Preise: hier kostet ein Bier noch unter 2 Euro' | 반영 안 함(tips에만) |
| Brauwelt Köln (미조사) | €2.30 | 날짜 미확인 | speisekarte.de 메뉴 | — |
| 알트슈타트 브라우하우스 일반 | €2.20–2.30 | 2024년 여름 | verliebtinkoeln '…Kölsch maximal 2 Euro' | — |
| 중심가 브라우하우스 일반 | €2.30–2.80 | 날짜 미확인 | nomadotravel Kölsch-Guide | — |
| t-online 범위 | €2.00–2.80 (가장 싼 곳 Trierer Eck €1.70) | 날짜 미확인 | t-online | — |
| 옛 값 | Sion €2.20 (2022-10), Reissdorf am Griechenmarkt €1.70–1.90 (2020–22), Zum Alten Brauhaus Reissdorf €2.10 (2022-06 메뉴) | 오래됨 | verliebtinkoeln 비교, 메뉴 PDF | — |
| 신뢰 낮음 | €2.50–3.50 '2026' | 근거 없음 | chasingwhereabouts 블로그 | — |

- verliebtinkoeln의 '46개 업소 쾰시 가격 비교' 기사는 제목만 확인했다. 내용과 기준 날짜는 확인하지 못했다. 다음 라운드에서 가장 먼저 볼 출처다.
- Gürzenich·Kölnkongress 행사장 €2.90도 검색 요약에만 나왔고 출처가 불분명하다.

## 4. 결제·예약 (colognecitybreaks 2026 가이드, 페이지 약 103일 전)

- 오래된 집 중에는 현금만 받는 곳이 있다고 하지만, 어느 집인지는 밝히지 않았다.
- Päffgen과 Lommerzheim은 '현금을 선호·기대하는' 작은 옛 술집으로 분류된다. Lommerzheim은 예약을 전혀 받지 않는다(→ JSON `reservation: walk-in`).
- Peters와 Malzmühle은 예약을 받고 카드 결제도 점점 늘어나는 대형 브라우하우스로 분류된다.
- '현금만(cash-only)'이라고 단정한 출처는 이번 세션에 없었다. 그래서 `payment: cash-only`는 한 곳에도 넣지 않았다. Hellers(오래된 Yelp 리뷰)는 후보 found에만 적었다.
- Pfaffen은 카드는 받지만 최소 결제 금액이 있다는 Wanderlog 리뷰가 있다.

## 5. 쾰시 문화 — 출처 확인

**출처로 확인한 사실**
- **쾨베스(Köbes)**: 브라우하우스의 웨이터. 잔이 비기 전에 주문을 기다리지 않고 새 쾰시로 바꿔 준다. [en.wikipedia 'Kölsch (beer)'] (koelner-kompass.de 블로그 'Der Köbes: Warum Kölner Brauhäuser anders funktionieren'은 제목만 확인)
- **슈탕에(Stange) 0.2 l**: 쾰시는 전통적으로 가늘고 긴 원통형 0.2 l 잔에 나온다. 쾰시는 탄산이 비교적 적고 거품이 오래가지 않아서, 작은 잔이 맥주를 차갑고 신선하게 유지해 준다. [de.wikipedia 'Kölner Stange', biergartenkoeln.de 'Wat es en Stange?']
- **크란츠(Kranz)**: 쾨베스가 여러 잔을 한 번에 나르는 둥근 쟁반. 보통 11–20잔 정도가 들어가고, 정해진 표준은 없다. [verliebtinkoeln 'Warum wird das Kölsch in einem Kranz gebracht?']
- **코스터로 잔 덮기**: 맥주 코스터(Bierdeckel)를 잔 위에 올려 두면 '더는 안 마신다'는 신호다. [en.wikipedia]
- **코스터에 긋는 줄(Strich)**: 한 잔 낼 때마다 쾨베스가 손님 코스터에 줄을 하나씩 긋고, 계산할 때 줄 수만큼 낸다. [en.wikipedia]
- **2026년 쾰시 가격대**: 중심가 브라우하우스 0.2 l은 대략 €2.30–2.80이다(nomadotravel, 날짜 미확인). 2025–26년 개별 값으로 확인된 것은 Peters 약 €2.30, Malzmühle 약 €2.40(둘 다 2025년 가을), FRÜH am Dom €2.50(2026년 10월 메뉴)이다. 2024년 여름에는 알트슈타트가 €2.20–2.30이었다(verliebtinkoeln).
- **쾰시 협약(Kölsch-Konvention)**: 1986년 협약이다[en.wikipedia]. 'Kölsch'는 보호 명칭이라 협약에 따라 쾰른과 그 주변에서만 양조한다[colognecitybreaks]. 다만 협약에 서명한 쾰른 밖 양조장도 만들 수 있고, 일부 브랜드는 Früh에서 위탁 양조한다[en.wikipedia]. 그래서 '쾰른 안에서만'이 아니라 '쾰른과 그 주변'이 정확하다. 협약 양조장은 쾰시를 Stange로만 내기로 약속한다[de.wikipedia 'Kölner Stange'].
- 사례(약한 출처): Brauerei zum Pfaffen의 맥주는 Lohmar에서 양조돼 'Kölsch'라는 이름을 쓸 수 없다는 GastroGuide 이용자 글이 있다.
- about-drinks.com 'Kölsch Konvention 2026 – Vorstand des Kölner Brauerei-Verbandes bestätigt'는 제목만 확인했고 내용은 보지 못했다.

**미확인(출처 없음, 본문에 쓰려면 재확인 필요)**
- 'Köbes'라는 이름이 야고보(Jakob)에서 왔다는 어원 설.
- 쾨베스가 무뚝뚝하게 농담하거나 손님에게 반말하는 '전통'.
- 하르페 한(Halve Hahn, 호밀빵+치즈) 같은 안주 설명. 이번 세션에는 투어 상품 제목에만 등장했다.
- 쾰시의 적정 온도, Pils 잔에 달라고 하면 안 된다는 등의 에티켓.
- 쾰시 협약과 EU 지리적 표시 보호(PGI)의 관계. colognecitybreaks는 '보호 명칭'이라고만 썼다.

## 6. 의심·주의 (오케스트레이터용)

1. **병합 한계**: `import_raw.merge_into`는 빈 값(None/""/[])만 채운다. 기존 항목에 `reservation`/`payment`가 `"unknown"`으로 들어 있으면 r3 값이 반영되지 않는다. 시뮬레이션해 보니 Lommerzheim의 `walk-in`이 빠졌다. `beer_price_eur`·`beer_price_note`·`beers`·`vibe`는 정상적으로 병합된다(Peters 2.3, FRÜH am Dom 2.5, Malzmühle 2.4).
2. **`CATEGORY_SYNONYMS`가 `"kneipe"`를 `"bar"`로 바꾼다.** v2 스키마에서는 `kneipe`가 정식 카테고리라 서로 어긋난다. r3는 `brauhaus`만 써서 영향이 없지만, 다른 에이전트의 kneipe 항목은 bar로 바뀐다.
3. **우편번호**: Sünner(50667), Früh em Veedel(50678)은 이번 검색 요약에 PLZ가 직접 나오지 않아 지역명(Altstadt-Nord/Süd)으로 맞췄다. Gilden(Heumarkt 77)은 같은 광장의 Heumarkt 62가 50667로 확인됐다. Hellers(50674)·Sion Bräues(50679)는 r1 값이다.
4. 구글 수치를 출처 하나로만 확인한 곳: Max Stark, Gilden, Früh em Veedel(yably), Pütz(오래된 restaurantguru).
5. Päffgen은 유명한 하우스 양조장이지만 구글 3.8–3.9라 규칙상 후보로 갔다. 본문에서 '평점 기준 밖 명소'로 따로 소개할지는 편집에서 결정할 일이다.
6. 컨텍스트: Malzmühle가 Sünner 양조장을 인수했다는 r1 메모(Lebensmittelzeitung)가 있다. Sünner im Walfisch와 관계가 있을 수 있지만 이번에는 확인하지 않았다.
7. 음식 `price_level`은 메뉴 출처가 없어 신규 6곳 모두 null이다. import가 brauhaus 기본값 2를 추정치로 넣는다.

## 7. 새 리드 (미조사)

- Brauwelt Köln: reviewhero 4.3 (2,253), speisekarte.de 메뉴에 쾰시 0.2 l €2.30(날짜 미확인), 주소 미확인
- Zum Grinkenschmied: reviewhero 4.5 (318)
- reviewhero 목록에 'Braugasse 12' 업소: 4.5 (800), 이름이 잘려 있음
- Brauhaus Euro 'Reissdorf em Keuchhof': werkenntdenbesten 종합 4.41 (1,040, 7개 포털), 비어가든
- Kasalla-Brauhaus 'Marie & Johann': 새로 문 여는 곳, t-online 가격 기사 있음
- CityNEWS 'Lange Nacht der Kölschen Brauhäuser 2026: 18곳'
- Brauhaus Dellbrück(온라인 음료 메뉴), Zum Alten Brauhaus

## 8. 주요 출처

- 가격: https://www.frueh-am-dom.de/fileadmin/menus/Brauhaus/SpeisekarteBrauhaus.pdf · https://www.colognecitybreaks.com/de/city/cologne/articles/the-system-in-the-glass-inside-cologne-s-kolsch-ritual · https://koeln.t-online.de/region/koeln/id_100209048/koeln-koelsch-preise-hier-kostet-ein-bier-noch-unter-2-euro.html · https://verliebtinkoeln.com/koelner-lokale-in-denen-das-koelsch-noch-unter-2-euro-kostet/ · https://verliebtinkoeln.com/koelsch-preis-koeln-was-kostet-ein-koelsch-vergleich/ · https://verliebtinkoeln.com/die-bewertungen-und-preise-von-7-koelschen-brauhaeusern-im-vergleich/ · https://www.nomadotravel.app/de/guides/kolsch-beer-guide-cologne · https://www.speisekarte.de/k%C3%B6ln/restaurant/brauwelt_koeln/speisekarte
- 문화: https://en.wikipedia.org/wiki/K%C3%B6lsch_(beer) · https://de.wikipedia.org/wiki/K%C3%B6lner_Stange · https://verliebtinkoeln.com/warum-wird-das-koelsch-in-einem-kranz-gebracht/ · https://www.biergartenkoeln.de/blog/wat-es-en-stange-dein-crashkurs-in-der-koelschen-koelsch-kultur/ · https://www.koelner-kompass.de/blog/der-koebes-warum-koelner-brauhaeuser-anders-funktionieren · https://www.about-drinks.com/vorstand-des-koelner-brauerei-verbandes-bestaetigt/
- 업소별 출처는 JSON의 `sources`에 있다.
