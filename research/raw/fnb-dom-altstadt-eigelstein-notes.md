# fnb-dom-altstadt-eigelstein — 조사 노트 (2026-11-07)

범위: `dom-altstadt` + `agnesviertel-eigelstein`의 식음료(레스토랑·브라우하우스·카페·베이커리·디저트·스트리트푸드, 바 제외).

## 0. 상태 요약 (먼저 읽을 것)

- **미완성.** 목표는 28–32곳이었지만 확정(places)은 3곳뿐이다. 후보(candidates)는 27곳이다.
- 원인:
  - **WebFetch는 차단됨.** `werkenntdenbesten.de`가 ENOTFOUND로 실패했다(브리프대로 1회만 시도).
  - **WebSearch는 19회 성공한 뒤 공유 한도에 걸림.** 한도는 턴당 200회이고 모든 에이전트가 합산해서 쓴다. 도구가 "다시 검색하지 말 것"이라는 메시지와 함께 거부해서 조사를 중단했다.
- 확정 3곳은 모두 구시가 브라우하우스다. 범위의 나머지는 **아직 전혀 조사하지 못했다**: 카페·베이커리·아침, 중앙역 근처 캐주얼·인터내셔널, 파인다이닝, 아이겔슈타인·아그네스 지구 전체.
- 확정 3곳의 `price_level`은 **null**로 두었다. 이번 세션에서 메뉴나 구글 1인 가격 출처를 찾지 못했기 때문이다. 병합 전에 채우거나 null 허용 여부를 정해야 한다.
- `must_try`에는 출처로 확인한 각 집의 쾰시만 넣었다. 요리는 메뉴 출처가 없어서 비워 두었다.

## 1. 지역 분위기

> 표시가 없는 서술은 일반 지식이다(이번 세션에서 출처로 확인하지 않음). **[출처]** 표시는 이번 세션 검색 결과로 확인한 내용이다.

### dom-altstadt (대성당·구시가)
- **대성당·중앙역**: 도시 최대의 관광 허브다. 중앙역 정문 앞(Bahnhofsvorplatz 1)에 Gaffel am Dom이 있다 **[출처: koeln.de]**. 대성당 남쪽 Am Hof에는 FRÜH am Dom이 있다. 그래서 기차에서 내리자마자 쾰시를 한 잔 할 수 있다. 대신 대성당 바로 앞 업소들은 관광객 위주라 후기 편차가 크다(FRÜH am Dom의 2026년 후기 참고) **[출처: Tripadvisor]**.
- **구시가**(Alter Markt·Heumarkt·Salzgasse·Fischmarkt·Martinsviertel): 대성당과 라인강 사이 좁은 골목에 전통 브라우하우스가 몰려 있는 '브라우하우스 밀집 지대'다. Peters, Sion, Gaffel Haus/Zum Prinzen, Malzmühle, Sünner im Walfisch 등이 있다. 라인강변(Frankenwerft)에는 테라스 식당이 줄지어 있다.
- **Hohe Straße·Schildergasse~Neumarkt**: 보행자 쇼핑가로 체인점이 대부분이다. 제대로 된 식사보다 카페나 간단한 끼니에 맞는 곳이다.
- **언제 갈까**: 브라우하우스는 평일 늦은 오후~이른 저녁이 비교적 덜 붐빈다. 토요일 밤과 카니발 기간에는 구시가 전체가 인파로 꽉 찬다. 특히 11월 11일 11시 11분 시즌 개막일과 2월 거리 카니발이 그렇다. 여행 시점이 11월이라 11/11과 크리스마스 마켓 시즌에 Alter Markt·Heumarkt가 매우 붐빌 수 있다는 점을 일정에 반영할 것. 마켓 날짜는 미검증이다.

### agnesviertel-eigelstein (아그네스 지구·아이겔슈타인)
- **Eigelstein**: 중앙역 북쪽에서 중세 성문 Eigelsteintorburg까지 이어지는 거리다. 터키·중동계 식료품점과 식당, 오래된 쾰시 선술집(Em Kölsche Boor, Weinhaus Vogel 등)이 섞인 다문화적이고 서민적인 분위기다.
- **Ursula·Kunibertsviertel**(중앙역 북쪽~라인강): 호텔이 많고 조용하다. Schreckenskammer(St. Ursula 근처), Max Stark 같은 동네 브라우하우스가 있다.
- **Agnesviertel·Neustadt-Nord**: 19세기 신시가지 주거지다. St. Agnes 성당 주변과 Neusser Straße 일대에 카페와 비스트로가 많은 '현지인 동네'라 관광객이 적다.
- **Ebertplatz**: 교통 결절점이다. 다소 거친 이미지가 있지만 광장 지하 통로에 예술 공간들이 있다.
- **언제 갈까**: 저녁 식사나 주말 아침·브런치에 맞다. 중앙역에서 걸어갈 수 있어 '관광객 없는 쾰른'을 보기 좋다.
- 이 지역 업소는 **한 곳도 검증하지 못했다**(아래 후보 목록 참고).

## 2. 확정 장소 (places, 3곳)

| 이름 | 주소 | Google | 출처·기준시점 | 신뢰도 | 메모 |
|---|---|---|---|---|---|
| Peters Brauhaus | Mühlengasse 1, 50667 | 4.4 (8,395) | werkenntdenbesten.de, Stand 2026-05-30 | high | spinach.guide 4.4 (8,379)와 일치. TripAdvisor 3.9 (2,338) |
| FRÜH am Dom | Am Hof 12-18, 50667 | 4.3 (19,851) | restaurantguru.com, 날짜 없음 | medium | werkenntdenbesten 5개 포털 종합 4.22 (28,843). 오래된 리스트에도 4.3(~15,000). 2026년 9월까지 후기 극과 극(서비스·위생 불만 포함) |
| Brauerei zur Malzmühle | Heumarkt 6, 50667 | 4.2 (2,584) | spinach.guide, 날짜 없음 | medium | restaurantguru는 Google 4.3 (2,378), 페이지 약 755일 전. spinach 쪽 리뷰 수가 많아 더 최신으로 보고 채택. **기준선(4.2) 경계** |

## 3. 후보 / 미검증 (candidates, 27곳) — 후속 조사 우선순위

**A. 수치는 일부 찾았지만 판단이 보류된 곳**
1. **Gaffel am Dom** (Bahnhofsvorplatz 1). 두 출처가 충돌한다.
   - spinach.guide: 3.5 (9,701). 리뷰 수가 더 많아 더 최신으로 보이며, 기준 미달이다.
   - restaurantguru: Google 4.3 (8,716). 페이지는 약 554일 전 것이다.
   - 같은 구글 목록이라면 두 값은 산술적으로 양립할 수 없다. 실시간 확인이 필요하고, 확인되면 중앙역 앞이라 꼭 넣을 만하다.
2. **Brauhaus Sion** (Unter Taschenmacher 5-7). 이 주소와 확실히 연결되는 구글 수치를 못 찾았다. restaurantguru의 'Sion Bräues Traditionsbrauhaus' Google 4.2 (409)는 주소가 확인되지 않았고, 대형 브라우하우스치고 리뷰 수가 지나치게 적다.
3. **Sünner im Walfisch** (Salzgasse 13, 주소 미검증). 오래된 랭킹 요약에 Google 4.4만 있고 리뷰 수는 없다.
4. **FRÜH "Em Jan von Werth"**. restaurantguru Google 4.4 (1,163)로 기준은 충족하지만, 주소와 지역을 확인하지 못했다.
5. **Café-Lounge Alter Markt 55**. Google 4.5이지만 리뷰 수가 표시되지 않았다.
6. **Gilden Brauhaus (Gilden im Zims?, Heumarkt 77)**. werkenntdenbesten 종합 4.28 (14,185건/9개 포털)이 있지만 어느 업소 수치인지 불확실하고, 구글 단독 수치는 없다.
7. **Brauerei zum Pfaffen** (Heumarkt 62, 미검증). 리스트에 4.7만 있고 리뷰 수와 출처 페이지가 불명확하다.
8. **Gaffel Haus / Brauhaus zum Prinzen** (Alter Markt 20-22). 구글 수치가 없다. 같은 주소에 두 이름이 쓰인다.
9. **Gertrudenhof am Neumarkt**. verliebtinkoeln 독자 투표 1위라는 것만 확인했다. 업소 성격과 주소는 모른다.

**B. 기준 미달로 확인된 곳 (below-criteria)**
- Sion am Bahnhof (Dompropst-Ketzer-Straße 1): Google 4.1 (255)
- Alter-Markt-Treff (Alter Markt 18): Google 3.9 (80)

**C. 시드 중 전혀 조회하지 못한 곳.** 주소는 사전지식이며 JSON에 미검증으로 표시했다.
- dom-altstadt: Bierhaus en d'r Salzgass, Haxenhaus zum Rheingarten, Café Reichard, Hanse Stube(Excelsior Hotel Ernst), Sahila(Kämmergasse, Neumarkt 남쪽이라 지역 경계도 확인 필요), Alfredo. Wartesaal am Dom과 LOUIS Cafe am Dom은 restaurantguru 페이지가 있다는 것만 확인했다.
- agnesviertel-eigelstein: Schreckenskammer, Em Kölsche Boor, Max Stark, Weinhaus Vogel, Sion an der Agneskirche, Maximilian Lorenz, Astrein, Le Moissonnier. 마지막 세 곳은 영업 상태(폐업·이전)를 반드시 먼저 확인해야 한다.

**D. 아직 검색조차 못 한 카테고리 (후속 아이디어, 전부 미검증)**
- 대성당·중앙역 근처 아침·커피·캐주얼(빠른 한 끼), 전통 카페(Café Eigel 등)
- 구시가·라인강변 고급 레스토랑(Maibeck, Em Krützche 등)
- 아이겔슈타인 터키·중동 식당, 아그네스 지구 동네 비스트로·카페·베이커리, 디저트·젤라토

## 4. 제외 (폐업·이전)
- 이번 세션에서 폐업이나 이전을 **확인한** 곳은 없다. Le Moissonnier, Maximilian Lorenz, Astrein은 상태를 확인하지 못했다. 확인 전까지 가이드에 넣지 말 것.
- 참고: Lebensmittelzeitung에 따르면 Malzmühle가 Sünner 양조장을 인수하고 Heumarkt의 생산을 Kalk로 옮긴다(기사 날짜 미확인). Heumarkt 브라우하우스는 malzmuehle.de의 2026년 8월 채용공고 PDF로 보아 영업 중이다.

## 5. Kölsch & Brauhaus 문화

### 5.1 이번 세션 출처로 확인한 사실
- **Brauhaus Sion** [koeln.de]
  - 1318년부터 이 자리에서 맥주를 빚었다.
  - 'Sion-Kölsch'라는 이름은 1936년부터 쓰였다.
  - 2차 대전 때 파괴됐고 1953년에 다시 문을 열었다.
  - 가장 큰 홀 'Alte Brauerei'는 최대 200명을 수용한다. 음식은 든든한 향토식이고 채식 메뉴도 있다.
- **Gaffel Haus**는 알터 마르크트에서 가장 오래된 건물로 소개된다. 같은 주소를 Gaffel이 1987년 'Brauhaus zum Prinzen'으로 다시 열었다 [arrivalguides].
- **Gaffel am Dom**은 대성당과 중앙역 정문 바로 맞은편, Bahnhofsvorplatz 1에 있다 [koeln.de].
- **FRÜH am Dom**: Fodor's는 '대성당 그늘 아래의 유서 깊은 옛 양조장'으로 소개한다 [tripexpert]. 2026년 9월까지의 Tripadvisor 후기는 테라스 쾰시를 호평하는 글과 서비스·위생(쥐 목격)을 비판하는 글로 갈린다 [tripadvisor].
- **Peters Brauhaus** 후기에는 쾨베스(Köbes)의 서빙이 '경험의 일부'라는 언급이 많고, 관광객이 많다는 지적도 있다 [werkenntdenbesten/spinach 요약].
- **Malzmühle**는 자체 브랜드 Mühlen Kölsch를 빚는다 [beertasting.com]. Sünner 양조장 인수와 생산의 Kalk 이전 보도가 있다 [Lebensmittelzeitung].
- **인기 순위** [verliebtinkoeln, 22places]
  - verliebtinkoeln 독자 투표(비대표): 1위 Gertrudenhof am Neumarkt, 이어서 Lommerzheim·Päffgen. Schreckenskammer, FRÜH am Dom, Malzmühle도 올라 있다.
  - 2026년 7월 업데이트된 Top 10(22places로 추정): Früh em Veedel·Hellers·Päffgen이 상위이고, Sünner im Walfisch·Peters·Malzmühle가 뒤따른다.

### 5.2 브라우하우스별 쾰시 브랜드
| 브라우하우스 | 쾰시 | 근거 |
|---|---|---|
| FRÜH am Dom (+ FRÜH "Em Jan von Werth", "Em Veedel") | Früh Kölsch | beeradvocate 'Brauerei Früh am Dom / Früh Kölsch', restaurantguru 상호 |
| Peters Brauhaus | Peters Kölsch | 리뷰 요약 (werkenntdenbesten/spinach) |
| Brauerei zur Malzmühle | Mühlen Kölsch | beertasting.com, mdwiki 'Mühlen Kölsch' |
| Brauhaus Sion / Sion am Bahnhof / Sion an der Agneskirche | Sion Kölsch | koeln.de (Sion-Kölsch 명칭) |
| Gaffel am Dom / Gaffel Haus (Brauhaus zum Prinzen) | Gaffel Kölsch | koeln.de, arrivalguides(1987 Gaffel 재개업) |
| Sünner im Walfisch | Sünner Kölsch | 상호 기준 추정 + Lebensmittelzeitung(Sünner 양조장) |
| Gilden Brauhaus | Gilden Kölsch | 상호 기준 추정, 미검증 |

### 5.3 출처 미확보 — 일반 지식 초안 (검증한 뒤에 쓸 것)
> 아래는 이번 세션에서 출처를 찾지 못한 내용이다. 숫자(가격·연도)는 일부러 넣지 않았다.
- **Köbes(쾨베스)**: 브라우하우스의 전통 웨이터다.
  - 파란 상의와 앞치마, 허리에 찬 가죽 지갑이 상징이다.
  - 무뚝뚝하고 짓궂은 농담이 전통의 일부다.
  - 주문하지 않아도 잔이 비면 새 쾰시를 가져온다.
  - 이름은 Jakob의 쾰른 방언형이다.
- **Stange(슈탕에)**: 쾰시 전용 가는 원통형 잔이다. 표준 용량 0.2 l은 과제 설명에 명시된 값이다. 작은 잔을 빨리 비우는 방식이라 맥주가 늘 차갑고 신선하다.
- **Kranz(크란츠)**: 쾨베스가 들고 다니는 원형 쟁반이다. 가운데 손잡이가 있고 잔 구멍이 뚫려 있어 여러 잔을 한 번에 나른다.
- **코스터(Bierdeckel) 에티켓**:
  - 쾨베스는 잔을 놓을 때마다 코스터에 연필로 줄을 그어 잔 수를 센다. 계산은 이 줄로 한다.
  - **그만 마시려면 빈 잔 위에 코스터를 덮는다.** 덮지 않으면 계속 새 잔이 온다.
- **2026년 쾰시 1잔 가격**: **미확인.** 출처를 확보하지 못했다. 후속 조사에서 Express나 KStA의 쾰시 가격 기사로 확인할 것.
- **대표 요리**
  - **Halve Hahn(할베 한)**: 직역하면 '닭 반 마리'지만 닭이 아니다. 호밀빵(Röggelchen)에 두툼한 숙성 고다 치즈와 겨자, 생양파를 얹은 쾰시 안주다.
  - **Himmel un Ääd(힘멜 운 애드)**: '하늘과 땅'이라는 뜻이다. 사과(하늘)와 감자(땅)를 으깬 퓌레에 구운 블러드소시지(Flönz)와 볶은 양파를 곁들인다.
  - **Rievkooche / Reibekuchen(리브코헤)**: 간 감자를 납작하게 튀긴 감자전이다. 사과퓌레(Apfelmus)나 사탕무 시럽(Rübenkraut), 호밀빵과 함께 낸다. 금요일 메뉴로 내는 집이 많다.
  - **(Rheinischer) Sauerbraten(자우어브라텐)**: 식초·와인 마리네이드에 며칠 재운 고기를 졸인 찜이다. 라인란트식은 건포도가 들어간 새콤달콤한 소스가 특징이다. 원래 말고기였고 지금은 대개 소고기다(메뉴의 'vom Pferd' 표기 확인). 감자 크뇌델과 적양배추(Rotkohl)를 곁들인다.
  - **Flönz(플뢴츠)**: 쾰른식 블러드소시지(Blutwurst)다. 'Kölsche Kaviar'는 Flönz에 생양파와 호밀빵을 곁들인 것이다.
  - **Haxe / Hämchen(학세 / 헴헨)**: Schweinshaxe는 겉을 바삭하게 구운 돼지 정강이다. Hämchen은 염장한 뒤 삶은 쾰른식 돼지 정강이로, 자우어크라우트·으깬 감자와 함께 나온다. 둘 다 양이 매우 많다.
  - **Mettbrötchen(메트브뢰첸)**: 양념한 생 돼지고기 다짐육(Mett)을 빵에 바르고 생양파를 얹은 것이다. 날고기라는 점을 안내할 것.

## 6. 검색 기록 (19회 성공 + WebFetch 1회 실패)
- 일반 검색(standard):
  - "Früh am Dom Köln Google Bewertungen werkenntdenbesten"
  - "Gaffel am Dom Köln Bahnhofsvorplatz Google Bewertung"
  - "Peters Brauhaus Köln Mühlengasse Google Bewertungen"
  - "\"Früh am Dom\" google.de Bewertungen Am Hof 12"
  - "Brauhaus Sion Unter Taschenmacher Köln werkenntdenbesten google.de"
  - "Brauerei zur Malzmühle Heumarkt Köln Google Bewertungen"
  - "Gaffel Haus Alter Markt Köln Google Bewertungen"
  - top-rated.online / wanderlog 질의 각 1회
- 정밀 검색(extended):
  - werkenntdenbesten Früh am Dom
  - werkenntdenbesten Malzmühle
  - "beliebteste Brauhäuser Köln Google-Bewertungen Ranking 2026"
- `allowed_domains=werkenntdenbesten.de`: Früh am Dom, Malzmühle
- `allowed_domains=restaurantguru.com`: Früh am Dom, Gaffel am Dom, Brauhaus Sion, Malzmühle, Gaffel Haus
- 실패: spinach.guide 3건(검색 한도 소진). WebFetch werkenntdenbesten.de는 ENOTFOUND.

## 7. 의문점 / 주의
- **restaurantguru 수치는 오래됐을 수 있다.** 페이지 나이가 약 554~755일로 표시된 곳이 있다. FRÜH am Dom은 날짜가 아예 없어서 `google_as_of`를 null로 두었다.
- **Malzmühle은 기준선(4.2) 경계다.** 리뷰 2,584건도 이 규모 업소치고 적어 보인다. 구글 목록이 둘 이상일 수 있다.
- **Gaffel am Dom은 출처 충돌로 보류했다**(위 3-A-1).
- **검색 요약이 업소를 섞는 경우가 있었다.** 예를 들어 werkenntdenbesten 요약이 Heumarkt 77의 수치를 Früh am Dom에 붙였다. 확정 3곳은 업소별 페이지(Peters)나 업소명이 들어간 페이지(Früh, Malzmühle) 수치만 썼다.
- **대부분 후보의 주소는 사전지식이다.** 지오코딩 전에 반드시 확인할 것.

## 8. 범위 밖이지만 알아두면 좋은 발견 (다른 에이전트용, 미검증 포함)
- FRÜH "Em Veedel": restaurantguru Google 4.6 (1,230). 쥐트슈타트로 알려져 있음(미검증).
- Peters am Hahnentor: Rudolfplatz에 새로 연 Peters 브라우하우스 [koeln.de 'Prost am Rudolfplatz'].
- Lommerzheim(Deutz) 4.7(~3,900), Brauhaus Quetsch 4.7: 랭킹 리스트 요약에서 나왔고 날짜와 출처가 불명확하다.
- Reissdorf am Griechenmarkt: 오래된 리스트에 4.4.
- Haus Sion im Schäfer: restaurantguru Google 4.6 (448), 위치 미확인.

## 9. 주요 출처
- https://www.werkenntdenbesten.de/e/28017932/brauerei/koeln/peters-brauhaus-bruno-haumann-gf-bewertungen.html
- https://spinach.guide/venues/peters-brauhaus-23831/
- https://restaurantguru.com/Fruh-am-Dom-Cologne-2
- https://www.werkenntdenbesten.de/e/50856596/internationales-restaurant/koeln/frueh-am-dom-bewertungen.html
- https://www.tripadvisor.com/Restaurant_Review-g187371-d7235024-Reviews-Fruh_am_Dom-Cologne_North_Rhine_Westphalia.html
- https://www.tripexpert.com/cologne/restaurants/fruh-am-dom
- https://spinach.guide/venues/brauerei-zur-malzmuhle-33208/
- https://de.restaurantguru.com/Brauerei-zur-Malzmuhle-Cologne
- https://www.lebensmittelzeitung.net/industrie/nachrichten/koelsch-hersteller-malzmuehle-schluckt-suenner-brauerei-161790
- https://malzmuehle.de/wp-content/uploads/2026/08/Hausmeister-Schreiner_Stellenausschreibung_2026.pdf
- https://beertasting.com/en/beers/muhlen-kolsch
- https://restaurantguru.com/Gaffel-am-Dom-Cologne
- https://spinach.guide/venues/gaffel-am-dom-34330/
- https://www.koeln.de/tourismus/ll/brauhaus-koeln/gaffel-am-dom/
- https://www.koeln.de/tourismus/ll/brauhaus-koeln/brauhaus-sion/
- https://www.arrivalguides.com/de/Travelguide/COLOGNE/dining/gaffel-haus-5084
- https://restaurantguru.com/Brauhaus-Sion-Cologne
- https://verliebtinkoeln.com/beste-brauhaus-koeln/
- https://www.22places.com/cologne-breweries/
- https://www.beeradvocate.com/beer/profile/1450/6356/

## 10. 후속 조사 팁 (다음 턴에서 이어갈 때)
- **가장 효율이 좋았던 방식**: WebSearch에 `allowed_domains=["restaurantguru.com","de.restaurantguru.com"]`를 걸고 "<이름> Cologne Google rating"으로 검색하는 것이다. 'Google (x/5) N'이 바로 나온다. 다만 페이지 나이를 확인해야 한다.
- **기준시점(Stand)까지 필요할 때**: werkenntdenbesten 업소별 페이지에 'google.de x,xx (N)'과 Stand 날짜가 나온다. Peters는 "<이름> Köln <거리명> Google Bewertungen" 질의로 잡혔다.
- **spinach.guide**: Peters 수치가 구글과 일치했다. 교차확인용으로 쓸 만하다.
- **남은 검색량 추정**: 최소 30~40회는 필요하다. 후보 C 목록 18곳, A 목록 재확인 9곳, D 카테고리 신규 발굴, 쾰시 가격·문화 출처 2~3회를 합한 수치다.
