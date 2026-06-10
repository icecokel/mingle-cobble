# icecoke-cobblemon Server Docs

마지막 갱신: 2026-06-11

이 폴더는 `icenux-ms7b23`에서 실행 중인 개인용 Cobblemon 서버의 작업 기준 문서다. 서버에서 작업할 때는 먼저 이 파일을 읽고, 필요한 세부 문서로 이동한다.

## 문서 원칙

- 로컬 repo의 `docs/server/`가 원본이다.
- 서버의 `/home/icenux/minecraft/mingle-lounge/docs/`는 161 레거시 라인에 남아 있는 작업 현장 사본이다. 현재 173 라인에는 별도 `docs/` 사본을 두지 않는다.
- 서버 설정, 모드, 클라이언트 조건, 관장 계획이 바뀌면 로컬 원본 문서를 먼저 갱신한다. 원격 문서 사본은 필요한 경우에만 복사한다.
- 이 워크스페이스는 기준 재정의 전까지 문서와 스크립트 중심으로 유지한다. `client-mods/`, `datapacks/`, `resourcepacks/`, `sample/` 산출물은 로컬 Git 보관 대상에서 제외한다.
- 서버 작업을 했으면 `CHANGELOG.md`에 `요청`, `목표`, `작업내용`, `기대작용`, `특이사항`을 기록한다.
- 백업, 검증, 재시작 필요 여부, 클라이언트 영향이 있으면 같은 기록에 함께 남긴다.
- 검증하지 않은 상태를 완료로 적지 않는다.
- 이 문서 세트는 현재 `icecoke-cobblemon` 개인 서버의 173/161 버전 라인 운영 기준이다.
- 현재 플레이 기준은 `icecoke-cobblemon-173`이다.
- 기존 `1.6.1` 서버는 `icecoke-cobblemon-161` 레거시 라인으로 보존한다.
- 173 라인의 서버 경로에는 과거 테스트 인스턴스 이름인 `icecoke-cobblemon-173-test`가 남아 있지만, 표시명과 운영 명칭은 `icecoke-cobblemon-173`이다.

## 문서 목록

| 문서 | 역할 |
| --- | --- |
| [SERVER_CONCEPT.md](SERVER_CONCEPT.md) | 서버 목적, 현재 상태, 운영 방향 |
| [SERVER_RULES.md](SERVER_RULES.md) | 플레이 룰, 난이도, 공개 여부, 사망 보호 |
| [OPS_RUNBOOK.md](OPS_RUNBOOK.md) | SSH, screen, 콘솔 명령, 점검, 백업 원칙 |
| [MODS_AND_CLIENT.md](MODS_AND_CLIENT.md) | 서버/클라이언트 모드 상태와 접속 조건 |
| [COBBLEMON_173_LINE.md](COBBLEMON_173_LINE.md) | Cobblemon 173 라인 상태와 검증 기록 |
| [COBBLEMON_173_LOCAL_PROFILE.md](COBBLEMON_173_LOCAL_PROFILE.md) | 로컬 173 Modrinth 프로필과 접속 조건 |
| [COBBLEMON_173_MOD_GAP.md](COBBLEMON_173_MOD_GAP.md) | 161 레거시와 173 라인 모드 차이 |
| [HERMES_BRIDGE.md](HERMES_BRIDGE.md) | 게임 채팅 질문 응답 브리지 운영 |
| [HERMES_DEATH_LOCATION_PLAN.md](HERMES_DEATH_LOCATION_PLAN.md) | Hermes 사망 위치 기록/답변 기능 계획 |
| [DAILY_REWARD.md](DAILY_REWARD.md) | 접속 이벤트 기준 하루 1회 랜덤 데일리 보상 운영 |
| [DAILY_REWARD_IMPLEMENTATION_PLAN.md](DAILY_REWARD_IMPLEMENTATION_PLAN.md) | 접속 이벤트 기준 랜덤 데일리 보상 구현 계획 |
| [GYM_CONCEPT.md](GYM_CONCEPT.md) | 관장 타입, 바이옴, 동적 난이도 컨셉 |
| [GYM_TEAMS.md](GYM_TEAMS.md) | 관장별 포켓몬 팀 구성 |
| [GYM_IMPLEMENTATION_PLAN.md](GYM_IMPLEMENTATION_PLAN.md) | 서브 에이전트 기반 관장 추가 실행 계획 |
| [GYM_FLOATING_FIX_PLAN.md](GYM_FLOATING_FIX_PLAN.md) | 허공 gym 구조물 재수정 검증 계획 |
| [GYM_PLACEMENT_LOG.md](GYM_PLACEMENT_LOG.md) | 관장/NPC/체육관 실제 배치 좌표와 검증 기록 |
| [CHANGELOG.md](CHANGELOG.md) | 서버 문서와 주요 설정 변경 기록 |

## 현재 서버 요약

| 항목 | 값 |
| --- | --- |
| 현재 플레이 라인 | `icecoke-cobblemon-173` |
| 173 디렉터리 | `/home/icenux/minecraft/icecoke-cobblemon-173-test` |
| 173 Minecraft | `1.21.1` |
| 173 Loader | Fabric server `0.17.3` |
| 173 Cobblemon | `1.7.3` |
| 173 실행 세션 | `screen` 세션 `icecoke-173` |
| 173 포트 | `25566` |
| 161 레거시 라인 | `icecoke-cobblemon-161`, `/home/icenux/minecraft/mingle-lounge`, 포트 `25565` |
| 공개 여부 | 비공개, LAN/허용된 환경 우선 |
| 161 보조 세션 | `mc-daily-reward`, `mc-hermes-bridge` |

## 현재 기능 요약

- 개인용 Cobblemon 장기 플레이 서버
- 일반 적대 몬스터 비활성화, 사망 보호 활성화
- 지도/포켓몬 이름 표시와 희귀 스폰 알림 사용
- 173 라인은 전투, 포획, 지도, JEI, 탈것, Berry Pouch, Extra Structures 부팅/접속 검증을 통과했다.
- 173 라인의 CobbleBuilds 관장/체육관 일반 트레이너는 `mingle-gym-party-overrides` 데이터팩으로 배지 수 기반 레벨 보정을 적용한다.
- 173 라인의 RCTMod 자연 스폰 일반 트레이너는 플레이어 파티 최고 레벨 기준이며, 현재 `maxLevelDiff = 5`로 완화했다.
- 관장/배지/트레이너 밸런스는 적용 후 인게임 장기 검증 대상이다.
- 161 레거시 라인은 기존 8관장 marker/spawner, 데일리 보상, Hermes bridge 기준 상태를 보존한다.

## 작업 시작 체크

1. `OPS_RUNBOOK.md`에서 현재 서버 확인 명령을 본다.
2. 서버 설정을 바꾸기 전 `CHANGELOG.md`에 남길 `요청`, `목표`, `작업내용`, `기대작용`, `특이사항`을 정한다.
3. 모드/클라이언트 조건이 바뀌면 `MODS_AND_CLIENT.md`도 같이 갱신한다.
4. 관장 작업은 173 라인 적용 여부를 먼저 확인하고, `GYM_IMPLEMENTATION_PLAN.md`, `GYM_CONCEPT.md`, `GYM_TEAMS.md`를 기준으로 1명씩 진행한다.
