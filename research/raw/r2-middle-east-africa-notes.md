# r2-middle-east-africa — 조사 노트 (2026-11-07)

범위: 쾰른 전역의 터키·중동(레바논·시리아·이스라엘·페르시아·아프간·모로코)·아프리카(에티오피아·에리트레아·남아공) 음식.
결과: **places 26곳 / candidates 36곳**, WebSearch **28/28회 사용(상한 도달)**.
파일: `research/raw/r2-middle-east-africa.json` (agent `r2-middle-east-africa`, schema v2).
`scripts/import_raw.py --dry-run`으로 확인: 26곳 모두 기준 통과, 이 파일에서 나온 경고 0건.

## 방법과 출처 성격

- 숫자는 거의 모두 **Wanderlog**(목록·장소 페이지)에서 나왔다. Wanderlog는 "Google 평점(리뷰 수)"와 "Tripadvisor 평점(리뷰 수)"를 따로 보여 주고,
  검색 결과 요약에서도 둘을 구분해 줘서 구글 귀속은 분명한 편이다. 다만 **기준 시점 표시가 없어 `google_as_of`는 모두 null**이다.
- 같은 가게라도 Wanderlog 페이지(스냅샷)마다 숫자가 조금씩 다르다. 원칙: **구글이라고 명시된 값 중 리뷰 수가 가장 많은(=최신으로 보이는) 값**을 썼다.
  (예: Falafel König 4.3/1,044 vs 4.4/928 → 4.3/1,044, Al Salam 4.5/1,042 vs 4.7/1,024 → 4.5/1,042, Injera 4.5/745 vs 4.8/688·4.4/666 → 4.5/745)
- 예외 1건: **Soliana**는 spinach.guide의 "Google Maps 외부 평점 4.9(145)"를 썼다(rating_source에 표기).
- werkenntdenbesten.de는 이번 검색 어디에도 잡히지 않았다. restaurantguru도 마찬가지.
- 신뢰도는 전부 `medium`(검색 요약을 통한 간접 확인, 날짜 없음).

## 국가별 결과

| 나라 | places | 비고 |
|---|---|---|
| 터키 TR | Kebapland, Kudret Kebap House, Tantuni Haus, Eat Kumpir, Oruç Kebap, Zadem, Artistanbul Meze, Öz Harran Doy Doy, Ehrenfeld Café(카페), Kilim Restaurant(뮐하임 Keupstraße) — 10곳 | 에렌펠트 벤로어 슈트라세에 집중 |
| 레바논 LB | Habibi, Lebanon Vitamin, Hayati, Beirut Restaurant, Bethlehem Oriental Kitchen — 5곳 | Habibi·Lebanon Vitamin은 할랄 |
| 시리아 SY | Popeye Falafel — 1곳 | 주소 충돌 있음(아래) |
| 이란 IR | Zarathustra, Sadaf — 2곳 | Zarathustra는 비건 메뉴 많음(HappyCow) |
| 이스라엘 IL | NENI Köln — 1곳 | Nish Nush는 숫자 미확인 → 후보 |
| 에티오피아 ET(+ER) | Fasika, Injera Restaurant, Soliana, Enat(ET·ER) — 4곳 | |
| 남아공 ZA | Shaka Zulu — 1곳 | |
| 나라 미상(중동) | Falafel König, Al Salam — 2곳 | `cuisine_country` 비우고 `cuisine_region: "middle-east"`만 지정 |

→ 나라 코드 기준 8개국(TR·LB·SY·IR·IL·ET·ER·ZA).

**못 채운 나라**: 모로코 MA(Marrakesch Palace·Medina·Argana — 구글 숫자/주소 없음), 아프가니스탄 AF(Mari 4.2/372는 주소 없음, Restaurant Kabul은 주소만 있음),
팔레스타인 PS(Bethlehem은 출처들이 레바논 요리로 분류해 LB로 둠), 쿠르드(검색 예산 부족으로 따로 못 찾음).
**지역 공백**: deutz-messe에서는 해당 음식점을 찾지 못했다. 강 건너 쪽은 Kilim(뮐하임)·Enat(칼크)뿐.

## 검증 대상 15곳 결과

| 가게 | 결과 |
|---|---|
| Kebapland (Venloer Str. 385) | ✅ 4.7 / 12,444 (Wanderlog 두 목록에서 같은 값) |
| Falafel König (Venloer Str. 384) | ✅ 4.3 / 1,044 |
| Tantuni Haus (Venloer Str. 282) | ✅ 4.6 / 381 |
| Eat Kumpir (Venloer Str. 274) | ✅ 4.6 / 1,153 (다른 페이지 4.8/1,166). PLZ 50823은 speisekarte.de로 확인 |
| Kudret Kebap House (Venloer Str. 280) | ✅ 4.5 / 7,892. 현금만 받는다는 리뷰 → `payment: cash-only` |
| Murat Grill-Imbiss & Pizzeria (Venloer Str. 464) | ❌ 구글 숫자 없음 → 후보(주소는 Lieferando로 50825 확인) |
| Habibi (Zülpicher Str. 28) | ✅ 4.5 / 4,329 |
| Oruc (Heinsbergstr. 1) | ✅ "Oruç Kebap – Das Original seit 1988", 4.6 / 2,059. 주소 Heinsbergstraße 1, 50674 |
| Ferkulum (Zülpicher Str. 37) | ❌ 4.0 / 544로 기준 미달. 게다가 그리스식 기로스 가게(범위 밖) → 후보 |
| Soliana (Subbelrather Str.) | ✅ Subbelrather Str. 242, 50825 / 4.9 / 145 (spinach.guide 경유 구글) |
| Shaka Zulu (Belgisches Viertel) | ✅ Limburger Str. 29, 50672 / 4.8 / 1,474 (다른 스냅샷 1,566~1,586건) |
| Restaurant Fabian (Venloer Str. 531) | ⚠️ 5.0 / 182로 기준은 넘지만 Wanderlog 영업시간이 매일 "Permanently closed"로 표시 → **후보**(OpenTable 예약 가능·Mit Vergnügen 2026 목록에는 있음. 상태 확인 후 승격 가능). 요리는 INT(메제풍 셰어 디시) |
| NENI Köln (Im Klapperhof 22-24) | ✅ 4.3 / 1,989. 한 목록에 "임시 휴업" 표시가 있었으나 호텔(Accor·25hours)·speisekarte.de는 정상 영업으로 안내 → 포함, tips에 확인 문구 |
| Yu*lia Mezze Bar (Kämmergasse 18) | ❌ 구글 숫자 없음 → 후보 |
| Ehrenfeld Café (Venloer Str.) | ✅ Venloer Str. 176, 50823 / 4.7 / 131 |

## 새로 찾은 곳 (places)

Zadem(링, 4.7/1,131), Artistanbul Meze(대성당 서쪽, 4.8/795), Öz Harran Doy Doy(아이겔슈타인, 4.4/2,404), Beirut Restaurant(구시가, 4.2/3,692),
Lebanon Vitamin(4.4/757), Hayati(쥐트슈타트, 4.6/939), Al Salam(아이펠플라츠, 4.5/1,042), Bethlehem Oriental Kitchen(노이에렌펠트, 4.7/362),
Popeye Falafel(4.7/237), Zarathustra(4.5/807), Sadaf(4.8/1,165), Fasika(4.6/586), Injera Restaurant(4.5/745), Enat(칼크, 4.9/396), Kilim(뮐하임, 4.3/3,248).

## 의문점·주의 (리드 확인 요청)

1. **Kudret Kebap House PLZ**: 출처에서 본 것은 "Venloer Str. 280"까지다. 50823은 바로 옆 번지 274(speisekarte.de)·282(round 1 출처)가 모두 50823이라서 **추론해 넣은 값**이다.
2. **Popeye Falafel 주소 충돌**: Wanderlog(평점이 붙은 같은 구글 장소) = Venloer Str. 468, 50825 / speisekarte.de = Subbelrather Str. 165/167, 50823.
   Wanderlog 주소를 썼고 tips_ko에 경고를 넣었다. 지오코딩 전에 확인 권장.
3. **이름 매칭으로 주소를 붙인 곳**: Sadaf(평점은 Wanderlog 목록, 주소는 speisekarte.de "Sadaf Persisches Köln"), Bethlehem Oriental Kitchen(평점은 Wanderlog, 주소 Lenauplatz 8은 speisekarte.de·speisekarte.menu).
   쾰른에 같은 이름이 또 있다는 흔적은 없었지만 직접 연결된 출처는 아니다.
4. **같은 번지에 다른 가게**: round 1 후보 "Thai Street Food"도 Venloer Str. 282(Tantuni Haus와 같음), "Asia Oma"도 Zülpicher Str. 38(Lebanon Vitamin과 같음). 한 건물에 여러 가게일 수 있지만 한쪽이 바뀌었을 가능성도 있다.
5. **휴업·폐업 표시**: Oruç Kebap·NENI는 Wanderlog 목록 한 곳에서 "Temporarily closed"(영구 폐업 아님, 다른 출처는 정상) → 포함하고 tips에 적었다. Restaurant Fabian은 "Permanently closed" 표시라 후보로 뺐다.
6. **지역 경계**: Sadaf(Jahnstraße 20, 50676 알트슈타트-쥐트)는 `kwartier-lateng`으로 두었지만 `suedstadt`/`dom-altstadt`일 수도 있다. Al Salam(Eifelplatz 4, 50677)은 `suedstadt-rheinauhafen`(Elsaßstr.와 같은 50677). Shaka Zulu(Limburger Str. 29)는 round 1처럼 `belgisches-viertel`.
7. **중복 이름**: round 1 후보 "Oruc"와 내 place "Oruç Kebap"은 같은 가게다. `norm_name`이 달라서 importer가 round 1 후보를 지우지 못한다. 리드가 정리해 주거나 이름을 맞춰 주세요.
8. **할랄**: 출처에 할랄이 명시된 곳은 Habibi(round 1 출처)와 Lebanon Vitamin(Wanderlog 요약 "halal options")뿐이다. Kilim은 할랄 디렉터리 zabihah에 등재된 것만 보였고(app.zabihah.com "kilim-kln"), 직접 확인하지 못해 diet에 넣지 않았다.
9. **정보가 얇은 place**: Zadem·Sadaf·Shaka Zulu·Fasika·Enat는 숫자·주소는 확인됐지만 대표 메뉴를 확인하지 못해 must_try를 비웠다. summary_ko에 그 사실을 적었다.
10. **기준은 넘지만 후보로 둔 곳**: Saana(Kalk, 4.2/2,711, 요리 불명), African Roasters(Sülz, 4.8/93, 카페인지 로스터리 판매점인지 불명), 그리고 주소가 없는 Büyük Harran Doy Doy(4.4/6,142)·Kumpir Haus Ehrenfeld(4.8/588)·Mersin Tantuni(4.7/417)·Sülzer Kebab(4.6/586)·EL HABAB(4.8/523)·Mangal Doner(4.2/2,725)·Mari(4.2/372).
    주소만 찾으면 바로 승격할 수 있다.
11. 시설 정보(facets)는 출처에 있는 것만 넣었다. meals·occasions가 빈 곳이 많은 것은 의도한 것이다(임비스는 `quick`만 지정). price_level은 리뷰·분류가 "저렴"을 말한 4곳(Kebapland·Habibi·Lebanon Vitamin·Hayati)만 1로 넣고 나머지는 null.

## 검색 로그 (28회)

| # | 질의 요지 | 소득 |
|---|---|---|
| 1 | Wanderlog 터키 음식 (일반 검색) | 이름만(Lalezar, Büyük Harran, Istanbul, Bosporus), Oruç 주소 단서 |
| 2 | werkenntdenbesten 터키 에렌펠트 | WKDB 없음. Eat Kumpir 주소(speisekarte), Akasya·Kervansaray |
| 3 | Wanderlog(도메인 한정) 중동·팔라펠 | Habibi 4.5/4,329, 후보 이름 다수 |
| 4 | Wanderlog 중동 50 목록, 숫자·주소 | **핵심**: 숫자 12건 + 주소 17건 |
| 5 | Wanderlog 터키 50 목록 | Zadem, Kilim·Öz Harran·Büyük Harran 숫자, Asmali Konak(임시 휴업) |
| 6 | Wanderlog 아프리카 16 목록 | Shaka Zulu·Fasika·Enat 숫자+주소, Injera 주소 |
| 7 | Wanderlog Tantuni/Eat Kumpir/Kudret/Murat | 앞의 3곳 숫자, Kumpir Haus·Mersin Tantuni |
| 8 | Wanderlog NENI/Yulia/Oruç/Fabian | NENI·Oruç·Fabian 숫자, Fabian 폐업 표시 |
| 9 | 페르시아 일반 | Sadaf·Zarathustra 주소 |
| 10 | Wanderlog Zarathustra/Damaskus/Hayati/Lebanon Vitamin | 4곳 숫자+주소 |
| 11 | Wanderlog Ehrenfeld Café/Soliana/Murat/Ferkulum | Ehrenfeld Café 주소, Ferkulum 4.0 |
| 12 | 에티오피아(Soliana/Injera) | Soliana 주소, Popeye 주소(Subbelrather) |
| 13 | 모로코 일반 | Marrakesch Palace·Medina 메뉴만 |
| 14 | Wanderlog 모로코 | 소득 없음(타 도시) |
| 15 | NENI 2026 영업 여부 | 폐업 신호 없음, 테라스·전화 예약 |
| 16 | Yu*lia 구글 숫자 | 없음 |
| 17 | Wanderlog 팔라펠 목록 | Popeye 주소(Venloer 468), Ya Salam 주소 |
| 18 | Wanderlog 아프간 | Mari 4.2/372(주소 없음) |
| 19 | Wanderlog Bethlehem/Al Salam/Mari | Al Salam·Bethlehem 숫자 |
| 20 | Bethlehem 주소 | Lenauplatz 8, 50825 |
| 21 | Fabian 2026 상태 | OpenTable(€31–50, 4.8/18), 2026 영업시간 없음 |
| 22 | Soliana 구글 숫자 | 4.9/145(spinach.guide → Google Maps) |
| 23 | Murat Grill 숫자 | 주소만(Lieferando) |
| 24 | Wanderlog Kilim/Büyük Harran/Kudret | Kilim 주소(Keupstraße 69) |
| 25 | Wanderlog Injera/Nish Nush/Ya Salam | Injera 4.5/745 |
| 26 | Mari 주소 | 없음. Restaurant Kabul 주소(Elsaßstr. 32), Bamiyan |
| 27 | Wanderlog Kabul/Bamiyan/Nish Nush | 소득 없음(뮌헨) |
| 28 | Restaurant Kabul 구글 숫자 | Cylex 정보만 |

## 주요 출처

- Wanderlog 목록: 터키 https://wanderlog.com/list/geoCategory/779752/best-turkish-foods-and-restaurants-in-cologne ·
  중동 https://wanderlog.com/list/geoCategory/763561/best-middle-eastern-foods-and-restaurants-in-cologne (주소판 https://app.wanderlog.com/list/geoCategory/763561/best-middle-eastern-foods-and-restaurants-in-cologne) ·
  레바논 https://wanderlog.com/list/geoCategory/788747/best-lebanese-foods-and-restaurants-in-cologne ·
  아프리카 https://wanderlog.com/list/geoCategory/797742/best-african-foods-and-restaurants-in-cologne ·
  팔라펠 https://wanderlog.com/list/geoCategory/1794415/best-spots-for-falafel-in-cologne ·
  저렴한 맛집 https://wanderlog.com/list/geoCategory/20723/best-cheap-eats-in-cologne
- Wanderlog 장소 페이지: 각 place의 `sources` 참고(Tantuni Haus, Eat Kumpir, Kudret, Oruç, NENI, Fabian, Lebanon Vitamin, Hayati, Zarathustra, Damaskus Haus, Ferkulum, Ehrenfeld Cafe, Popeye, Al Salam, Bethlehem, Injera, Kilim, Mari 등)
- spinach.guide Soliana https://spinach.guide/venues/soliana-fusion-home-cooking-35154/
- speisekarte.de / speisekarte.menu: Eat Kumpir, Sadaf, Zarathustra, Bethlehem, Popeye, NENI, Marrakesch Palace, Medina
- OpenTable Fabian https://www.opentable.com/r/restaurant-fabian-koln · Accor 25hours The Circle https://all.accor.com/hotel/b0c9/index.de.shtml
- Mit Vergnügen 2024–2026 목록(Ehrenfeld·Venloer Str.·Kwartier Latäng·Belgisches Viertel·Neuentdeckungen 11/2024), Renk Magazin 2021(아카이브), Falstaff, tablejourney, Cylex(Restaurant Kabul), Lieferando(Murat Grill)
