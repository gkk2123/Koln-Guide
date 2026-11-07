# r2-east-asia 조사 노트 (2026-11-07)

담당: 쾰른 전역 동아시아 음식. 한식이 최우선이고, 그다음 일식(라멘·스시·이자카야·파인다이닝), 중식(수타면·쓰촨·딤섬), 대만, 몽골 순서입니다. 1라운드 동아시아 후보 12곳도 검증했습니다.

## 요약

- **places 21곳**: 한국 6 · 일본 10 · 중국 5(범아시아 1곳, 중국·베트남 1곳 포함)
- **candidates 22곳**: 수치 미확인·휴업 표시·주소 불완전·기준 미달·폐업 기록
- **WebSearch 30/30회 사용**(상한 도달 후 중단)
- 지역 분포: belgisches-viertel 6 · kwartier-lateng 3 · dom-altstadt 3 · friesenviertel-ehrenstrasse 2 · agnesviertel-eigelstein 2 · ehrenfeld 1 · suedstadt-rheinauhafen 1 · deutz-messe 1 · other 2
- 구글 수치 출처
  - Wanderlog 장소·리스트 페이지: 첫 번째 점수가 Google, 두 번째가 Tripadvisor
  - restaurantguru.com 평점 패널의 "Google (x/5) n"
  - reviewhero.io "1 Bewertungsportal"(= Google)
- 기준 시점(google_as_of): 어느 출처에도 표시되지 않아 전부 null

## 검색 30회 (괄호 안은 domain 제한)

1. Wanderlog best Korean restaurants Cologne → Bibimbab, Gogi Matcha, Hankki, Bulgogi Haus 이름만 확인
2. werkenntdenbesten koreanisches Restaurant Köln → reviewhero 목록(Hankki, Chlodwigplatz 9 한식당 4.4/326, Ghost Kitchen), Mit Vergnügen 2025 한식 기사
3. Mit Vergnügen 한식 11곳 → Bulgogi Haus 주소(PRINZ), Downtowner(Severinstraße)
4. Wanderlog "Korean restaurants in Cologne" → 성과 없음
5. Hankki 주소 → Wanderlog 4.5(906), 주소 없음
6. (reviewhero.io) koreanisches Restaurant Köln → **Hankki 4.49 / 1,077, Brabanter Str. 42**. Kuroneko, Sushiou 이름도 나옴
7. (reviewhero.io) 이름 4개를 한 번에 검색 → 실패. 이름을 여러 개 묶으면 효과가 없음
8. (wanderlog.com) Korean restaurant Köln place details → **Hana, Bulgogi Haus, Gangnamstyle, Gogi Matcha, Hankki** (가장 생산적인 검색)
9. (wanderlog.com) bibimbap/tteokbokki/kimbap → Bibimbab에 'Temporarily Closed' 표시
10. (wanderlog.com) Tanoshii, Daikan → 두 곳 수치·주소, Shibuya(Neusser Str. 332)
11. (wanderlog.com) ramen → **Takumi, COCO Ramen, Daimyo, Hambaga, Eppus**, TAKEICHI(휴업 표시), Takezo, Ramen & Sushi Köln(폐업)
12. (wanderlog.com) Tsukiji, Sushi Ninja, Kuroneko → 세 곳 수치. Kuroneko는 번지 없음
13. (wanderlog.com) taku, ITO, ZEN → taku 4.1(556)
14. ITO Michelin → 미쉐린 페이지에서 주소 확인(Antwerpener Str. 15)
15. (aggregators) ITO → **restaurantguru Google 4.6 / 308**
16. (aggregators + michelin) ZEN → **Bachemer Str. 233, 2026 셀렉션, Google 4.7**
17. (aggregators + mitvergnuegen) Wen Cheng → Flandrische Str. 2, 2026-05 개업, 수치 없음
18. (wanderlog.com) Qing Tian, Asia Oma, Ni'Hao, Noodle Fan → Qing Tian 수치 충돌, NiHao(Aachener Str. 31)
19. (wanderlog.com) dim sum/Sichuan/hot pot → Tang Wang, Great Wall, Xing Wang, China Fortuna Haus(휴업)
20. (reviewhero+wanderlog) Severinstraße 한식 → Corndawgs 4.2(625), 번지 없음
21. (aggregators) Tang Wang, Great Wall → **Tang Wang Google 4.7 / 685, Maximinenstr. 4**
22. (aggregators) Asia Oma → 못 찾음. 대신 Asia Thai Gourmet, Madame Dzung, Fantasia
23. (aggregators + mitvergnuegen) Meiwei → **Mindener Str. 4, Google 4.5 / 128**
24. (aggregators) Minsu → 한식이 아니라 VN/JP 퓨전. Downtowner 주소(162a) 발견
25. (aggregators) Downtowner → **restaurantguru Google 4.7 / 1,218**
26. (mitvergnuegen) 한식 주소·시간 → Downtowner Severinstr. 164, 50678 / Hankki 시간 / Anju(Ehrenfeld)
27. (aggregators) Ghost Kitchen, Corndawgs → Ghost Kitchen 폐업
28. (aggregators + mitvergnuegen) 대만 → 대만 전문점 없음. **Bai Lu Noodles**, NaiNai Bao, Wengo Dumplings
29. (aggregators) NaiNai Bao, Kung Fu Noodles, Noodle Fan → **NaiNai Bao 4.8 / 587**, Kung Fu 폐업
30. koreanischer Supermarkt Köln → Heng Long Asia Supermarkt

**효과 있던 방법:** `allowed_domains`를 wanderlog.com이나 reviewhero.io·restaurantguru.com으로 묶고 장르 단어로 검색하면, 장소 페이지 여러 개의 구글 수치·주소·전화를 한 번에 얻을 수 있습니다. 반대로 이름 여러 개를 한 검색에 넣으면 대부분 실패했습니다(7·18번).

## 나라별 결과

### 한국: places 6 + 후보 5

쾰른 한식은 세 갈래입니다.
- 치킨·분식: Hankki, Downtowner, Corndawgs
- 고기구이: Bulgogi Haus, Gangnamstyle
- 찌개·가정식: Hana, Gogi Matcha

| 이름 | area | 주소 | Google | 출처 | 메모 |
|---|---|---|---|---|---|
| Hankki Köln | belgisches-viertel | Brabanter Straße 42, 50672 | 4.5 (1,077) | reviewhero(Ø4.49) / Wanderlog 4.5(1,045) | 양념·간장 순살치킨, 떡볶이. 웨이팅 30분+, 예약 권장. confidence high |
| Hana Korean Kitchen | kwartier-lateng | Hohenstaufenring 23, 50674 | 4.7 (741) | Wanderlog | 순두부찌개, 해물파전. 영업시간 일부만 확인 |
| Bulgogi Haus | other | Neusser Straße 654, 50737 | 4.8 (2,024) | Wanderlog (TA 4.5/588) | 테이블 그릴, 반찬 뷔페. 현지인 추천 1순위(Culture Trip). 시내에서 멂 |
| Gangnamstyle Korean BBQ | dom-altstadt | Thurnmarkt 7, 50676 | 4.7 (2,088) | Wanderlog | 구시가 고깃집 겸 바, QR 주문. 과다 청구 리뷰가 있어 계산서 확인 팁 |
| Gogi Matcha | agnesviertel-eigelstein | Johannisstraße 47, 50668 | 4.4 (1,388) | Wanderlog (TA 4.0/82) | 부대찌개, 치즈불닭. 늘 붐빔. 뒤셀도르프 지점과 혼동 주의 |
| Downtowner | suedstadt-rheinauhafen | Severinstraße 164, 50678 | 4.7 (1,218) | restaurantguru Google 패널 | 치킨, 불고기, 비빔밥, 전, 콘도그. 메인 약 €24. 수–일만 영업 |

- 한식 후보
  - Corndawgs: 콘도그. 번지가 없고 수치가 충돌함
  - Anju: Ehrenfeld, 한식 타파스. 2019 기사뿐
  - Bibimbab: 휴업 표시, 주소 미상
  - Ghost Kitchen Korean Style: 폐업. 기록용으로만 후보에 넣음
  - Minsu: 이름은 한국식이지만 VN/JP 퓨전
- 이름을 못 찾은 곳: reviewhero 한식 목록에 **"Chlodwigplatz 9" 한식당 4.4(326)**이 있는데 상호가 나오지 않았습니다. 다음 라운드에서 한 번 검색할 가치가 있습니다.
- OpenTable 결과
  - "LĒN | KimBaBBox"(4.7/16), "Sojubar"(4.4/14): 쾰른 위치·구글 수치 미확인. OpenTable 점수라 쓰지 않음
  - "Kochi Flingern": 뒤셀도르프(Flingern)입니다.
- 김밥·분식 전문점은 이번에 확인하지 못했습니다.
- Mit Vergnügen 2025 "11 Restaurants und Imbisse … Koreanisch" 기사의 11곳 중 확인한 곳은 Hankki, Downtowner, Bulgogi Haus뿐입니다.

### 일본: places 10 + 후보 9

| 이름 | area | 주소 | Google | 메모 |
|---|---|---|---|---|
| Takumi | kwartier-lateng | Hohenstaufenring 58, 50674 | 4.7 (7,973) | 라멘. 리뷰 수가 매우 많아 재확인 권장(아래 의문점 3) |
| Tsukiji | kwartier-lateng | Zülpicher Platz 4a, 50674 | 4.8 (982) | 스시, 좌식 테이블은 예약 필요. Mit Vergnügen '크바르티어 라텡 최고 핫플' |
| COCO Ramen – Sushi | dom-altstadt | Breite Straße 26 (WDR Arkaden), 50667 | 4.7 (947) | 점심 가성비 |
| Daimyo | friesenviertel-ehrenstrasse | Friesenwall 116, 50672 | 4.7 (834) | 라멘·피트니스 스시. 현금만 받는다는 리뷰 → payment cash-only |
| ZEN Japanese Restaurant | other (Lindenthal) | Bachemer Straße 233, 50935 | 4.7 (730) | 2026 미쉐린 셀렉션, €€. Aachener Str. 20의 'ZEN'(1.9점)은 다른 가게 |
| ITO Japanese Cuisine | belgisches-viertel | Antwerpener Straße 15, 50672 | 4.6 (308) | 오마카세, 테이스팅 €109. 미쉐린 가이드 수록, 2020-11 개업. fine-dining · price 4 |
| Hambaga | belgisches-viertel | Aachener Straße 9, 50674 | 4.6 (356) | 버거·라멘·칵테일 바. JP+US |
| Tanoshii | belgisches-viertel | Brabanter Straße 3, 50674 | 4.5 (905) | 스시 + 베트남 요리(JP+VN). 장어·와규 니기리 |
| Sushi Ninja | ehrenfeld | Venloer Straße 241, 50823 | 4.5 (724) | 린덴탈 지점 4.3(275)은 tips에만 적음 |
| Daikan | belgisches-viertel | Maastrichter Straße 9, 50672 | 4.3 (2,378) | 이자카야, 미소 라멘. Wanderlog 라멘 1위 |

- 일식 후보
  - Tokyo Ramen TAKEICHI: 4.5/710, 휴업 표시
  - KURONEKO Sushi: 4.8/230, Brück, 번지 없음
  - Shibuya: Neusser Str. 332, 4.4/563, 다이칸 지점인지 불명
  - Ramen Eppus: Chlodwigplatz 6, 4.7/264, 수프 바인지 라멘집인지 불명
  - Ramen Bar Takezo: 수치·번지 없음
  - Fantasia Sushi: 무제한 스시, 리뷰 수 없음
  - taku: 4.1/556, 기준 미달
- 이름만 나온 곳(다음 라운드 리드): Saigyo, Kaizen, Sushi Mi Cologne, Sushi-Nakoyashi, Sushiou, TOKYO Japanese Restaurant(restaurantguru), Shima by Ito(schlemmer-atlas; ITO 계열로 보이나 미확인)

### 중국: places 5 + 후보 9

| 이름 | area | 주소 | Google | 메모 |
|---|---|---|---|---|
| Tang Wang Köln | agnesviertel-eigelstein | Maximinenstraße 4, 50668 | 4.7 (685) | 쓰촨. 생선 요리, 돼지고기 조림, 소고기 국수. '숨은 맛집'. confidence high |
| NaiNai Bao | dom-altstadt | Josef-Haubrich-Hof 3, 50676 | 4.8 (587) | 비앙비앙면, 1인 €10–20 |
| Bai Lu Noodles | friesenviertel-ehrenstrasse | Palmstraße 41, 50672 | 4.5 (1,352) | 소고기 국수. 플랫폼 명시가 없어 Wanderlog 규칙으로 구글 판단 |
| MEIWEI | deutz-messe | Mindener Straße 4, 50679 | 4.5 (128) | 범아시아(CN+TH): 바오쯔·완탕, 채식, 평일 점심 €10.50 |
| NiHao | belgisches-viertel | Aachener Straße 31, 50674 | 4.6 (97) | 중국·베트남. EC카드/현금만이라는 리뷰. 정보가 얇음 |

- 중식 후보
  - Wen Cheng Köln: 주소 확인, 수치 없음
  - Qing Tian: 수치 충돌, 휴업 표시
  - NOODLE FAN, Great Wall, Wengo Dumplings: 주소·수치 없음
  - Xing Wang: 4.2, 플랫폼 불명
  - Asia Thai Gourmet: Google 4.6/262지만 정보가 얇고 PLZ 없음
  - Asia Oma, Ni'Hao Nudelbar: 이번에 못 찾음
  - Kung Fu Noodles: 폐업
- **딤섬 전문점은 확인하지 못했습니다.** restaurantguru의 "soup dumplings in Cologne" 목록 페이지가 있으니 다음 라운드에서 한 번 검색할 가치가 있습니다.
- 훠궈: China Fortuna Haus는 휴업 표시 때문에 넣지 않았습니다.

### 대만 · 홍콩 · 몽골

- 대만: 전문 식당은 못 찾았습니다. Wengo Dumplings에 대만식 꽈바오가 있다는 것만 확인했습니다(후보).
- 홍콩: 조사하지 못했습니다.
- 몽골: 1라운드에서 검증된 Mongo's 외에 추가 조사는 하지 않았습니다.

## 1라운드 후보 12곳 검증 결과

| 이름 | 결과 |
|---|---|
| Tanoshii | places로 올림. Brabanter Str. 3, 4.5 (905) |
| Daikan | places로 올림. Maastrichter Str. 9, 4.3 (2,378) |
| Wen Cheng | 후보 유지. 주소(Flandrische Str. 2)와 영업시간은 확인, 구글 수치 없음 |
| Sushi Ninja | places로 올림. Venloer Str. 241, 4.5 (724) |
| Qing Tian | 후보 유지. 4.9(109)와 4.7(238)이 충돌하고 휴업 표시 |
| Asia Oma | 못 찾음(상호 변경 가능성). 후보 유지 |
| Ni'Hao Nudelbar | 못 찾음. 다른 가게인 NiHao(Aachener Str. 31)를 places로 올림 |
| Tsukiji | places로 올림. Zülpicher Platz 4a, 4.8 (982) |
| Meiwei | places로 올림. Mindener Str. 4, 4.5 (128) |
| taku | 기준 미달 4.1 (556). 후보 |
| ITO | places로 올림. Antwerpener Str. 15, 4.6 (308) |
| ZEN | places로 올림. Bachemer Str. 233, 4.7 (730) |

1라운드 후보와 이름을 맞춰 두었으므로(Tanoshii, Daikan, Sushi Ninja, Tsukiji, MEIWEI) import 때 낡은 후보 행이 자동으로 빠집니다. Wen Cheng과 Qing Tian은 새 정보가 묻히지 않도록 이름을 조금 달리 했습니다('Wen Cheng Köln', 'Qing Tian | Handpulled Noodles'). 리드가 중복을 정리해 주세요.

## 의문점·주의

1. **Wanderlog 수치의 구글 귀속**
   - 검색 요약은 장소 페이지마다 점수 두 개를 보여 줬습니다. Bulgogi Haus, Gogi Matcha, ZEN, Tsukiji, Sushi Ninja에서는 첫 번째를 'Google', 두 번째를 'Tripadvisor'라고 명시했습니다.
   - 요약이 플랫폼을 말하지 않은 Hambaga, Bai Lu, NiHao도 같은 규칙으로 구글로 읽고 confidence를 medium으로 두었습니다.
   - Daikan은 요약이 두 번째 점수 3.5(206)를 'Google'이라고 했습니다. 하지만 리뷰 수 규모로 보아 Tripadvisor를 잘못 부른 것으로 판단했습니다. 엄격하게 보려면 Daikan과 Bai Lu는 low로 내려도 됩니다.
2. **스냅샷 차이**: 같은 가게라도 Wanderlog 리스트 페이지와 장소 페이지의 리뷰 수가 다릅니다. 리뷰 수는 줄지 않으므로 가장 큰 값을 최신으로 보고 썼습니다.
   - Tanoshii 755–905
   - ZEN 640–730
   - Hankki 906 / 1,045 / 1,077
3. **Takumi 7,973건**: 라멘집 한 곳치고 아주 많습니다. 구글 지도에서 한 번 확인하는 게 좋습니다.
4. **Downtowner 번지**: Mit Vergnügen은 164(PLZ 포함), Restaurant Guru는 162a입니다. PLZ가 있는 164를 썼습니다.
5. **area 판단**
   - Hohenstaufenring 23·58 → kwartier-lateng (쥘피허 플라츠~바바로사플라츠 링 구간)
   - Johannisstraße 47, Maximinenstraße 4 (50668) → agnesviertel-eigelstein (중앙역 북쪽)
   - Breite Straße 26(WDR Arkaden), Thurnmarkt 7(호이마르크트 남쪽), Josef-Haubrich-Hof 3(노이마르크트) → dom-altstadt
   - Palmstraße 41 → friesenviertel-ehrenstrasse
   - Venloer Str. 241 → ehrenfeld (1라운드와 동일)
6. **가격**: 출처에 1인 가격이 거의 없어 대부분 price_level을 null로 두었습니다.
   - 근거가 있는 곳: NaiNai Bao 1, Bulgogi Haus 2, Downtowner 2, ITO 4
   - Bulgogi Haus의 정액 €21.90은 작성 시점을 모르는 Culture Trip 기사 기준입니다.
   - ITO는 미쉐린 표기가 €€이지만, 리뷰의 €109 테이스팅 메뉴를 근거로 4로 두었습니다.
7. **미쉐린**
   - ZEN은 2026 셀렉션이 명시돼 있습니다.
   - ITO는 미쉐린 페이지가 있지만(€€, Japanese·Modern) 연도가 확인되지 않아 "MICHELIN Guide (selected)"로 적었습니다.
   - taku의 별은 Wanderlog 설명에만 나옵니다. 2026 공식 확인은 하지 못했습니다.
8. **영업시간**: Hankki는 기사 연도마다 시간이 달라(2022 점심 영업 / 2025 저녁만, 주말 낮) tips에 적었습니다.

## 폐업·휴업 신호(가이드에 넣지 말 것)

- 폐업
  - Ghost Kitchen Korean Style (Severinstraße 78, Restaurant Guru)
  - Kung Fu Noodles (Alter Markt 10)
  - Ramen & Sushi Köln (Roonstraße 8)
  - NiHao (Brüsseler Straße 44)
  - China-Restaurant Qing Dao
- 휴업 표시
  - Tokyo Ramen TAKEICHI (Friesenstraße 57)
  - Qing Tian (Venloer Straße 207, 리스트 페이지)
  - Bibimbab
  - China Fortuna Haus (훠궈)
- 혼동 주의: 'ZEN' (Aachener Straße 20)은 평점 1.9인 다른 가게입니다.

## 한국·아시아 식료품점(검색 1회)

- **Heng Long Asia Supermarkt**: Aachener Straße 201–209, 50931 Köln, Tel. 0221 2828800
  - 약 1,000㎡ 규모의 아시아 식품·잡화점입니다. 한국 식품 비중은 출처에 없습니다.
  - 출처: https://www.koeln.de/branchen/eintrag/551/asia-maerkte/heng-long-asia-supermarkt
- **Mit Vergnügen "11 asiatische Supermärkte in Köln"**(2025·2026판)
  - 기사가 있다는 것은 확인했지만 목록은 뽑지 못했습니다. 다음 라운드에서 이 기사 하나만 검색하면 한국 마트를 확인할 수 있을 것입니다.
  - https://koeln.mitvergnuegen.com/2026/asiatische-supermaerkte
- 'Asia Shop bei Miga': 한국 음식이 있는 아시아 숍으로 언급됐지만 주소는 미확인입니다.
- 근교(쾰른 밖, 기차로 당일): 뒤셀도르프 리틀 도쿄 일대
  - **Dae-Yang**: Immermannstraße 21, Düsseldorf. 한국·일본 슈퍼 (https://ryukoch.com/de/bewertungen/dae-yang)
  - **Hanaro Markt**: Düsseldorf (https://www.visitduesseldorf.de/attraktionen/hanaro-markt-56ea5bd93a)

## 다른 담당에게 넘길 것

- 베트남: **Madame Dzung**, Zülpicher Str. 39, Google 4.9 (99), restaurantguru → 동남아 담당
- 범아시아 퓨전: Minsu Restaurant Köln, Mindener Str. 2 (Deutz). 구글 수치 없음

## 다음 라운드 제안(검색 8–10회)

1. "Chlodwigplatz 9 Köln koreanisch" → 이름이 확인되지 않은 한식당(reviewhero 4.4/326)
2. Mit Vergnügen 2025 한식 11곳 기사 → 나머지 8곳의 이름
3. Mit Vergnügen 아시아 슈퍼 11곳 기사 → 한국 마트
4. Wen Cheng Köln 구글 수치 (개업 반년이 지나 리뷰가 쌓였을 것)
5. Qing Tian, TAKEICHI 영업 재개 여부
6. KURONEKO Sushi 번지(Brücker Mauspfad)
7. restaurantguru "soup dumplings / dim sum Cologne" → 딤섬
8. NOODLE FAN 지점 주소·수치
9. taku 2026 미쉐린 별 유지 여부
10. Takumi 리뷰 수 재확인

## 주요 출처

- Wanderlog 리스트
  - 일식: https://wanderlog.com/list/geoCategory/54638/best-japanese-food-and-restaurants-in-cologne
  - 스시: https://wanderlog.com/list/geoCategory/84981/best-sushi-restaurants-and-sushi-bars-in-cologne
  - 라멘: https://wanderlog.com/list/geoCategory/1507873/best-ramen-in-cologne
  - 면 요리: https://wanderlog.com/list/geoCategory/1789534/best-noodle-spots-in-cologne
  - 중식: https://wanderlog.com/list/geoCategory/22508/best-chinese-food-in-cologne
  - 치킨: https://wanderlog.com/list/geoCategory/1817171/best-spots-for-fried-chicken-in-cologne
- Wanderlog 장소 페이지: JSON 각 항목의 `sources`에 있습니다.
- reviewhero
  - https://www.reviewhero.io/hankki-koln-1736
  - https://www.reviewhero.io/de/koreanisches-restaurant/koeln
- restaurantguru
  - https://restaurantguru.com/Downtowner-Cologne
  - https://restaurantguru.com/ITO-Japanese-Cuisine-Cologne
  - https://restaurantguru.com/Tang-Wang-Cologne
  - https://de.restaurantguru.com/MEIWEI-Asiatisch-Cologne
  - https://restaurantguru.com/Ghost-Kitchen-Korean-Style-Koln-Cologne
- Michelin
  - https://guide.michelin.com/us/en/nordrhein-westfalen/koln/restaurant/zen-japanese-restaurant
  - https://guide.michelin.com/th/th/nordrhein-westfalen/koln/restaurant/ito-1193617
  - https://guide.michelin.com/de/de/best-of/die-top-japaner-in-dusseldorf-koln-und-bonn
- Mit Vergnügen
  - 한식: https://koeln.mitvergnuegen.com/2025/koreanisch-essen/
  - 수타면: https://koeln.mitvergnuegen.com/2026/handgezogene-nudeln/
  - 중식: https://koeln.mitvergnuegen.com/2026/chinesisch-essen/
  - 만두: https://koeln.mitvergnuegen.com/2025/dumplings/
  - 강 동쪽 아시아 음식: https://koeln.mitvergnuegen.com/2025/asiatisch-schael-sick/
  - Anju: https://koeln.mitvergnuegen.com/2019/anju-koeln/
  - Gogi Matcha: https://koeln.mitvergnuegen.com/2019/gogi-matcha-das-vielleicht-beste-koreanische-restaurant-koelns/
- 기타
  - https://theculturetrip.com/europe/germany/cologne/articles/best-asian-restaurants-cologne
  - https://prinz.de/koeln/locations/kategorie/essen-trinken/koreanisch/
