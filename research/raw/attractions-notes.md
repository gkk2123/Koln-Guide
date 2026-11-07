# 관광지 조사 노트 (agent: attractions, 2026-11-07)

## 0. 조사 방법과 한계 — 먼저 읽어 주세요
- WebFetch는 1회 시도했으나 네트워크 정책으로 차단(koelner-dom.de ENOTFOUND). 이후 WebSearch만 사용.
- WebSearch는 약 37회 사용 후 **세션 공용 한도(200회)가 소진**되어 이후 모든 검색이 실패했습니다. 코디네이터가 "한도 리셋"을 알렸지만 제 턴에서는 재시도 3회가 모두 같은 오류로 실패했습니다.
- 그래서 `attractions.json`은 다음처럼 나눴습니다.
  - `places`(28): 이번 세션 검색 결과로 가격·시간·2026 상태를 확인한 곳 + 날짜가 달력 계산으로 확정되는 카니발 일정 3건.
  - `candidates`(46): 검색하지 못한 곳(공공 공간·공원·체험·쇼핑·성문·밤문화 지역·크리스마스 마켓·당일치기·일부 박물관). 이름·지역·주소·한 줄 설명은 넣었고 가격·시간·상태는 비웠습니다.
    - `reason: unverified-public-space`: 무료 상시 개방 공간(다리·광장·거리·공원·성문 외관). 2026 공사·통제만 빠르게 확인하면 승격해도 위험이 낮습니다.
    - `unverified-2026-dates` / `unverified-2026-status` / `unverified-2026`: 반드시 검색으로 확인한 뒤 승격해야 합니다(특히 크리스마스 마켓 날짜, 케테 콜비츠·동아시아 미술관·오디세움 상태, 케이블카 시즌, 아르 계곡 철도).
- 구글 평점은 한 건도 확인하지 못해 모두 `null`입니다. lat/lng도 모두 `null`입니다.
- 주소 중 일부(Heinrich-Böll-Platz, Obenmarspforten 21/40, Am Schokoladenmuseum 1A, An Groß St. Martin 9, Kunibertsklostergasse 2, Am Pantaleonsberg 2, Domkloster 3)는 검색 결과 본문이 아니라 일반 지식으로 적었습니다. 지오코딩 전 한 번 대조해 주세요.

## 1. 2026년 상태 핵심 (여행 일정에 직접 영향)
| 장소 | 2026-11 상태 | 근거 |
|---|---|---|
| 쾰른 대성당 | **2026-07-01부터 관광 입장 유료 €12**(할인 €6, 13세 이하 무료). 미사·기도(북쪽 익랑)는 무료 | koelner-dom.de 공지, 티켓 플라이어 PDF, evangelisch.de(2026-06-02), web.de |
| 대성당 탑 / 보물관 | 각 €8(할인 €4), 탑+보물관 콤비 €12(할인 €6). 콤비에 성당 내부 관광은 미포함 | koeln.de, hotel-lyskirchen.de (일부 언론은 "탑·보물관에도 같은 요금"이라고 써서 상충 → 공식 확인 필요) |
| 발라프 리하르츠 미술관 | **휴관**(2026-08-03~2028년 중반/말) | stadt-koeln.de 보도자료, wallraf.museum |
| 로마-게르만 박물관 | **임시관** Belgisches Haus, Cäcilienstraße 46. 수–월 10–18, **화 휴관**, €6 | stadt-koeln.de, koeln.de |
| 쾰른 시립 역사박물관 | **임시관** Minoritenstraße 13(옛 Franz Sauer), 2024-03 재개관, €5 | stadt-koeln.de 보도자료 |
| MiQua | **공사 중**. 인도 2028년 4분기 목표, 개관 2029년 중반 예상(2026-02 기준) | de.wikipedia(Archäologische Zone), wz.de, MiQua:forum 2026 Q4 프로그램 |
| MAKK | 개관 중이나 **역사 컬렉션 수년간 휴관**, 디자인전·특별전만 | stadt-koeln.de, makk.de 월간 프로그램 |
| 초콜릿 박물관 | 매일 10–18, 단 **2026-11-02·09·16(월) 휴관**, 12/24·25 휴관, 12/31 10–16 | schokoladenmuseum.de(plan a visit) |
| NS 기록센터 | 개관(화–금 10–18, 주말 11–18). 상설전·공용 공간 리뉴얼 계획 있음 | bpb.de, 2024/25 연례보고서 |
| 케테 콜비츠 미술관 / 동아시아 미술관 / 오디세움 | **미확인**(검색 한도 소진) | — |

기타 시기 정보: ART COLOGNE 2026-11-05~08(미술관 연장 개관), St. Gereon 오르간 콘서트 2026-11-15 17:00(€15), 루트비히 미술관 매월 첫째 목요일 22시까지.

## 2. 대성당 방문 규정 (요청 항목)
- **요금(2026-07-01~)**: 관광 €12 / 할인 €6(14세 이상 학생·직업훈련생·대학생 등) / 13세 이하 무료. 미사 참석과 개인 기도(Nordquerhaus)는 무료.
- **무료일**: 1월 6일(주현절)~그다음 일요일, 5월 1일, 10월 3일, 동방박사 순례(Dreikönigswallfahrt) 기간 → 이번 여행 범위에선 **2027-01-06(수)~01-10(일)**.
- **티켓**: tickets.koelner-dom.de(최대 3개월 전 예매), 현장 매표소 Roncalliplatz 2 Kurienhaus.
- **관람 시간**: 관광 관람 월–토 10:00–17:45(마지막 입장 17:30), 일·공휴일은 오후만(구 자료 13:00–16:30). 성당 자체(기도)는 06:00–20:00로 소개되는 자료도 있음. 미사 중 관람 제한. 출처 간 차이가 있어 공식 사이트 재확인 필요.
- **탑**: 533계단, 엘리베이터 없음, 약 97m. 3–10월 9–18시, 11–2월 9–16시(제3자 자료).
- **복장**: 공식 복장 규정은 찾지 못함. 예배 공간이므로 단정한 복장·모자 벗기·정숙을 권장(관광 페이지 수준의 약한 근거).
- 출처: koelner-dom.de/aktuelles/…, api.koelner-dom.de 티켓 플라이어, evangelisch.de, web.de, welterbetour.de(opening hours), koeln.de.

## 3. 실용 정보 (요청 항목 — 대부분 미검증)
| 항목 | 상태 | 메모 |
|---|---|---|
| KölnCard 2026 가격 | **미검증** | 검색 한도 소진으로 조회 못함 |
| KVB 단일권(Einzelticket) 2026 | **미검증** | 조회 못함 |
| Deutschlandticket 2026 | **미검증** | 일반 지식(미검증): 2026-01부터 월 €63으로 인상 결정. 반드시 확인 |
| 일요일 상점 휴무 | 일반 지식(출처 미검색) | NRW 상점법상 일요일·공휴일은 대부분 상점 휴무. 중앙역 내 상점·빵집 일부·주유소·키오스크는 영업. 연 몇 차례 '쇼핑 일요일(verkaufsoffener Sonntag)' 예외 |
| 소매치기 주의 지역 | 일반 지식(출처 미검색) | 중앙역·Domplatte(대성당 앞 광장), 크리스마스 마켓 혼잡 구간, Hohe Str./Schildergasse, 카니발 군중, 붐비는 전차. 가방은 앞으로, 휴대폰은 안주머니 |

## 4. 지역(area id) 한 줄 소개 — 성격 / 이런 사람에게
※ 일반 지식 기반 서술(이번 세션 검색으로 확인한 내용 아님).
- `dom-altstadt` 대성당·구시가: 대성당·박물관·브라우하우스·강변이 몰린 관광 중심. 혼잡하고 관광객 가격이지만 동선이 가장 짧다. → 첫 방문, 짧은 일정, 교통 편의 중시.
- `belgisches-viertel` 벨기에 지구: 19세기 건물 사이 부티크·카페·칵테일 바가 모인 세련된 동네, 저녁엔 브뤼셀 광장에 사람이 모인다. → 쇼핑·카페·데이트, 현지 분위기.
- `friesenviertel-ehrenstrasse` 프리젠 지구·에렌슈트라세: 스트리트 패션 쇼핑(에렌슈트라세)과 오래된 펍·클럽이 섞인 링 북쪽 구간. → 쇼핑과 밤 외출을 한 동네에서.
- `kwartier-lateng` 크바르티어 라텡(쥘피허 지구): 대학가. 저렴한 바·식당, 늦게까지 북적이며 카니발 때는 인파의 중심. → 학생 같은 밤문화, 가성비. 조용한 숙박을 원하면 비추천.
- `ehrenfeld` 에렌펠트: 옛 공장 지대가 그라피티·클럽·다국적 음식점 동네로 변신. → 힙한 동네 탐방, 클럽·라이브 공연, 다양한 음식.
- `suedstadt-rheinauhafen` 쥐트슈타트·라인아우하펜: 동네 'Veedel' 감성의 쥐트슈타트와 크란하우스·초콜릿 박물관의 신식 항구 지구. → 강변 산책, 가족 여행, 현지 술집.
- `agnesviertel-eigelstein` 아그네스 지구·아이겔슈타인: 중앙역 북쪽, 다문화 상점가(아이겔슈타인)와 조용한 주거지(아그네스 지구). → 중앙역 가까운 실속 숙소, 로컬 식당.
- `deutz-messe` 도이츠·메쎄: 라인강 건너편 박람회·공연장 지역. 대성당 야경을 정면으로 보는 강변과 전망대. → 박람회 출장, 야경 사진, 공연 관람.
- `other` 기타 시내: 동물원·식물원(리엘), 니페스 장터, 멜라텐 묘지 등 흩어진 명소. → 시간 여유가 있는 재방문자.
- `day-trip` 근교 당일치기: 본·브륄·뒤셀도르프·아헨·라인 계곡 등 열차로 1시간 안팎. → 3일 이상 머무는 여행자.

## 5. 후보(candidates)로 보류한 것 — 승격 전 확인할 항목
- **크리스마스 마켓 2026(최우선)**: Dom(Roncalliplatz), Markt der Engel(Neumarkt), Heimat der Heinzel(Heumarkt/Alter Markt, 아이스링크 포함), Nikolausdorf(Rudolfplatz), Hafen-Weihnachtsmarkt(초콜릿 박물관 앞), Stadtgarten → 2026 개장·종료일, 영업시간, 12/24~26 휴무 여부. 새해 이후 운영하는 아이스링크·윈터 이벤트도 확인.
- **카니발**: 11.11 개막 무대(Heumarkt)·쥘피허 통제 방식, 2027 로젠몬탁 퍼레이드 경로·시작 시각.
- **박물관 상태**: 케테 콜비츠(리노베이션 후 재개관 여부), 동아시아 미술관, 오디세움(운영 여부).
- **체험**: KD 유람선 겨울 운항·요금, 케이블카 2026 시즌(겨울 휴업 여부), 동물원 요금, 쾰른트라이앵글 전망대 요금·시간, 플로라 개방 시간, 브라우하우스 투어 운영사.
- **당일치기**: 쾰른 중앙역 기준 열차 종류·소요 시간(travel_time_min), 브륄 궁전 겨울 개방, 드라헨펠스 산악열차 겨울 운행, 아르 계곡 철도 복구 상태, 중부 라인 겨울 유람선.
- **실용 정보**: KölnCard·KVB 단일권·Deutschlandticket 2026 가격.

## 6. 열린 의문
- 대성당 관광 관람 시간: "월–토 10:00–17:45 / 일 오후"와 "매일 9:00–17:30" 등 출처가 엇갈림. 탑·보물관 요금이 새 입장료와 별도인지(대부분 별도)도 한 언론과 상충.
- 초콜릿 박물관 성인 요금: €15.50·16.50·17.50·19 등 출처마다 다름(평일/주말 차등 가능성).
- 콜룸바: 영업 시간(수–월 12–17 vs 화–일 11–18)과 요금(€8 vs €10) 상충.
- 쾰른 시립 역사박물관 영업 시간 두 가지 버전.
- NS 기록센터 요금(€4.50)은 여행 사이트 기준, 리뉴얼로 부분 휴관 가능성.
- 로마-게르만 박물관 임시관이 2026년 이후에도 유지되는지(본관 재개관 시점) 미확인.

## 7. 주요 출처
- 대성당: https://www.koelner-dom.de/aktuelles/aktuelle-information-zur-oeffnung-des-koelner-domes · https://tickets.koelner-dom.de/en · https://api.koelner-dom.de/uploads/Dom_Ticket_Flyer_05_ON_5b22f02690.pdf · https://www.evangelisch.de/inhalte/256000/02-06-2026/touristen-muessen-kuenftig-zwoelf-euro-eintritt-fuer-koelner-dom-zahlen · https://web.de/magazine/reise/eintritt-koelner-dom-touristen-kuenftig-wissen-42020018 · https://www.koeln.de/tourismus/stadtfuehrungen/dachfuehrung-dom/ · https://www.hotel-lyskirchen.de/sehenswuerdigkeiten/koelner-dom/
- 성당: https://www.romanische-kirchen-koeln.de/fileadmin/user_upload/FvRK_Fuehrungen2026_260405_WEB.pdf · https://www.nomadotravel.app/de/attractions/st-gereon-basilica · https://www.nrw-tourism.com/architecture/st-maria-im-kapitol · https://www.travelbook.de/orte/st-ursula-knochenkirche-koeln
- 박물관: https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/28476/index.html (발라프 휴관) · https://www.stadt-koeln.de/service/adressen/00081/index.html (RGM) · https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/26718/index.html (시립 역사박물관) · https://de.wikipedia.org/wiki/Arch%C3%A4ologische_Zone_K%C3%B6ln (MiQua) · https://www.schokoladenmuseum.de/en/plan-a-visit/ · https://www.koeln.de/veranstaltungsort/museum-ludwig-koeln/ · https://www.stadt-koeln.de/service/adressen/00274/index.html (MAKK) · https://www.bpb.de/themen/holocaust/erinnerungsorte/502992/ns-dokumentationszentrum-der-stadt-koeln-im-el-de-haus/
- 카니발 날짜: 부활절 2027-03-28 기준 계산(Weiberfastnacht 02-04, Rosenmontag 02-08, Aschermittwoch 02-10), 11.11.2026 = 수요일. 공식 일정(koelnerkarneval.de)으로 재확인 권장.
