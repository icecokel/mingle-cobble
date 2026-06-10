# Server Concept

마지막 갱신: 2026-06-10

`icecoke-cobblemon`은 `icenux-ms7b23`에서 실행하는 개인용 Minecraft/Cobblemon 게임 서버다. 현재 목표는 공개 서버가 아니라, 개인이 안정적으로 접속해 장기 플레이할 수 있는 Cobblemon 월드를 유지하는 것이다.

## 한 줄 정의

외부 공개보다 월드 보존과 안정성을 우선하는 개인용 Cobblemon 서버.

## 현재 서버 라인

현재 플레이 기준은 `icecoke-cobblemon-173`이다. 기존 1.6.1 서버는 `icecoke-cobblemon-161` 레거시 보존 라인으로 남긴다.

| 항목 | 173 현재 라인 | 161 레거시 라인 |
| --- | --- | --- |
| 역할 | 현재 플레이/검증 기준 | 보존, 비교, 롤백 참고 |
| 서버 디렉터리 | `/home/icenux/minecraft/icecoke-cobblemon-173-test` | `/home/icenux/minecraft/mingle-lounge` |
| 표시명/MOTD | `icecoke-cobblemon-173` | `icecoke-cobblemon-161` |
| LAN 접속 | `192.168.219.110:25566` | `192.168.219.110:25565` |
| screen | `icecoke-173` | `mingle-sample` |
| Minecraft | `1.21.1` | `1.21.1` |
| Fabric Loader | server `0.17.3` | `0.16.14` |
| Cobblemon | `1.7.3` | `1.6.1` |
| 활성 서버 모드 | 58개 | 90개 |

173 라인의 실제 서버 디렉터리에는 과거 테스트 인스턴스 이름인 `icecoke-cobblemon-173-test`가 남아 있다. 안정성을 위해 파일 이동은 하지 않고, 표시명과 운영 명칭만 `icecoke-cobblemon-173`으로 사용한다.

## 현재 목적

- Cobblemon 1.7.3 기준 장기 플레이 월드를 운영한다.
- 서버 운영을 CLI와 문서 기준으로 단순하게 유지한다.
- 새 기능보다 접속 안정성, 월드 보존, 백업 가능성을 우선한다.
- 관장, 데일리 보상, Hermes 답변처럼 개인 플레이에 의미 있는 기능만 작게 붙인다.
- 포트포워딩, 도메인, 공개 서버 정책은 현재 범위에 넣지 않는다.

## 현재 기능 범위

| 영역 | 173 현재 라인 상태 |
| --- | --- |
| 기본 플레이 | 접속, 월드 진입, 전투 1회, 포획 1회 확인 |
| 사망 보호 | `keepInventory=true` 유지 대상 |
| 지도 | 로컬 Xaero 미니맵/월드맵 사용, 포켓몬 이름 표시 |
| 아이템 검색 | 로컬 173 프로필에 JEI 적용 |
| 희귀 스폰 알림 | 1.7.3용 Cobblemon Spawn Alerts 적용 |
| 탈것/이동 | Immersive Aircraft, Gliders, Gotta Ride 'Em All 적용 |
| 베리 보관/구조물 | Berry Pouch, Cobblemon Extra Structures 적용. 구조물 신규 청크 생성은 추가 확인 필요 |
| 관장/배지 | CobbleBuilds marker/spawner와 `mingle-gym-party-overrides` 데이터팩 적용. 배지 지급과 반복 플레이 흐름은 추가 인게임 검증 필요 |
| 트레이너 레벨 | CobbleBuilds 관장/체육관 일반 트레이너는 배지 수 기반. RCTMod 자연 스폰 일반 트레이너는 파티 최고 레벨 기준이며 `maxLevelDiff = 5` |
| 데일리 보상 | 161 레거시 라인 bridge 기준. 173 이관은 별도 작업 |
| Hermes | 161 레거시 라인 bridge 기준. 173 이관은 별도 작업 |

## 운영 원칙

1. 개인 서버이므로 공개 접속 편의보다 월드 보존을 우선한다.
2. 173 현재 라인과 161 레거시 라인의 설정, 모드, 문서를 섞지 않는다.
3. 모드 추가는 마지막 선택지로 본다.
4. 서버와 클라이언트의 필수 모드 차이를 만들지 않는다.
5. 월드 파일, 설정 파일, 모드 파일 변경 전에는 되돌릴 방법을 확보한다.
6. 서버 주소나 접속 조건이 바뀌면 문서도 함께 갱신한다.

## 현재 제외 범위

- 공개 서버 런칭
- 불특정 다수 접속 허용
- 서버 홍보 페이지 구성
- 관리자 웹 패널 구축
- 새 경제/상점 모드 추가
- 검증 없는 대규모 모드 변경
- 검증 없는 관장/구조물 대량 변경
- 서버 자동 관리 AI가 월드나 설정을 직접 변경하는 기능

## 관련 문서

- [SERVER_RULES.md](SERVER_RULES.md)
- [OPS_RUNBOOK.md](OPS_RUNBOOK.md)
- [MODS_AND_CLIENT.md](MODS_AND_CLIENT.md)
- [COBBLEMON_173_LINE.md](COBBLEMON_173_LINE.md)
- [COBBLEMON_173_LOCAL_PROFILE.md](COBBLEMON_173_LOCAL_PROFILE.md)
- [COBBLEMON_173_MOD_GAP.md](COBBLEMON_173_MOD_GAP.md)
- [GYM_CONCEPT.md](GYM_CONCEPT.md)
- [HERMES_BRIDGE.md](HERMES_BRIDGE.md)
- [DAILY_REWARD.md](DAILY_REWARD.md)
