# r2-cafes-dessert — 조사 노트 (2026-11-07)

카페·스페셜티 커피·브런치·베이커리·파티스리·아이스크림·외국식 디저트 조사(2차).
결과: **places 24곳 / candidates 26곳**, WebSearch **20/20회 사용**(상한 도달 후 중단).

## 방법과 수치 원칙

- 구글 수치는 거의 다 **Wanderlog**에서 확보했다. 장소 페이지·리스트는 평점 두 쌍을 보여 준다. 첫 번째(리뷰 수가 큰 쪽)가 Google, 두 번째가 Tripadvisor다. 검색 요약도 여러 번 그렇게 표시했다.
- Wanderlog는 페이지(스냅샷)마다 리뷰 수가 다르다. 기준 시점(`google_as_of`)이 표시되지 않아 모두 `null`로 두었다.
  **리뷰 수가 가장 큰 스냅샷을 최신으로 보고 그 값을 썼다.** 예: Coffee Gang 1,290–1,378 → 1,378, LOUIS 4.5/297 vs 4.4/407 → 4.4/407.
- 예외 1 — Café Feynsinn: Wanderlog는 약 4.2(674–758건, 요약상 근사치)다. 그래서 정확한 값이 있는 gelbeseiten.de 4.2/724를 그대로 썼다.
- 예외 2 — Die Eisdielerin: 수치가 범위(약 4.4–4.5, 약 550–630건)로만 나와 **낮은 쪽 값(4.4/550)**을 적었다. 어느 쪽이든 기준을 충족한다.
- 모든 places는 `confidence: "medium"`이다. Wanderlog를 거친 구글 수치이고 스냅샷이 엇갈리기 때문이다. low로 둔 곳은 없다.
- 주소는 이번 세션 Wanderlog 페이지에서 확인했다. Café Heimisch만 1차 조사 출처(koeln.de, speisekarte 등)와 Wanderlog를 함께 썼다.

## 검색 20회

1. Wanderlog 벨기에 지구 카페(일반) → Café Sehnsucht 4.4(1594)
2. Wanderlog 커피 리스트 → Coffee Gang, Van Dyck, Sehnsucht
3. Wanderlog 아침·브런치 리스트 → Oma Janßen, ST. LOUIS Breakfast, Lint No 7
4. Coffee Gang / Van Dyck / Buur 장소 페이지 → Coffee Gang 주소·수치
5. 카페 리스트(Buur·Belgique·Balthasar·Caprista·Luz·Bauturm·Reichard) → Buur, Reichard, Bauturm, Caprista, Balthasar 주소
6. Hempies / Belgique / Luz / Balthasar → Hempies, Belgique 수치, Balthasar 수치, Luz 없음
7. Van Dyck / Zeit für Brot / Sehnsucht → Van Dyck·Sehnsucht 주소·수치, Zeit für Brot 없음
8. LOUIS / Oma Janßen / Wahlen / Lint No 7 → Oma Janßen만
9. Heimisch / CoffeeIN / Feynsinn → Heimisch, Feynsinn, (CoffeeIN 대신) THE COFFICE DEUTZ
10. Wanderlog 아이스크림·젤라토 리스트 → Ferigo, Eismacher, Eisliebe, Panciera 등
11. 케이크·파티스리 리스트 → Wahlen 주소(수치 없음), Klüppelberg
12. 포르투갈 나타 / 터키 바클라바 → Bom Dia, Darwish, Damla, Damla Ehrenfeld, Tadım Damak
13. 쥐트슈타트(Bom Dia / Eismacher / Cafeteria South) → Bom Dia 폐업 신호, Eismacher, South 3.9
14. 아이스크림 추가(Eisdielerin / Breda / Eisliebe / Panciera) → 주소·수치
15. werkenntdenbesten(Zeit für Brot / Zimmermann) → Zeit für Brot 주소에 다른 업체, Zimmermann 종합 점수만
16. 일본·한국 카페 → PUFU(일본 수플레 팬케이크), 한국 카페는 못 찾음
17. PUFU / Törtchen Törtchen → Törtchen 주소·수치, PUFU 수치
18. Café Belgique / PUFU 주소 → 둘 다 확인
19. LOUIS Cafe am Dom / Lint No 7 → LOUIS 주소·수치, ST. LOUIS Café(도이츠)
20. ST. LOUIS Café / Coffice 우편번호, Lint No 7 주소 → 셋 다 확인

## 검증 요청 17곳 결과

| 업소 | 결과 | 비고 |
|---|---|---|
| The Coffee Gang | ✅ 4.8 / 1,378 | 주소 **Hohenstaufenring 19, 50674**(1차의 Maastrichter Str. 아님). 그래서 지역은 kwartier-lateng |
| Café Buur | ✅ 4.7 / 3,517 | 주소 **Richard-Wagner-Str. 28**(1차의 Maastrichter Str. 아님) |
| Hempies | ✅ 4.8 / 535 | Händelstraße 55. 벨기에 지구/쿼르티어 라텡 경계 |
| Café Luz | ❌ 후보 | Wanderlog에 없음(신규 개업). 'Café Lu'(다른 곳)만 나옴 |
| Café Belgique | ✅ 4.5 / 358 | Brüsseler Platz 16. 12시 오픈 |
| Balthasar | ✅ 4.4 / 1,476 | Aachener Str. 18. 'Café Balthasar' 4.3/904 중복 페이지 있음 |
| Café Caprista | ✅ 4.8 / 1,043 | 수치는 **Venloer Str. 380(에렌펠트)** 지점 기준. 1차의 Flandrische Str. 15 지점은 미확인 |
| Van Dyck (Körnerstr. 43) | ✅ 4.6 / 451 | 리스트의 4.8(265–272)은 뮐하임 로스터리(Schanzenstr. 36)일 가능성 |
| Café Sehnsucht | ✅ 4.4 / 1,689 | 스냅샷 1,594–1,689 |
| Zeit für Brot | ❌ 후보 | Venloer Str. 202에 Fresh Café & Backshop / Die Mehlwerkstatt만 확인 → 폐업·이전 의심 |
| Café Heimisch | ✅ 4.3 / 1,375 | 영업시간 출처별 상이 |
| CoffeeIN | ❌ 후보 | 못 찾음. 대신 THE COFFICE DEUTZ(4.8/245) 등재 |
| Café Reichard | ❌ 후보 | **기준 미달 3.8 / 5,365** |
| Café Feynsinn | ✅ 4.2 / 724 | 기준선. Wanderlog도 약 4.2로 확인돼 1차의 low를 medium으로 올림 |
| Café Bauturm | ❌ 후보 | **기준 미달 4.1 / 774** |
| Bäckerei Zimmermann | ❌ 후보 | Ehrenstr. 75. 구글 단독 수치 없음(werkenntdenbesten 종합 4.80/552) |
| LOUIS Cafe am Dom | ✅ 4.4 / 407 | Kleine Budengasse 1-3. 정오 오픈이라 아침 장소는 아님. €10 미만 카드 불가 |

## 새로 찾은 곳 (지역별)

- **dom-altstadt (대성당 근처 아침 공백 보완):** **Oma Janßen Colonialwarenhandel**(Alter Markt 56, 4.7/694)은 독일식 아침을 내는 식료품점 겸 카페다.
  **Lint No 7**(Lintgasse 7, 4.7/499)은 오전에만 열고 월요일은 쉰다. LOUIS Cafe am Dom은 오후 카페다.
  → 중앙역(Hbf) 바로 앞 아침 장소는 여전히 공백이다(검색에 BackWerk 체인만 나옴).
- **friesenviertel-ehrenstrasse:** 파티스리 **Törtchen Törtchen**(Apostelnstr. 19, 4.5/1,374), 아이스크림 **Eisliebe in der Kettengasse**(Kettengasse 4, 4.9/501).
- **kwartier-lateng:** **ST. LOUIS Breakfast**(Meister-Gerhard-Str. 30, 4.7/3,462)는 리뷰 수로 보면 쾰른 최대급 아침 카페다.
- **deutz-messe:** **ST. LOUIS Café-Köln**(Deutzer Freiheit 89, 4.7/957), **THE COFFICE DEUTZ**(Charles-de-Gaulle-Platz 1d, 4.8/245, 평일만 영업)가 메쎄 앞에 있다.
- **suedstadt-rheinauhafen:** 유기농 아이스크림 **Der Eismacher**(Severinstr. 53, 4.8/181).
- **ehrenfeld:** **Die Eisdielerin**(Venloer Str. 402), **PUFU**(Vogelsanger Str. 197b).
- **other:** **Il Gelato di Ferigo**(바이엔탈, 4.7/1,617), **Darwish Konditorei**(쥘츠, 4.5/940).

## 나라별 (외국 스타일)

- **일본 JP:** PUFU — 수플레 팬케이크, 기본 €6.50. 대기가 길고 음료가 약하다는 평이 있다.
  말차 카페(Café Goldzeit, Ain Café)는 이름만 나오고 수치·주소가 없어 넣지 않았다.
- **터키 TR:** Damla(Weidengasse 47, 4.2/538, 기준선) — 피스타치오 바클라바.
  Damla Baklava Ehrenfeld는 4.0으로 기준 미달이다. Tadım Damak(4.2/677)는 레스토랑이라 후보에 두고 터키 담당에게 넘긴다.
- **중동(나라 미상):** Darwish Konditorei — 호두 바클라바, 쿠나파.
  나라가 출처에 없어 `cuisine_country`는 비우고 `cuisine_region: "middle-east"`만 적었다. import_raw.py가 이 값을 그대로 받는다.
- **이탈리아 IT:** Il Gelato di Ferigo(젤라테리아).
- **포르투갈 PT:** Bom Dia Köln café(Vorgebirgstr. 1C, 4.3/484, 파스텔 드 나타 €2)가 유일한 후보다.
  같은 거리의 다른 'Bom Dia' 페이지가 'Permanently Closed'로 표시돼 **후보로 보류**했다. 영업 중으로 확인되면 승격해도 된다.
- **이란 IR:** Nobel Konditorei(페르시아어 상호) — 수치·주소 없어 후보.
- **한국 KR 카페:** 쾰른에서 빙수·한국 카페를 찾지 못했다(Wanderlog의 Namu Café는 뒤셀도르프).
  한식 레스토랑 Hana Korean Kitchen(Hohenstaufenring 23)과 아시안 퓨전 Minsu(도이츠, 4.8/934)는 레스토랑 담당 참고용으로 후보에 남겼다.

## 의문점·주의

1. **지역 경계(지오코딩 후 확인):** Coffee Gang(Hohenstaufenring 19 → kwartier-lateng로 분류, 요청서에는 벨기에 지구), Hempies(Händelstraße 55), ST. LOUIS Breakfast(Meister-Gerhard-Str.), Eisliebe(Kettengasse 4 — 우편번호 50672로 프리젠 지구 추정).
2. **겨울 휴업:** 아이스크림 4곳(Eismacher, Eisliebe, Eisdielerin, Ferigo)은 11월 영업 여부를 확인하지 못했다. Eisdielerin은 한 리스트에 '임시 휴업'으로 표시돼 있다.
3. **Eiscafé Breda**(Pfeilstr. 8): 약 4.4/약 1,130으로 수치는 충족한다.
   다만 최근 1점 리뷰에 무례한 응대와 인종차별 발언 주장이 있어 편집 판단용 후보로 두었다.
4. **Café Caprista 지점:** Flandrische Str. 15(벨기에 지구, 1차 tablejourney)와 Venloer Str. 380(에렌펠트, Wanderlog)이 있다. 등재한 쪽은 수치가 연결된 에렌펠트 지점이다.
5. **ST. LOUIS 두 곳**(Breakfast / Café-Köln)이 같은 브랜드인지는 확인하지 못했다.
6. **내용이 얇은 places:** Lint No 7, ST. LOUIS Breakfast, ST. LOUIS Café-Köln은 수치·주소는 확실하다. 다만 메뉴 정보가 없어 must_try가 비어 있다.
7. Wanderlog 수치는 검색 요약을 거친 값이다. 몇 곳(Heimisch 1,375, Darwish 940)은 요약에 '약'이 붙어 있었다.

## 주요 출처

- Wanderlog 리스트: 카페 https://wanderlog.com/list/geoCategory/17153/best-coffee-shops-and-best-cafes-in-cologne ·
  아침·브런치 https://wanderlog.com/list/geoCategory/10013/best-breakfast-and-brunch-in-cologne ·
  로스터 https://wanderlog.com/list/geoCategory/1861715/best-coffee-roasters-in-cologne ·
  아이스크림 https://wanderlog.com/list/geoCategory/51068/best-ice-cream-shops-in-cologne ·
  젤라토 https://wanderlog.com/list/geoCategory/49283/places-to-have-best-gelato-in-cologne ·
  케이크 https://wanderlog.com/list/geoCategory/18938/best-cake-shops-and-cake-bakeries-in-cologne ·
  파티스리 https://wanderlog.com/list/geoCategory/68918/best-pastries-and-patisseries-in-cologne ·
  팬케이크 https://wanderlog.com/list/geoCategory/67133/best-pancakes-in-cologne
- Wanderlog 장소 페이지: 각 항목의 `sources`에 있음
- werkenntdenbesten 베이커리 쾰른: https://www.werkenntdenbesten.de/baeckerei/koeln
- gelbeseiten(Feynsinn): https://www.gelbeseiten.de/gsbiz/c575c5e8-cb41-43be-935a-0d9f8bef67d6
- 1차 조사 출처 재사용(주소·분위기 정보): koeln.de(Café Belgique, Heimisch), Rausgegangen, Mit Vergnügen 2025·2026, tablejourney, Meininger 블로그
