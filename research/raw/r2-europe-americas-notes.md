# r2-europe-americas 조사 노트 (2026-11-07)

담당: 독일 외 유럽·아메리카 음식(이탈리아·스페인/포르투갈·그리스·프랑스·오스트리아·조지아·미국·멕시코·페루·아르헨티나·브라질),
비건 전문점, 미쉐린 스타 파인다이닝. 쾰른 전 지역.

## 1. 결과 요약

- **places 27곳 / candidates 34곳.** WebSearch **30회(상한 30) 모두 사용.**
- **나라 11개 + INT:** 이탈리아 7 · 프랑스 3 · 그리스 3 · 페루 2 · 멕시코 2 · 스페인 1 · 포르투갈/스페인 1 · 미국 1 ·
  아르헨티나 1 · 오스트리아 1 · 조지아 1 · INT(모던 유러피언·파인다이닝) 3 · 비건 중동식 1(나라 미정, `cuisine_region: middle-east`)
- **지역:** ehrenfeld 6 · suedstadt-rheinauhafen 6 · belgisches-viertel 5 · kwartier-lateng 5 · agnesviertel-eigelstein 2 ·
  dom-altstadt 1 · deutz-messe 1 · other 1(닙페스) · **friesenviertel-ehrenstrasse 0(공백)**
- **가격대:** €€€€ 3곳(Ox & Klee, La Société, Pottkind) · €€ 2곳(Grissini, Maspinzelo). 나머지 22곳은 가격 출처가 없어
  `price_level: null`. 저가 쪽은 피자(Spaccanapoli, SORELLINA, Virtuous Pie), 타코(Casita Mexicana 2곳), 버거(Die Fette Kuh),
  비건 중동식(Vegan Food Revolution), 그리스 길거리 음식(Kouzina)이다. 다만 금액으로 확인한 것은 아니다.
- **미쉐린:** ★★ Ox & Klee, ★ La Société·Pottkind(2026 별은 1차 조사의 교차 검증 목록 기준), 빕 구르망 Capricorn [i] Aries
  Brasserie(연도 미확인), 셀렉티드 Christoph Paul's.

## 2. 방법과 숫자 규칙

- 검색 도구가 원문 스니펫이 아니라 **요약문**을 돌려준다. 그래서 `allowed_domains`를 wanderlog.com·restaurantguru.com으로 좁히고,
  쿼리 하나에 가게 1–2곳을 넣어 "Google rating number of reviews / street address postcode"를 명시적으로 물었다.
- **Wanderlog:** 상세 페이지는 "Review score 4.x … N reviews From Google"이라고 명시한다. 목록 페이지는 "4.7 (957) • 4.5 (686)"처럼
  두 점수를 보여 주며, 앞쪽이 구글이다(The ASH·Il Bagutta 요약에서 앞=Google, 뒤=다른 플랫폼으로 확인).
- **Restaurant Guru:** "Google (4.9/5) 773"처럼 구글 수치가 따로 표시될 때만 썼다. 사이트 자체 점수(예: 4.8/3,635)는 쓰지 않았다.
- **스냅샷마다 수치가 다를 때:** 리뷰 수가 가장 많은 스냅샷(가장 최근일 가능성이 큼)을 채택하고, 나머지는 `rating_source`나 `tips_ko`에 적었다.
- 요약이 "약 4.5, 약 1,200"처럼 **반올림해 준 숫자는 쓰지 않았다**(→ candidates). 해당: Black Angus XL, Steakhouse Ponchos,
  Colina, El Gaucho, Casona Argentina.
- 기준 시점이 표시된 출처가 없어 `google_as_of`는 전부 null이다. 그래서 confidence는 대부분 medium이다.
  Spaccanapoli만 high(구글 5점 분포까지 표시, 주소 2개 출처 일치).
- 주소는 이번 세션의 출처에서 번지와 우편번호까지 확인했다. 예외는 아래 두 곳으로, 우편번호를 1차 조사 기록에서 가져왔다.
  - Gusto Antico: 번지는 이번에 Restaurant Guru 메뉴 페이지 제목으로 확인. 우편번호 50825는 1차 기록(Mit Vergnügen).
  - Etrusca: 우편번호 50674는 1차 기록(Mit Vergnügen 2024).

## 3. 나라별로 찾은 것

| 나라 | places | 메모 |
|---|---|---|
| 이탈리아 | Pizzeria Spaccanapoli 4.7 (644) · SORELLINA 4.7 (542) · Virtuous Pie 4.8 (794) · Gusto Antico 4.9 (773) · Etrusca 4.7 (459) · CARUSO Pastabar 4.7 (957) · Grissini 4.3 (1,694) | Nonna Napoli는 지점을 특정하지 못해 후보로 남김. Made In Napoli는 4.7 (1,844)인데 우편번호만 빠짐 |
| 프랑스 | Petit Frère 4.9 (253) · Capricorn [i] Aries Brasserie 4.6 (277) · La Société ★ 4.7 (454) | Le Moissonnier Bistro(★)는 구글 수치 미확인 |
| 그리스 | Kouzina 4.4 (917) · Diogenis 4.4 (619) · Jamas 4.5 (426) | Sophias 4.7 (644)·Plomari 4.7 (552)는 주소 미확인. Ouzeria·Phaedra는 못 찾음 |
| 스페인·포르투갈 | Tapeo & Co. 4.5 (2,336) · TapaVinho 4.5 (333) | Salera 4.7 (571)은 주소 미확인, Manuela 4.4 (851)는 번지 미확인 |
| 페루 | Tigermilch 4.5 (1,059) · El Inca 4.6 (1,772) | Miguelitos는 수치 없음 |
| 멕시코 | Casita Mexicana Südstadt 4.5 (2,338) · Casita Mexicana "Belgisches Viertel" 4.4 (1,175) | 이름과 달리 Roonstraße 88이라 kwartier-lateng으로 분류. Tony's Tacos는 폐업, Tacos Los Carnales는 이동식 트럭 |
| 미국 | Die Fette Kuh 4.4 (6,103) | Bunte Burger는 Wanderlog '영구 폐업'. The ASH 2곳은 기준 미달(4.0, 3.9) |
| 아르헨티나 | El Chango 4.5 (1,929) | 나머지 스테이크하우스 5곳은 숫자가 반올림돼 후보 |
| 오스트리아 | Essers Gasthaus 4.4 (565) | 와인 리스트 수상은 한 출처뿐 |
| 조지아 | Maspinzelo 4.8 (783), 1인 €20–30 | Tamada는 구글 4.3이지만 리뷰 수 없음. badagi는 수치 없음 |
| 브라질 | 없음 | Pantanal Rodizio는 수치·주소 없음. Maracanã Rodizio는 폐업 표시 |
| INT·비건 | Christoph Paul's 4.9 (223) · Ox & Klee ★★ 4.6 (623) · Pottkind ★ 4.7 (325) · Vegan Food Revolution 4.7 (531) | La Cuisine Rademacher 4.8 (399, ★)는 주소가 상충해 후보 |

검증 요청 목록 26곳 가운데 places로 확정한 곳은 17곳이다: Spaccanapoli, SORELLINA, Gusto Antico, Etrusca, Virtuous Pie, CARUSO,
Petit Frère, Tigermilch, Vegan Food Revolution, Fette Kuh, Grissini, Christoph Paul's, Essers, Capricorn, Ox & Klee, La Société, Pottkind.
(Nonna Napoli 2곳은 한 항목으로 셌다.)
나머지는 후보로 남겼다.
- 수치 미확인: Belgischer Hof, Esszimmer, Phaedra, Ouzeria, Alfredo, Borsalino
- 폐업: Bunte Burger
- 기준 미달: The ASH MesseCity
- 지점 불명: Nonna Napoli 2곳

## 4. 의심스러운 점

1. **Ox & Klee:** Wanderlog 상세 페이지는 4.6 (623, "From Google")이다. 같은 사이트 목록은 4.8 (593·600), Restaurant Guru는 4.8 (586)이다.
   규칙대로 리뷰 수가 가장 많은 4.6/623을 썼다. 23개 늘면서 0.2점 떨어진 것은 이례적이니 구글에서 재확인이 필요하다.
2. **Casita Mexicana Südstadt:** Restaurant Guru의 구글 표기는 4.5 (2,338), Wanderlog는 4.3 (2,256)이다. 어느 쪽이든 기준은 넘는다.
3. **Christoph Paul's:** 스냅샷별로 4.7 (177)부터 4.9 (223)까지다. 영업 요일도 출처마다 다르다.
4. **Petit Frère:** 2026년 기사에서는 확인하지 못했다(2024 Mit Vergnügen, Wanderlog). 폐업 신호는 없다.
5. **Capricorn [i] Aries Brasserie의 빕 구르망**은 미쉐린 쾰른 페이지에 연도 표시가 없다(1차 조사). awards에는 연도 없이 넣었다.
6. **CARUSO Pastabar:** 2023년 빕 구르망(hogapage) 기록만 있다. 현재 표시는 미확인이라 awards에 넣지 않고 tips에만 적었다.
7. **Vegan Food Revolution:** Wanderlog에는 'Vegan Revolution'으로 올라 있다. 중동식(후무스·팔라펠)이지만 어느 나라인지 몰라
   `cuisine_country`는 비우고 `cuisine_region`만 middle-east로 넣었다. 작성 시점에 r2-middle-east-africa.json과 겹치지 않았다.
8. **Kouzina:** category를 restaurant로 넣었지만 streetfood(임비스형)일 수도 있다.
9. **Tigermilch:** tablejourney에 브런치 페이지가 있지만 실제 브런치 영업은 확인하지 못해 meals를 비웠다.
10. **La Cuisine Rademacher:** Wanderlog는 Dellbrücker Hauptstraße 176, 1차 조사(사전지식)는 Dellbrücker Mauspfad 482다. 주소 확인 전까지 후보.
11. **Grissini:** Restaurant Guru URL이 'Regency-Club-Cologne'이다. 같은 호텔(하얏트 리젠시) 다른 업장의 페이지를 이름만 바꿨을 수 있으나,
    Wanderlog의 'Grissini Restaurant & Terrasse'(4.3/1,587, 같은 주소)와 일치해 채택했다.
12. facet(meals·occasions·features·drinks·vibe)은 출처가 말한 것만 넣었다. 그래서 비어 있는 칸이 많다. reservation·payment는
    근거가 있는 곳만 채웠다: Spaccanapoli 예약 권장, SORELLINA 카드 전용, Vegan Food Revolution 현금만.

## 5. import 관련 (리드 확인 필요)

- 이름이 같은 1차 candidates는 import 때 자동으로 빠진다. 해당: Christoph Paul's, Tigermilch, Petit Frère, SORELLINA, Essers,
  Gusto Antico, Pizzeria Spaccanapoli, Vegan Food Revolution, La Société, Etrusca, Ox & Klee, Pottkind, Capricorn.
- **이름이 달라 자동으로 빠지지 않는 1차 candidates는 수동 삭제가 필요하다:**
  - "Fette Kuh" → Die Fette Kuh
  - "Grissini Restaurant" → Grissini Restaurant & Terrasse
  - "Virtuous Pie" → Virtuous Pie – Vegane Pizza
  - "Nonna Napoli Ehrenfeld" → 내 후보 "Nonna Napoli (Ehrenfeld)"
- **candidates 중복 제거는 파일 이름순으로 먼저 나온 것을 남긴다(fnb-* → r2-*).** 그래서 아래 항목은 1차의 낡은 정보가 남고
  이번 갱신 내용이 가려진다. r2 쪽 정보를 우선해 주세요.
  - Bunte Burger: **영구 폐업 표시**
  - The ASH Köln MesseCity: **기준 미달 4.0/1,419**, 주소 확인
  - Nonna Napoli (Zülpicher Straße), Belgischer Hof, Ouzeria, Phaedra, Alfredo, Borsalino, Esszimmer Köln
- `scripts/import_raw.py --dry-run`에서 이 파일 관련 경고는 0건이었다.

## 6. 범위 밖이지만 본 것 (다른 담당 참고)

- 독일 파인다이닝 maiBeck: Am Frankenturm 5, 50667 · 4.7 (438). 독일 요리라 제외.
- Maximilian Lorenz(Johannisstraße 64, ★)와 Zur Tant(Porz, ★)는 구글 리뷰 수 미확인.
- 기타 이탈리아·그리스·프랑스·스페인
  - TUTTO(이탈리안 뷔페): 4.2 (3,607), 주소 없음
  - Katerina's Greek Taverne 4.3 (535), Grill Korfu 4.7 (376): 둘 다 주소 없음
  - Brasserie Marie: 4.0, 기준 미달
  - Meson El Cordobes(Gladbacher Str. 11, 50672): 수치 없음
  - Hans im Glück Am Ring: 체인이라 제외
- 아시아·중동·카페
  - DAIKAN IZAKAYA(Maastrichter Str. 9, 50672): 일식
  - Der Libanese(Venloer Str.): spinach 4.5 (195)
  - Chum Chay 4.6 (1,866), Hanse Stube 4.5 (393)
  - prôt von Alex(Lütticher Str. 6, 50674): 4.8 (552), 베이커리

## 7. 사용한 검색 30회

1. Wanderlog best Italian restaurants Cologne Google rating reviews address pizza
2. werkenntdenbesten Pizzeria Köln Ehrenfeld google.de … Nonna Napoli Spaccanapoli Gusto Antico
3. (spinach.guide) Nonna Napoli Köln Venloer Straße Read on Google Maps reviews — 결과 없음
4. (wanderlog) best pizza in Cologne … Nonna Napoli Spaccanapoli Sorellina
5. (wanderlog) Cologne vegan restaurant Bunte Burger Vegan Food Revolution Virtuous Pie
6. "best vegetarian restaurants in Cologne" Wanderlog … — 성과 없음
7. (wanderlog) Petit Frère Tigermilch Belgischer Hof Christoph Paul's … — 성과 없음
8. (wanderlog/restaurantguru/werkenntdenbesten) Ox & Klee Köln Google rating reviews Im Zollhafen
9. (wanderlog) "best places for steak in Cologne" Argentinian steakhouse The ASH
10. (wanderlog) "best Latin and South American foods and restaurants in Cologne" …
11. (wanderlog) "fine dining in Cologne" La Société Pottkind Esszimmer Alfredo Capricorn
12. (wanderlog) "Michelin star restaurants in Cologne" Neobiota Maximilian Lorenz Sahila La Société
13. (wanderlog) "best French restaurants and bistros in Cologne" Petit Frère Capricorn Belgischer Hof
14. (wanderlog) "best Greek restaurants in Cologne" Ouzeria Phaedra mezze
15. (wanderlog) "best tapas" OR "Spanish restaurants" in Cologne Portuguese
16. (wanderlog) "best burgers in Cologne" Fette Kuh Bunte Burger
17. (wanderlog) "best places for pasta in Cologne" Caruso Etrusca Borsalino Nonna Napoli Gusto Antico
18. (wanderlog/restaurantguru) SORELLINA 주소; Spaccanapoli 주소
19. (wanderlog/restaurantguru) Tigermilch 주소; El Inca 주소
20. (wanderlog/restaurantguru) TapaVinho 주소; Tapeo & Co 주소
21. (wanderlog/restaurantguru/werkenntdenbesten) georgisches Restaurant Köln Khachapuri Khinkali
22. (wanderlog/restaurantguru) El Chango; Colina; El Gaucho 정확한 구글 수치 — El Chango만 결과
23. (wanderlog/restaurantguru) Die Fette Kuh 구글 수치; Vegan Revolution 주소
24. (wanderlog/restaurantguru) Essers Gasthaus; Maspinzelo — Essers만 결과
25. (wanderlog/restaurantguru) Christoph Paul's; Colina — Christoph Paul's만 결과
26. (wanderlog/restaurantguru) Nonna Napoli Venloer Str. 248; Gusto Antico
27. (wanderlog/restaurantguru) Grissini Deutz; The ASH MesseCity
28. (wanderlog/restaurantguru) Maspinzelo; Tamada — Maspinzelo만 결과
29. (wanderlog/restaurantguru) Casita Mexicana; Tony's Tacos
30. (wanderlog/restaurantguru) Ristorante Etrusca; Virtuous Pie

## 8. 주요 출처

- Wanderlog 목록
  - 이탈리안: https://wanderlog.com/list/geoCategory/52853/best-italian-restaurants-in-cologne
  - 파스타: https://wanderlog.com/list/geoCategory/1799196/best-places-for-pasta-in-cologne
  - 프렌치: https://wanderlog.com/list/geoCategory/45713/best-french-restaurants-and-bistros-in-cologne
  - 남미: https://wanderlog.com/list/geoCategory/799541/best-latin-and-south-american-foods-and-restaurants-in-cologne
  - 그리스: https://wanderlog.com/list/geoCategory/786948/best-greek-foods-and-restaurants-in-cologne
  - 타파스: https://app.wanderlog.com/list/geoCategory/1825451/best-places-for-tapas-in-cologne
  - 스페인: https://wanderlog.com/list/geoCategory/804938/best-spanish-foods-and-restaurants-in-cologne
  - 스테이크: https://wanderlog.com/list/geoCategory/1503221/best-steaks-in-cologne
  - 미쉐린: https://wanderlog.com/list/geoCategory/59993/michelin-star-restaurants-in-cologne
  - 멕시칸: https://wanderlog.com/list/geoCategory/776154/best-mexican-foods-and-restaurants-in-cologne
- Wanderlog 상세: 각 place의 `sources` 첫 줄
  - 예: https://wanderlog.com/place/details/6228856/spaccanapoli-k%C3%B6ln
  - 예: https://wanderlog.com/place/details/1140610/oxklee
- Restaurant Guru 상세(구글 표기)
  - https://restaurantguru.com/Gusto-Antico-Cologne
  - https://restaurantguru.com/Regency-Club-Cologne
  - https://restaurantguru.com/Essers-Gasthaus-Cologne
  - https://restaurantguru.com/Casita-Mexicana-Cologne
  - https://restaurantguru.com/Ox-and-Klee-Cologne-2
- 미쉐린 2026(1차 조사 교차 검증)
  - https://koeln.mitvergnuegen.com/2026/sterne-restaurants/
  - https://guide.michelin.com/de/de/article/michelin-guide-ceremony/alle-sternerestaurants---michelin-guide-deutschland-2026
- 1차 조사 출처(영업시간·설명): Mit Vergnügen 2024–2026 지역 목록, koeln.de, speisekarte.de, tablejourney, foodle.pro, Schlemmer-Atlas
