# 와인 조사 노트 (agent: wine-guide / wine-places) — 2026-11-07

## 0. 상태 요약 (리드가 먼저 볼 것)

| 산출물 | 상태 |
|---|---|
| `guides/german-white-wine.md` | **완성** (16개 절, 약 650줄). 법규·통계·빈티지·한국 면세는 세션 출처 기반. 이동 시간·생산자·가격대·젝트/글뤼바인 세부·포장 요령은 **† 표시(미검증 일반 지식)** |
| `research/raw/wine-guide-data.json` | **완성** (품종 12, 산지 13, 용어 59, 출처 80). `meta.unverified_fields`에 미검증 필드 명시 |
| `research/raw/wine-places.json` | **미완** — `places` 0곳, `candidates` 4곳(검증 안 된 리드뿐) |
| 이 노트 | 완성 |

**결정적 제약**
1. **WebFetch 차단**: `www.vdp.de` → `getaddrinfo ENOTFOUND`. 브리프 지침대로 1회만 시도하고 다시 쓰지 않음.
2. **WebSearch 공유 한도(턴당 200회) 소진**: 30번째 검색 이후 거부됨. 코디네이터가 "한도 리셋, 최대 15회 추가 가능"이라고 알린 뒤에도 쾰른 와인 장소 검색 3회가 모두 같은 사유로 거부됨(총 거부 6회). 그래서 **쾰른 와인 바·와인숍의 구글 평점은 하나도 확인하지 못했고**, 이동 시간·생산자 가격 검증도 못 했다.
3. 후속 조사 시 우선순위: (1) 와인 장소 구글 수치 → (2) 쾰른발 기차 시간 → (3) 젝트·글뤼바인·페더바이서 규정 → (4) 생산자 가격대. 아래 6절에 쿼리 목록을 정리했다.

## 1. 실제로 수행한 검색 (30회 성공 + 6회 거부)

1. deutscheweine.de Geschmacksangaben trocken halbtrocken lieblich süß Restzucker g/l feinherb
2. Weingesetz 2021 Herkunftspyramide … Deutsches Weininstitut
3. VDP Klassifikation Gutswein Ortswein Erste Lage Grosse Lage Grosses Gewächs vdp.de
4. 관세청 여행자 휴대품 면세 주류 2병 2리터 400달러 2026
5. Korea Customs Service traveler duty free allowance alcohol 2 bottles 2 liters US$400 2025 2026
6. vdp.de "VDP.Grosse Lage" "VDP.Erste Lage" … Ertrag Handlese
   - (WebFetch https://www.vdp.de/en/the-wines/classification → ENOTFOUND)
7. 주류 면세 병수 제한 폐지 관세법 시행규칙 시행 2025년 3월 2리터 400달러 기획재정부
8. Prädikatswein Mindestmostgewicht Oechsle Kabinett … Eiswein Mosel Rheingau Tabelle
9. germanwines.de 13 wine regions vineyard area hectares 2024 …
10. Wines of Germany new German wine law 2021 origin pyramid Großlage Region … 2026 vintage
11. Weinrecht 2021 Lagenwein Handlese Mindestmostgewicht Kabinett Ortswein … Jahrgang 2025
12. German wine law 2021 "Erste Lage" "Große Lage" legally protected terms Weinverordnung 2025 2026
13. meininger "Rechtsrahmen für GG und 1G steht"
14. Dreizehnte Verordnung zur Änderung weinrechtlicher Vorschriften 2026 Bundesrat GG 1G Classic Crémant
15. Regierungspräsidium Darmstadt Weinbezeichnungsrecht ab Ernte 2026 …
16. Deutsches Weininstitut Statistik 2025 Rebsorten Rebfläche …
17. germanwines.de grape varieties white Riesling Silvaner Müller-Thurgau …
18. deutscheweine.de Scheurebe Gewürztraminer Gutedel Elbling Kerner …
19. tageskarte "Weißweinsorten weiter auf dem Vormarsch" …
20. DWI Rebsortenstatistik 2025 Riesling … Müller-Thurgau Grauburgunder …
21. Wines of Germany Riesling "percent of the world's Riesling" …
22. vinetur "Germany's vineyards tilt further toward white wine" 2026 …
23. Weinjahrgang 2025 Deutschland Bilanz Deutsches Weininstitut …
24. German vintage report 2024 2023 2022 Riesling …
25. German Riesling vintages 2019 2020 2021 assessment …
26. 2025 vintage Germany Riesling early harvest September rot … Decanter/Wine Spectator/Meininger
27. Weinlese 2025 Mosel Bilanz …
28. winesofgermany.com "The 2025 vintage in the 13 wine-growing regions" …
29. Wines of Germany 2024 vintage "13 wine-growing regions" frost …
30. "Great vintage after turbo harvest" Wines of Germany 2025
31–33. (거부) Köln→Cochem / Köln→Bad Neuenahr-Ahrweiler(Ahrtalbahn 복구 상태) / Köln→Rüdesheim·Bacharach·Bad Kreuznach 기차 시간
34–36. (거부, 리셋 안내 후) werkenntdenbesten Weinbar Köln / best wine bars Cologne Google rating / Köln Weinbar Tipp (KStA·Mit Vergnügen·koeln.de)

## 2. 확인된 핵심 사실과 근거

- **당도 표기**: trocken ≤4 g/l(잔당이 총산보다 2 g/l 넘게 많지 않으면 ≤9), halbtrocken ≤12(산도 조건 시 ≤18), lieblich ≤45, süß >45. feinherb는 법정 용어가 아님. 근거는 infranken.de·antwort.net·alleantworten.de 같은 **소비자·사전형 사이트**뿐이고 법령 원문은 아님(값은 EU 규정과 일치한다고 판단). halbtrocken의 산도 조건(총산이 잔당보다 10 g/l 넘게 낮지 않을 것)은 구체 수치 출처를 못 찾아 본문에는 "산도 조건 충족 시"로만 썼다.
- **2021 개혁**: 개정법 2021-01-27 발효, 시행령 2021-03-26 연방참사원 승인·2021-05-07 공포. 피라미드는 Deutscher Wein → Landwein(g.g.A., 26개) → g.U.(Gebiets-/Regional-/Orts-/Lagenwein). 과도기는 2025 빈티지까지이고 2026 빈티지부터 의무(LWG 바이에른, RP 다름슈타트, RP 슈투트가르트 자료와 다수 해설). 그로스라게·Bereich 이름 앞에 "Region"을 같은 서체·색·크기로 표기해야 하고, Leitgemeindenprinzip은 폐지. Lagenwein은 허용 품종만, 최소 Kabinett 당도, 이듬해 3월 1일 이후 판매(Meininger). 라인헤센은 2026 수확부터 Lagenwein 허용 품종을 6개로 정함.
- **GG·1G 법제화**: 2021년 헤센 주 제안으로 시행령에 용어가 들어갔고 2024 빈티지부터 규칙이 적용됨(Meininger). 법정 GG는 드라이 필수이고 Prädikat 병기 불가(Jancis Robinson, NVWA). DWV·VDP 공동 위원회가 Erste·Große Lage를 분류(Meininger "Rechtsrahmen für GG und 1G steht", **기사 날짜 미확인**).
- **13차 개정령**: 연방참사원 2026-06-12 동의(Drs. 272/26), 2026-08-24 서명, 2026-09-01 BGBl. 2026 I Nr. 243 공포. 다만 Bundesrat 문서 요약은 주로 WeinÜV·WeinFöGewV·LMZDV 변경을 다루고, Vinetur(2026-09-04)는 Classic·1G·GG·Crémant 표기 개정(9/2 시행)을 보도 → **같은 개정령인지, 내용이 무엇인지 원문으로 확인하지 못함.** 본문에는 "보도"로만 적었다.
- **VDP**: 회원 약 200곳, 2012 빈티지부터 4단계(노이슈타트 임시총회 만장일치). 드라이 최상급은 GG(GG 로고), Erste Lage 드라이는 1G. 수확량 75/60/50 hl/ha와 상위 2단계 손수확은 **2017년 자료**라 현행 여부 불확실. 라인헤센 Erste Lage는 2022 빈티지부터 포도밭명·전용 캡슐. GG는 매년 9월 초 출시(Drinks Business 2026-08).
- **Prädikat 머스트 당도**: Kabinett 약 67–82, Spätlese 76–90, Auslese 83–100, BA·Eiswein 110–128, TBA 150–154 °Oe(Wikipedia, ProWein). 2025년 Prädikatswein 비율 29.3%(전년 16.1%, Destatis 기반 Tageskarte).
- **통계**: 2025년 포도밭 약 102,000 ha이고 화이트 약 70%(DWI, Vinetur 2026-05). 리슬링은 2023년 24,388 ha(23.5%), 2024년 24,233 ha로 세계의 약 45%(WoG). 2023년 Müller-Thurgau 10,738, Grauburgunder 8,372, Weißburgunder 6,318, Silvaner 4,330, Chardonnay 2,912 ha. Sauvignon Blanc 약 1,900 ha(2022). PIWI 약 4,000 ha(2025).
- **빈티지**: 본문 9절 표 참고(WoG 2024·2025 지역 보고, Jancis Robinson, Suckling, Justerini, Decanter, Meininger, Vinetur, Harpers).
- **한국 면세**: 2025-03-21부터 병 수 제한이 폐지되고 2 L·US$400는 유지(기재부 시행규칙 개정 보도: 세정신문, SBS Biz, 스마트투데이). 일반 US$800과 별도. 초과 시 전액 과세(한국경제 2025-10). 2026년 기준도 동일(yellowit 2026, Air Traveler Club "as of October 2026"). 만 19세 미만 면세 없음, 자진신고 30% 감면은 해외 2차 사이트 근거. **관세청 원문은 열람하지 못함.**

## 3. 의문점·불일치

- Kabinett 최저 당도가 출처마다 67/70/73 °Oe로 엇갈림. 모젤과 라인가우 값이 서로 뒤바뀌어 보이는 자료도 있다. Meininger "Niedrigere Öchsle-Hürden" 기사(미열람)로 보아 최근 개정이 있었을 수 있음 → 본문은 범위로만 표기.
- Ortswein에 Kabinett급 당도가 필요한지는 블로그와 Meininger가 엇갈림 → 본문에 "확정 못 함"으로 명시.
- 과도기 종료를 "2025 빈티지부터 의무"로 쓴 자료(Substack)가 있음 → 다수설(2026 빈티지 의무)을 채택.
- "Kabinett trocken·Spätlese trocken이 2021 개혁 후 불가"라는 주장(1개 출처)은 검증 불가라 본문에서 제외. 본문의 "Spätlese trocken" 예시는 일반 개념 설명.
- 리슬링 면적은 Destatis 최신 열 23,885 ha(연도 불명), Meininger 23,700 ha(2016) 등 제각각 → WoG/DWI의 연도 명시 수치를 사용.
- Müller-Thurgau는 10,738(2023) / 10,511(Decanter, 연도 불명) / Destatis 약 10,230(최신 열). 전체 품종 순위에서는 Spätburgunder가 Müller-Thurgau보다 클 수 있어 본문에 "화이트 2위"로만 표기.
- 산지 면적은 연도·출처가 섞여 있음(모젤 8,287 ha와 미텔라인 439 ha는 winewithseth 위키, 팔츠 23,640 ha는 표현이 모호, 라인가우 3,180 ha는 레이아웃 깨진 스니펫이라 미사용). 바덴·프랑켄·나에·헤시셰 베르크슈트라세 면적은 못 찾음.
- Kerner "1969년 육성"이라는 출처 표현은 품종 보호 연도와 혼동한 것으로 보여 연도를 생략.
- 2024년 라인가우 서리 피해 규모가 출처마다 다름. 2025년 생산량은 DWI 730만 hl, Destatis 755만 hl.
- Meininger "VDP Riesling GG 2025 – 59개 세계적 수준" 기사가 2025년 빈티지인지 2025년 시음(2024 빈티지)인지 불분명해 사용하지 않음.
- 한국 면세: 일부 해외 가이드의 '1 L' 표기는 오류·구정보로 판단. 자진신고 감면 한도(금액)는 미확인.

## 4. † 미검증 항목 (본문에서 † 표시, 게시 전 검증 권장)

- 3절·JSON `from_koeln`의 **모든 기차 이동 시간**(DB 시간표 미확인). Ahrtalbahn 복구·운행 구간도 미확인.
- 8절 **생산자·포도밭·가격대 표 전체**와 14절 **추천 10병 가격**. 세션 출처에 이름이 나온 곳은 Dr. Loosen, Weiser-Künstler, Julian Haart, Weinhof Herrenberg, Künstler, Balthasar Ress, Eva Fricke, Wegeler, Dönnhoff, Christmann, Westhofener Morstein(Wittmann/Keller)뿐.
- 2절의 일부 향 묘사, 품종별 가격 팁, Bocksbeutel, Gutedel=Chasselas, Elbling(오버모젤·고대 품종·젝트 원료), Ahr=레드 중심, 2021년 아르 홍수, Mittelrhein UNESCO·Drachenfels(최북단), 라인가우 남향 비탈·수도원, 나에 토양.
- 4절 A.P.-Nr.가 Qualitätswein에도 적용된다는 점(Prädikat 쪽만 세션 출처 있음), Prädikat 보당 금지, Eiswein 정의.
- 5절 VDP 독수리 캡슐, 화이트 GG의 "수확 이듬해" 출시, VDP의 Prädikat 사용 관행.
- 6절 edelsüß 정의, "저알코올이면 잔당 가능성" 요령, 젝트 당도 체계.
- 7절 Gutsabfüllung 정의, A.P.-Nr. 끝자리 = 검사 연도, EU e-라벨.
- 10절 젝트 표기(Deutscher Sekt / Sekt b.A. / Winzersekt), 페더바이서 제철·운반, 글뤼바인(화이트·mit Schuss·Tassenpfand·마켓 기간), 바인쇼를레.
- 11절 0,25 l Viertel, Eichstrich, 와인 리스트 정렬 관행.
- 13절 매장 유형별 가격, 포장 요령, 액체 규정·STEB, Tax Free, 자진신고 감면 한도, 면세점 구매분 합산.

## 5. 쾰른 와인 장소 (wine-places.json)

- 검증된 장소 **0곳**. 구글 평점·리뷰 수를 하나도 확인하지 못했으므로 브리프 규칙상 `places`에 넣을 수 없음.
- `candidates` 4곳(Wein am Rhein, Henne.Weinbar, Sorgenfrei, Kölner Weinkeller)은 **배경지식 기반 리드**다. 주소 필드는 비워 두었고 기억나는 거리 이름만 reason에 "기억(미검증)"으로 적음. 폐업·이전 가능성이 있으니 반드시 확인할 것.
- 일반 체인(Jacques' Wein-Depot 등)은 브리프의 "체인 지양" 원칙에 따라 후보에서 제외하고 가이드의 매장 유형 설명에만 언급.

## 6. 후속 조사용 쿼리 제안 (검색 한도 회복 시)

장소(목표 10–15곳, 가격대·지역 분산):
- `werkenntdenbesten Weinbar Köln` / `werkenntdenbesten Weinhandlung Köln` (google.de 점수·리뷰 수·Stand 날짜)
- `restaurantguru wine bars Cologne Google rating` / `wanderlog best wine bars Cologne`
- `Mit Vergnügen Köln Weinbars` / `Kölner Stadt-Anzeiger beste Weinbars Köln 2025` / `koeln.de Weinbar`
- 개별 확인: `"Wein am Rhein" Köln Johannisstraße`, `Henne Weinbar Köln Pfeilstraße`, `Sorgenfrei Köln Antwerpener Straße`, `Kölner Weinkeller Stolberger Straße Bewertungen`, 각 이름 + `geschlossen` / `2026`
- 독일 와인 특화: `Köln Weinbar Riesling deutsche Weine`, `Köln Weinhandlung deutsche Winzer Mosel`, `Köln Naturwein Bar`(natural-wine 태그 후보)
- Michelin/Falstaff/Feinschmecker 와인 리스트 언급 레스토랑: `Falstaff Weinbar Köln`, `Feinschmecker Weinbar Köln`

사실 확인:
- `DB Köln Hbf Cochem Fahrzeit`, `Köln Bad Neuenahr-Ahrweiler Zug Ahrtalbahn 2026`, `Köln Rüdesheim Zug`, `Köln Bacharach Zug`
- `Winzersekt Definition Flaschengärung Weinverordnung`, `Sekt b.A. Deutscher Sekt Unterschied`
- `Federweißer Verkauf Zeitraum Regel`, `Kölner Weihnachtsmärkte 2026 Termine Glühwein Preis Tassenpfand`
- `관세청 여행자 휴대품 주류 면세 2리터 400달러` (customs.go.kr 원문)

## 7. 쾰른 관찰 (배경 메모, 미검증)

- 쾰른은 쾰시 맥주 문화가 압도적이라 Brauhaus에서는 와인 선택지가 적다. 독일 와인을 즐기려면 와인 바·와인 리스트가 좋은 레스토랑·와인 전문점으로 가야 한다는 점을 가이드에 적었다.
- 11월 방문객이라면 페더바이서는 끝물이고, 크리스마스 마켓 글뤼바인(화이트 포함)과 11월 성 마르틴 축일 거위 요리(Martinsgans) 페어링이 시즌 포인트다. 2025 빈티지 Gutswein이 매장에 깔려 있고, 2025 화이트 GG는 2026년 9월 출시분이다.

## 8. 주요 출처

전체 목록은 `guides/german-white-wine.md` 16절과 `wine-guide-data.json`의 `sources`(80개)에 있다. 핵심 출처는 아래와 같다.
- Wines of Germany(2025·2024 빈티지 지역 보고, wine law, Riesling) · germanwines.de · deutscheweine.de Riesling PDF
- RP Darmstadt(Weinbezeichnungsrecht ab Ernte 2026), LWG Bayern, Bundesrat Drs. 272/26, Bundesregierung
- Meininger(Weinrecht, GG/1G 법적 틀, 라인헤센 Lagen 품종, VDP 피라미드), Jancis Robinson, Decanter, Falstaff, Drinks Business, James Suckling, Justerini & Brooks, Wine Spectator
- Destatis, DWI 수치 보도(Vinetur, Tageskarte, Lebensmittelpraxis)
- 세정신문·SBS Biz·스마트투데이·한국경제(한국 면세)
