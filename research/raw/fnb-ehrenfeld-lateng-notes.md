# fnb-ehrenfeld-lateng 조사 노트 (2026-11-07)

담당: 에렌펠트(`ehrenfeld`) + 크바르티어 라텡/쥘피허 지구(`kwartier-lateng`)의 식음료(레스토랑, 브라우하우스·브루펍, 카페, 베이커리, 디저트, 길거리 음식). 칵테일·맥주·와인 바는 제외.

## 0. 상태 요약 (먼저 읽어 주세요)

- **결과: 기준 충족 3곳(`places`), 후보 40곳(`candidates`: 에렌펠트 26, 크바르티어 라텡 14).** 목표 25–30곳에 크게 못 미칩니다.
- **원인 1 — WebFetch 차단:** `www.werkenntdenbesten.de` 요청이 ENOTFOUND로 실패(세션 네트워크 허용 목록 밖). 브리프대로 1회만 시도. 이 사이트를 쓰려면 세션 네트워크 설정에서 `www.werkenntdenbesten.de`를 허용해야 합니다.
- **원인 2 — WebSearch 공유 한도 소진:** 턴당 200회(모든 에이전트 공유) 한도가 이 에이전트의 약 30번째 검색에서 바닥났습니다. 이후 검색이 전혀 불가능해 개별 검증 단계에 들어가지 못했습니다. 한도를 우회하는 다른 수단은 쓰지 않았습니다.
- **후보 40곳 = 검증 대기열:** 주소·특징·출처는 정리돼 있고 **구글 평점·리뷰 수만 확인하면 됩니다.** 후속 세션에서 `"<이름> Köln Google Bewertungen"`류 검색을 곳당 1–2회 돌리면 상당수가 `places`로 올라갈 것으로 봅니다. 우선순위 추천: Brauhaus Pütz, Haus Scholzen, Kebapland, Asia Oma, Habibi, La Société, Hellers Brauhaus, Nonna Napoli(두 지점), Falafel König, Viet Village, Café Sehnsucht, Van Dyck.
- **price_level = null (3곳 모두):** 메뉴 가격이나 구글 1인 가격대 출처를 확보하지 못해 추정하지 않고 비웠습니다. 빌드 스크립트에서 null 처리가 필요합니다.
- **google_as_of = null (3곳 모두):** 검색 결과에 "Stand" 날짜가 보이지 않았습니다.

## 1. 검색한 내용

- 시드 10곳 개별 검색: Braustelle, Haus Scholzen, Essers Gasthaus, Herbrand's, Bunte Burger, Bei Oma Kleinmann, Hellers Brauhaus, Brauhaus Pütz, Café Feynsinn, La Société (독일어 "Google Bewertungen", werkenntdenbesten, restaurantguru, 그리고 spinach.guide / restaurantguru.com / wanderlog.com 도메인 제한 검색).
- 영업 상태: Hellers Brauhaus 2025/2026 영업 여부, La Société 미쉐린 2026.
- 후보 발굴용 리스트: Mit Vergnügen Köln — 2026 "21 Restaurants in Ehrenfeld", 2026 "21 Cafés und Restaurants auf der Venloer Straße", 2026 "21 Cafés in Ehrenfeld", 2025 "21 Orte in Ehrenfeld … lunchen", 2024 "11 Cafés und Restaurants an der Zülpicher Straße", 2024/2026 Kwartier Latäng 기사, 2026 "wie in der Türkei"; koeln.de 에렌펠트 인기 레스토랑; 시리아·레바논·터키 음식(Venloer Straße).
- **못 한 것(한도 소진):** 크바르티어 라텡 카페·브런치 리스트, 에렌펠트 시리아·레바논 전문점(검색에서 구체적 가게명이 안 나옴), 베이커리, 디저트·아이스크림, 라멘, 고급 레스토랑(Fabian, Esszimmer) 수치 검증, 후보 전원의 구글 수치.

## 2. 지역 분위기

### 에렌펠트 (Ehrenfeld)

- **성격:** 쾰른 서쪽의 옛 공업·노동자 동네. 헬리오스(Helios) 전기회사 공장 터 같은 산업 유산 위에 클럽·공연장·스튜디오·스트리트아트가 들어서, 지금은 쾰른에서 가장 다문화적이고 '힙한' 동네로 꼽힌다. 아프리카·터키 이발소와 레바논 음식점이 섞인 거리 풍경 자체가 볼거리.
- **베놀러 거리(Venloer Straße) = 먹자 거리:** 동쪽 입구의 DITIB 중앙모스크부터 서쪽으로 길게 터키계 케밥·라흐마준·탄투니·쿰피르 가게(Kebapland 385, Tantuni Haus 282, Eat Kumpir 274), 팔라펠(Falafel König 384), 베트남(Viet Village 235)·태국(Thai Street Food 282)·중국 수타면(Qing Tian 207), 나폴리 피자(Nonna Napoli 248, Spaccanapoli 502), 비건(Vegan Food Revolution 456), 독일 전통(Haus Scholzen 236, 1907년부터), 고급 메제(Restaurant Fabian 531)까지 이어진다.
- **골목:** 쾨르너 거리(Körnerstraße)는 작은 카페·에스프레소 바(Café Sehnsucht 67, 옛 미용실 자리의 Van Dyck 43)가 모인 조용한 골목. 헬리오스 지구에는 하우스 양조장 Braustelle(Christianstraße 2)와 옛 객차공장 자리의 Herbrand's(Herbrandstraße 21, 비어가든). 서브벨라터 거리(Subbelrather Straße)엔 에티오피아 인제라집 Soliana. 주택가 노이에렌펠트(Neuehrenfeld)엔 와인 리스트로 상을 받은 오스트리아식 Essers Gasthaus(Ottostraße 72).
- **언제 갈까:** 점심~저녁의 '먹방 산책'이 가장 좋다(싸고 푸짐한 점심집이 많음). 주말 밤엔 클럽·공연장 손님으로 붐빈다. 교통: 트램 3·4번 Körnerstraße / Venloer Str./Gürtel / Leyendeckerstraße 정류장, 13번 Venloer Str./Gürtel, S-Bahn Köln-Ehrenfeld역.

### 크바르티어 라텡 (Kwartier Latäng, 쥘피허 지구)

- **성격:** 'Kwartier Latäng'은 파리 '카르티에 라탱(라틴 지구)'의 쾰시 사투리. 쾰른 대학교와 맞닿은 학생 지구다. 쥘피허 거리(Zülpicher Straße)는 Mit Vergnügen 표현대로 "주로 파티 거리"(술집·클럽 밀집)지만, 음식은 프렌치 타파스부터 이탈리안 파인다이닝까지 폭이 넓다.
- **먹을 곳:** 쥘피허 거리 초입(1–50번대)에 몰려 있다 — 거대한 슈니첼의 Bei Oma Kleinmann(9), 40년 넘은 사르데냐식 이탈리안 Etrusca(27), 쾰른에서 가장 유명한 팔라펠집 Habibi(28), 새벽 3시까지 여는 플랫브레드 Ferkulum(37), 구글 리뷰로 거리 최고라는 중식 Asia Oma(38), 수타면 Ni'Hao Nudelbar(46), 나폴리 피자 Nonna Napoli(5). 키프호이저 거리(Kyffhäuserstraße)엔 미쉐린 1스타 La Société(53)와 "쾰른 최고 되너"라는 팬이 있는 Oruc(Heinsbergstraße 모퉁이). 로온 거리(Roonstraße)엔 Hellers Brauhaus(33), 엥겔베르트 거리(Engelbertstraße)엔 지하 볼트형 공간의 Brauhaus Pütz(67)와 학생 크나이페, 나무 많은 광장 라테나우플라츠(Rathenauplatz)엔 유기농 아침의 Café Feynsinn(7).
- **언제 갈까:** 저녁~심야가 본령(늦게까지 여는 곳이 많음). 낮엔 비교적 조용해 카페·점심에 좋다. 교통: U-Bahn Zülpicher Platz(9·12·15번), Barbarossaplatz(12·15·16·18번), 9번 Universität.
- **주의 — 11월 11일:** 카니발 시즌 개막일(11.11)과 Weiberfastnacht(카니발 목요일)에는 쥘피허 거리 일대가 엄청난 인파로 출입 통제·유리병 반입 금지 등이 시행되는 구역이 된다. 2026년 11월 11일(수)도 해당되니, 이날은 이 동네 식당을 피하거나 통제 상황을 각오하고 갈 것.

## 3. 포함한 3곳 메모

| 장소 | 구글 수치 | 출처 | 판단 |
|---|---|---|---|
| Braustelle (에렌펠트, 브루펍) | 4.6 / 342 | werkenntdenbesten.de ("google.de" 항목). Wanderlog도 약 4.6 / 약 330으로 일치 | 2026 Mit Vergnügen 에렌펠트 리스트에 등장 → 영업 중. confidence medium |
| Bei Oma Kleinmann (쥘피허, 독일식) | 4.7 / 4,677 | gayout.com의 Google 항목. spinach.guide는 4.7 / 4,542 | 리뷰 수가 더 많은(=더 최신으로 보이는) GayOut 값 채택. 2025-09 리뷰 있음. confidence high |
| Café Feynsinn (라테나우플라츠, 카페) | 4.2 / 724 | gelbeseiten.de ("Google-Bewertungen") | 기준선에 딱 걸침. speisekarte.menu는 3.7 / 3,365(출처 불명)로 충돌 → **confidence low, 재확인 권장**. 그 3.7이 구글 수치로 확인되면 후보로 내릴 것 |

참고: werkenntdenbesten 도시 랭킹 페이지엔 Braustelle가 4.69(3개 포털 79건)로 따로 나와 있어 프로필 페이지와 데이터셋이 다릅니다. 구글 단독치는 프로필 페이지의 4.60(342)을 사용했습니다.

## 4. 후보·제외 메모

- **구글 수치를 못 찾은 시드:** Haus Scholzen, Essers Gasthaus, Herbrand's, Bunte Burger, Hellers Brauhaus, Brauhaus Pütz, La Société → 모두 `candidates`.
- **Brauhaus Pütz:** 포털 합산 4.4–4.6(1,755–3,444건)만 확인, 구글 단독치는 없음. 통과 가능성이 높아 보임. Mühlen Kölsch를 받아 쓰는 집(자체 양조 아님).
- **Hellers Brauhaus:** 2024년 여름 이후 **양조는 중단**, 브라우하우스와 Volksgarten은 계속 영업(leinetal24). 2026년 1월 방문 OpenTable 리뷰 있음 → 폐업 아님. 다만 더 이상 '자가 양조 맥주'가 아니라는 점을 가이드에 반영해야 함.
- **La Société:** 미쉐린 1스타(2024·2025 확인), 2026 유지 여부는 미확인. 셰프 Leon Hofmockel.
- **폐업 확인된 곳:** 없음.
- **담당 구역 밖(다른 에이전트에게):** Café Lindenburg(Zülpicher Str. 275, 50937 — Sülz), Café Goldjunge(Zülpicher Str. 282 — Sülz) → `other`. Gilbert's Pinte(Engelbertstraße 학생 크나이페) → 바 담당.
- **넣지 않은 것:** Café Fee(쾨르너/베놀러 모퉁이, 2024년 2월 개업)와 Pfeiler Grill(Körnerstraße 119, 기로스)는 이름이 나왔지만 어느 출처인지 특정할 수 없어 후보에서도 뺐습니다. restaurantguru의 "Ehrenfelder Brauhaus"도 정보가 이름뿐이라 뺐습니다.

## 5. 미해결 의문

- **Haus Scholzen PLZ:** speisekarte.de 제목은 50667, koeln.de는 50823 → 에렌펠트 PLZ인 50823 사용.
- **Bunte Burger 주소:** 현재 Hospeltstraße 1, 50825. rausgegangen 기사의 Brabanter Str. 48은 옛 주소로 보임.
- **Essers Gasthaus 영업시간:** koeln.de(수 휴무, 18시 주방 오픈) vs speisekarte.de(매일 17:30–23:00).
- **Nonna Napoli Ehrenfeld:** 2026 리스트는 Venloer Straße 248, 2025 스니펫엔 "Vogelsanger Straße 뒷마당"으로 나옴 — Gusto Antico(Vogelsanger Straße 216)와 섞인 것으로 추정.
- **Ni'Hao Nudelbar(Zülpicher Str. 46) ≠ NiHao(Aachener Str. 31):** 다른 가게.
- 후보 중 PLZ나 번지를 확인 못 한 곳은 주소에 "(PLZ unverified)" / "(house number unverified)"로 표시. 지오코딩 전에 보완 필요.
- Virtuous Pie(Venloer Str. 241–245)는 Mit Vergnügen 리스트에 있으나 음식 종류를 결과에서 확인하지 못함.

## 6. 주요 출처

- Mit Vergnügen Köln: https://koeln.mitvergnuegen.com/2026/restaurants-ehrenfeld/ · https://koeln.mitvergnuegen.com/2026/venloer-strasse-kulinarisch/ · https://koeln.mitvergnuegen.com/2026/cafes-in-ehrenfeld/ · https://koeln.mitvergnuegen.com/2025/lunchen-ehrenfeld/ · https://koeln.mitvergnuegen.com/2024/zuelpicher-strasse-kulinarisch/ · https://koeln.mitvergnuegen.com/2024/essen-kwartier-lataeng · https://koeln.mitvergnuegen.com/2026/kwartier-lataeng
- 구글 수치: https://www.werkenntdenbesten.de/e/29129548/brauerei/koeln/braustelle-bewertungen.html · https://www.gayout.com/europe/germany/cologne/restaurants/bei-oma-kleinmann · https://spinach.guide/venues/bei-oma-kleinmann-30508/ · https://www.gelbeseiten.de/gsbiz/c575c5e8-cb41-43be-935a-0d9f8bef67d6 · https://wanderlog.com/place/details/1784408/braustelle
- koeln.de / Köln Tourismus: https://www.koeln.de/leben/ll/beliebte-restaurants-in-koeln-ehrenfeld/haus-scholzen · https://www.koeln.de/leben/ll/imbisse-und-fast-food-in-koeln/kebapland · https://willkommen.koelntourismus.de/en/gastro/braustelle
- 영업 상태·수상: https://www.leinetal24.de/welt/roonstrasse-pils-hellers-bier-brauerei-koelsch-sort-produktion-eingestellt-anna-heller-zr-92846067.html · https://guide.michelin.com/en/nordrhein-westfalen/koln/restaurant/la-societe
- 기타: restaurantguru.com, wanderlog.com, speisekarte.de, falstaff.com, enprimeurclub.com, joinpearl.co (장소별 URL은 JSON의 `sources` 참고)
