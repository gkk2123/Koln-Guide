# r2-se-south-asia — 동남아·남아시아 음식 조사 노트 (2026-11-07)

## 요약
- **결과:** `places` 15곳, `candidates` 21곳. 파일: `research/raw/r2-se-south-asia.json`.
- **나라 5개:** 태국 7(Thai-Viet 1곳 포함), 베트남 4, 인도 2, 네팔 1, 인도네시아 1.
- **지역:** dom-altstadt 4, belgisches-viertel 3, kwartier-lateng 3, friesenviertel-ehrenstrasse 2, agnesviertel-eigelstein 2, other(니페스) 1.
- **WebSearch:** 22/22회 사용(한도 소진).
- **confidence:** 모두 `medium`. 구글 수치에 기준 시점(`google_as_of`)이 표시된 출처가 없었다.
- **수치를 얻은 곳:** 가장 효과적인 출처는 **top-rated.online**(`allowed_domains` 제한 검색)이었다. Google Maps 데이터를 미러링하는 사이트로, 수치와 주소를 함께 준다. 이 사이트를 쓴 뒤로 한 번 검색에 5–7곳씩 확보됐다.

## Round 1 후보 6곳 검증 결과 — 모두 후보로 남음

| 업소 | 결과 | 이유 |
|---|---|---|
| Viet Village Ehrenfeld | 후보 | 주소는 Venloer Str. 235, 50823으로 확인(Wolt·spinach 일치). spinach.guide 3.2 (763)은 spinach 자체 점수로 보이고, 구글 값은 찾지 못했다. 호엔슈타우펜링 본점의 2호점이다. |
| Com Pho | 후보 | 주소를 **Zülpicher Straße 58D, 50674**로 확보했다. 수치는 speisekarte.menu 4.4 (약 2,450)뿐이라 구글 값이 아니다. 주로 현금이다. |
| Thai Street Food (Venloer 282) | 후보 | **주소가 충돌한다.** top-rated.online에서 Venloer Str. 282는 Tantuni Haus(4.6/372)의 주소로 나온다. 같은 이름으로 검색하면 구시가의 다른 업소(Thai-Viet Street Food Imbiss)만 나온다. |
| Warung Bayu | 후보 | 주소를 **Brabanter Straße 5, 50674**로 확보했다. spinach.guide 4.2 (917)이 구글 값인지 불명확하다(round 1 경험상 spinach 상단 점수는 자체 점수일 수 있음). |
| Mandalay | 후보 | 주소는 Brüsseler Straße 53, 50674인데 출처가 tablejourney 1곳뿐이다. 수치는 speisekarte.menu 4.3 (1,397)뿐이라 구글 값이 아니다. |
| Masala Empire | 후보 | 쾰른 관광청에 페이지가 있어 영업 중 신호는 있다. 검색 요약에 4.3 (661)/(639)가 나왔지만, 실제로 뜬 페이지는 **Masala King**이어서 수치가 섞였을 가능성이 크다. 번지와 PLZ는 미확인이다. |

## 나라별 결과

### 태국 (7곳) — 검색 #8 한 번으로 주소와 수치 확보
| 업소 | 주소 | 구글 | 비고 |
|---|---|---|---|
| Thai Ja-Röen Imbiss | Thürmchenswall 64, 50668 | 4.9 (157) | top-rated 태국 1위, 리뷰 수 적음 |
| Thai-Viet Street Food Imbiss | Kleine Budengasse 11a, 50667 | 4.6 (2.4K) | 현금만. 예전 스냅샷은 318. 태국·베트남 |
| Thai Imbiss | Eigelstein 114, 50668 | 4.5 (1,535) | 중앙역 북쪽 |
| Thai Gourmet | Neusser Str. 311, 50733 | 4.4 (540) | 니페스, 현금만 |
| Krua Thai am Heumarkt | Heumarkt 25, 50667 | 4.4 (748) | 2호점 |
| Thai Food | Friesenwall 24B, 50672 | 4.4 (391) | |
| Krua Thai – Belgisches Viertel | Brüsseler Str. 40-42, 50674 | 4.2 (903) | 기준선 |

이름만 나오고 수치는 얻지 못한 곳(Wanderlog 리뷰 스니펫): Tom Yam Gung Köln('쾰른 최고 태국집' 리뷰), Bangkok Thai Restaurant(예약 권장), Thara Thai, ChangThai, Lai Thai 2, Lannathai(평 엇갈림). Wanderlog 장소 ID와 이름을 대조할 수 없어 후보 JSON에는 넣지 않았다.

### 베트남 (4곳 + Thai-Viet)
| 업소 | 주소 | 구글 | 비고 |
|---|---|---|---|
| Nam | Engelbertstraße 3, 50674 | 4.9 (676) | 쌀국수, 비건 옵션, 길가 좌석 |
| Lúa by Danny | Brabanter Str. 9, 50674 | 4.7 (585) | 휘르트 지점 목록도 따로 있음 |
| 1980 – Cafe und Bánh Mì | Bobstraße 28, 50676 | 4.7 (541) | 반미, 쾰른 관광청 블로그 베스트 5 |
| Chum Chay | Friesenwall 29, 50672 | 4.6 (1,866) | 채식·비건. Wanderlog 수치와 top-rated 4.6/1.9K 일치 |

후보: Yame(Bonner Str. 33, 4.7, 리뷰 수 없음), Kuchi Mami(4.8/1.5K, 주소 없음, 스시 중심), Bun Pho(4.5/1,897, 구글 여부 불명), Hanoi 36, 1992 Vietnamese Fusion & Sushi, Ngon-Ngon, LU Vietnamese Cuisine.

### 인도 (2곳)
- **Ginti:** Händelstraße 33, 50674, 4.4 (4.9K).
- **Ganesha:** Händelstraße 26, 50674, 4.7 (1.8K), 1987년 개업. 카드 결제 후기가 엇갈린다.
- **후보:** Thali(4.6/454, 주소 없음), Namaste, Das Tandoori(Kyffhäuserstr.), Chennai Chef(남인도), Rangoli(3.9, 기준 미달), Masala Empire.

### 네팔 (1곳)
- **Buddha's Eye:** Mariengartengasse 5, 50667, 4.4 (664). reviewhero에 '출처 1곳 = Google'로 나오지만 **업소명 없이 주소만** 보였다. TripAligner에 같은 주소의 Buddha's Eye(네팔·티베트, 4.3/156)가 있어 이 둘을 맞췄다. 리드 검토를 권한다.
- **후보:** Momo Empire(An St. Agatha 27, 네팔 음식점인지 불명), Tibet Momo(Aachener Str. 11, 티베트 음식이라 스키마에 국가 코드 없음).

### 인도네시아 (1곳)
- **Bali Restaurant:** Brüsseler Platz 2, 50672, 4.4 (690). 예전 스냅샷은 4.2 (377)이고, 리뷰 수가 많은 쪽을 채택했다. 사테 땅콩 소스가 칭찬받고, 서비스가 느리다는 평도 있다.
- **후보:** Warung Bayu, Daur Lang(범아시아 비스트로, 인도네시아 음식 호평).

### 미얀마·말레이시아·필리핀·스리랑카·파키스탄 — 확정 0곳
- **미얀마:** Mandalay뿐이고 후보로 남았다.
- **스리랑카·파키스탄:** top-rated.online에서 쾰른 결과가 나오지 않았다(베를린만 나옴).
- **말레이시아·필리핀:** 검색 예산이 부족해 따로 검색하지 못했다.

## 의심·주의 사항
1. **top-rated.online의 기준 시점:** 시점이 표시되지 않는다. 같은 사이트의 한 목록 제목에 'Updated December, 2023'이 있어, 1–3년 전 스냅샷일 수 있다. 같은 업소가 페이지마다 다른 수치를 보이기도 했다(Thai-Viet 318 vs 2.4K, Bali 377 vs 690). 리뷰 수가 많은 쪽을 더 최신으로 보고 채택했다. 그래서 전부 confidence `medium`이다.
2. **'K' 반올림 값:** Ginti 4900, Ganesha 1800, Thai-Viet 2400은 사이트 표시값('4.9K' 등)을 그대로 숫자로 옮긴 것이다. 정확한 개수가 아니며, `rating_source`에 이 사실을 적었다.
3. **Chum Chay의 Wanderlog 수치:** '4.6 (1866) • 4.5 (82)' 중 앞 값을 Google로 봤다(Wanderlog 표기 순서). top-rated.online 값과 일치한다.
4. **검색 요약의 숫자 혼동:** Masala Empire 수치가 Masala King 페이지에서 왔을 가능성이 있다. Thai Street Food 주소도 충돌한다. 둘 다 후보로 뒀다.
5. **지역(area) 판단:**
   - Händelstraße(Ginti·Ganesha): `kwartier-lateng`으로 넣었다. 루돌프플라츠 남쪽 라테나우플라츠 쪽 노이슈타트-쥐트이고, `belgisches-viertel`과 경계다.
   - Bobstraße(1980): `dom-altstadt`로 넣었다. 노이마르크트 남쪽이고 판탈레온 지구와 경계다.
   - Thürmchenswall(Thai Ja-Röen): `agnesviertel-eigelstein`으로 넣었다(중앙역 북쪽 쿠니베르츠 지구).
6. **태국 편중:** 15곳 중 7곳이 태국이다. 출처에서 나온 그대로이고, 대부분 임비스나 캐주얼 식당이다.
7. **비어 있는 정보:** 가격(price_level)은 Buddha's Eye(TripAligner '중간 가격대' → 2)를 빼고 전부 null이다. 메뉴 가격 출처를 찾지 못했다. 영업시간(meals)도 비웠다. 태국 7곳은 대표 메뉴 출처가 없어 must_try를 비웠다.

## 폐업 신호 (넣지 않음)
- **Nanu Thai Kitchen**(Von-Sandt-Platz 12)과 **SOMTAM Thai-Imbiss**(Auguststr. 42): top-rated.online에 'permanently closed'로 표시됨.
- **Taj Mahal**(인도, 3.5/179): 'permanently closed'.
- **Kittichai**(Alter Markt): HappyCow에 2026년 1월 폐업 보고. 다른 라운드에서 다시 넣지 말 것.

## 공백과 다음 라운드 제안
- **우선순위 지역 중 확정 0곳:** 에렌펠트, 도이츠·메쎄, 쥐트슈타트. 에렌펠트는 Viet Village, Thai Street Food, Masala Empire, Hanoi 36이 모두 후보로 남았다.
- **잘 통한 검색 패턴:** `allowed_domains: ["top-rated.online"]` + "<업소명들> Cologne street address rating"처럼 여러 이름을 한 번에 넣는 방식. 페이지가 이미 노출된 업소는 주소가 잘 나왔다.
- **다음에 할 검색:**
  - top-rated.online에서 Viet Village, Mandalay, Yame(리뷰 수), Thali(주소), Kuchi Mami(주소).
  - spinach.guide의 'Read on Google Maps' 값(Warung Bayu, Viet Village).
  - 말레이시아·필리핀·스리랑카는 "malaysisches Restaurant Köln" 같은 독일어 일반 검색.
- **효과 없던 패턴:** spinach.guide 도메인 제한에 여러 이름을 넣은 검색(2회 모두 실패). werkenntdenbesten 제한 검색은 여러 포털을 합산한 값만 나왔다.

## 검색 기록 (22회)
1. Wanderlog Vietnamese Cologne: Chum Chay 4.6(1866), 업소 이름 다수.
2. Wanderlog pho list: 추가 수치 없음.
3. werkenntdenbesten vietnamesisch: Bun Pho 4.5/1897(포털 불명).
4. werkenntdenbesten.de 제한: 합산 수치만 나옴(Thai-Viet 4.5/3166 등).
5. Viet Village Venloer 235: 주소 확인, spinach 3.2/763.
6. spinach.guide 제한, 에렌펠트 3곳: 실패.
7. Wanderlog Thai: 이름만, Kittichai 폐업 보고.
8. top-rated.online Thai: 7곳 확보.
9. top-rated.online Vietnamese: 수치 확보.
10. top-rated.online Indian: Ginti·Ganesha·Thali 수치.
11. top-rated.online Nepal·Sri Lanka·Pakistan: 쾰른 결과 없음.
12. top-rated.online Warung Bayu·Mandalay: 수치 없음, Bali Restaurant·Daur Lang 발견.
13. top-rated.online 베트남 주소: 5곳 주소 확보.
14. top-rated.online 에렌펠트 3곳: 282번지 충돌, Masala King 혼동.
15. Warung Bayu 일반 검색: 주소, spinach 4.2/917.
16. Mandalay 일반 검색: 주소, speisekarte.menu 4.3/1397.
17. top-rated.online Ganesha 등: Ganesha 주소.
18. Com Pho 일반 검색: 주소, speisekarte.menu 4.4/2450.
19. 네팔 일반 검색: reviewhero Mariengartengasse 5 4.4/664(Google).
20. spinach.guide Warung Bayu: 결과 없음.
21. Mariengartengasse 5: Buddha's Eye 확인.
22. top-rated.online Bali Restaurant: 주소와 수치 확보.

## 주요 출처
- **top-rated.online (Google 미러):**
  - https://www.top-rated.online/cities/Cologne/place/p/2223196/Nam
  - https://www.top-rated.online/cities/Cologne/place/p/8260601/L%C3%BAa+by+Danny
  - https://www.top-rated.online/cities/K%C3%B6ln/place/p/4164063/1980+%E2%80%93+Cafe+und+B%C3%A0nh+M%C3%AC
  - https://www.top-rated.online/cities/Cologne/place/p/3041799/Chum+Chay
  - https://www.top-rated.online/cities/Cologne/place/p/1238041/Thai-Viet+Street+Food+Imbiss
  - https://www.top-rated.online/cities/Cologne/place/p/13815343/Thai+Ja-+R%C3%B6en+Imbiss
  - https://www.top-rated.online/cities/Cologne/place/p/1237961/Thai+Imbiss
  - https://www.top-rated.online/cities/Cologne/place/p/4167204/Thai+Gourmet?r
  - https://www.top-rated.online/cities/Koeln/place/p/2223278/Krua+Thai+2+-+Heumarkt
  - https://www.top-rated.online/cities/K%C3%B6ln/place/p/4166725/Krua+Thai+1+-+Belgisches+Viertel
  - https://www.top-rated.online/cities/Cologne/place/p/3287279/Thai+Food?r
  - https://www.top-rated.online/cities/Cologne/place/p/1237972/Ginti+Indian+Restaurant
  - https://www.top-rated.online/cities/Cologne/place/p/1238024/Ganesha+Indisches+Restaurant+in+K%C3%B6ln+seit+1987
  - https://www.top-rated.online/cities/Cologne/place/p/2223265/Bali+Restaurant
- **Wanderlog:**
  - https://wanderlog.com/list/geoCategory/1830383/best-spots-for-soup-in-cologne
  - https://wanderlog.com/list/geoCategory/1820358/pho
  - https://wanderlog.com/place/details/2627460/nam
- **reviewhero / TripAligner:**
  - https://www.reviewhero.io/de/nepalesisches-restaurant/koeln
  - https://tripaligner.com/countries/germany-22/destinations/koln-8618/places/buddha-s-eye-6429306
- **편집 기사:**
  - https://blog.koelntourismus.de/en/culinary-finds/the-five-best-vietnamese-restaurants-in-cologne/
  - https://theculturetrip.com/europe/germany/articles/best-asian-restaurants-cologne
  - https://koeln.mitvergnuegen.com/2025/asiatisch-essen/
- **후보 검증용:**
  - spinach.guide (Viet Village, Warung Bayu)
  - speisekarte.menu (Com Pho, Mandalay, Bun Pho)
  - Wolt (Viet Village, Com Pho)
  - tablejourney (Warung Bayu, Mandalay)
  - koeln.de
  - cologne-tourism.com (Masala Empire)
  - 업소별 URL은 JSON의 `sources`에 있음.
