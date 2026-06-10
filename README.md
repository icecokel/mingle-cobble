# icecoke-cobblemon 운영 워크스페이스

마지막 갱신: 2026-06-11

이 저장소는 `icenux-ms7b23`에서 실행 중인 개인용 Minecraft/Cobblemon 서버 `icecoke-cobblemon`의 운영 문서와 서버 보조 스크립트를 관리한다. 모드 jar, 데이터팩 zip, 리소스팩 zip, 샘플 zip 같은 산출물은 기준을 다시 잡기 전까지 이 워크스페이스에 보관하지 않는다.

## 현재 프로젝트 정의

`icecoke-cobblemon`은 공개 서버나 커뮤니티 서버가 아니라 개인용 Cobblemon 장기 플레이 서버다. 현재 목표는 접속 안정성, 월드 보존, 백업 가능성, 작은 단위의 기능 확장이다.

서버는 버전 라인으로 구분한다. 현재 플레이 기준은 `icecoke-cobblemon-173`이고, 기존 `1.6.1` 서버는 `icecoke-cobblemon-161` 레거시 라인으로 보존한다.

| 항목 | 현재 기준 |
| --- | --- |
| 서버 | `icenux-ms7b23` |
| 현재 운영 라인 | `icecoke-cobblemon-173` |
| 173 서버 디렉터리 | `/home/icenux/minecraft/icecoke-cobblemon-173-test` |
| 173 서버 이름/MOTD | `icecoke-cobblemon-173` |
| 173 접속 | `192.168.219.110:25566` |
| Minecraft | `1.21.1` |
| 173 Loader | Fabric server `0.17.3` |
| 173 Cobblemon | `1.7.3` |
| 161 레거시 | `/home/icenux/minecraft/mingle-lounge`, `192.168.219.110:25565`, `icecoke-cobblemon-161` |
| 공개 여부 | 비공개, LAN/허용된 환경 우선 |
| 173 실행 세션 | `screen` 세션 `icecoke-173` |
| 로컬 클라이언트 | Modrinth App 프로필 `icecoke-cobblemon-173` |

## 현재 운영 컨셉

- Cobblemon 중심 개인 플레이 월드
- 일반 Minecraft 적대 몬스터 비활성화
- 사망 시 인벤토리, 가방, 경험치 보호
- 방송, 녹화, 보이스챗, 쉐이더, 아이템 물리 연출 제거
- Xaero 지도와 포켓몬 이름 표시를 로컬 편의 기능으로 사용
- 희귀 포켓몬 스폰 알림 사용
- 8관장 탐험 콘텐츠를 문서와 배치 로그 기준으로 관리
- CobbleBuilds 관장/체육관 일반 트레이너는 배지 수 기반 데이터팩 override로 관리
- RCTMod 자연 스폰 일반 트레이너는 플레이어 파티 최고 레벨 기준이며, 현재 허용 레벨 차이는 `maxLevelDiff = 5`
- 데일리 보상과 Hermes bridge는 아직 161 레거시 라인 기준으로 남아 있으며, 173 라인 이관은 별도 작업으로 본다.

## 워크스페이스 보관 기준

현재 로컬 워크스페이스는 문서와 스크립트 중심으로 유지한다.

| 구분 | 현재 기준 |
| --- | --- |
| 유지 | `docs/`, 루트 문서, `tools/`, 운영 스크립트 |
| 제외 | `client-mods/`, `datapacks/`, `resourcepacks/`, `sample/`, 백업/임시 작업물 |
| 샘플 원본 | `/home/icenux/minecraft/source-archives/포켓몬 100일 생존 1.21.zip` |
| 정기 백업 | 173 서버 `/home/icenux/minecraft/icecoke-cobblemon-173-test/backups/` |

클라이언트 모드, 데이터팩, 리소스팩을 다시 Git에서 관리할지는 후속 기준 재정의 때 결정한다.

## 문서 기준

현재 운영 기준은 `docs/server/` 아래 문서다.

| 문서 | 역할 |
| --- | --- |
| [docs/server/README.md](docs/server/README.md) | 서버 문서 진입점 |
| [docs/server/SERVER_CONCEPT.md](docs/server/SERVER_CONCEPT.md) | 서버 목적과 현재 상태 |
| [docs/server/SERVER_RULES.md](docs/server/SERVER_RULES.md) | 플레이/운영 룰 |
| [docs/server/OPS_RUNBOOK.md](docs/server/OPS_RUNBOOK.md) | SSH, screen, 백업, 콘솔 작업 |
| [docs/server/MODS_AND_CLIENT.md](docs/server/MODS_AND_CLIENT.md) | 모드와 클라이언트 접속 조건 |
| [docs/server/COBBLEMON_173_LINE.md](docs/server/COBBLEMON_173_LINE.md) | 173 라인 상태와 검증 기록 |
| [docs/server/COBBLEMON_173_LOCAL_PROFILE.md](docs/server/COBBLEMON_173_LOCAL_PROFILE.md) | 로컬 173 프로필 |
| [docs/server/GYM_PLACEMENT_LOG.md](docs/server/GYM_PLACEMENT_LOG.md) | 관장/체육관 실제 배치 기록 |
| [docs/server/HERMES_BRIDGE.md](docs/server/HERMES_BRIDGE.md) | Hermes bridge 운영 |
| [docs/server/DAILY_REWARD.md](docs/server/DAILY_REWARD.md) | 데일리 보상 운영 |

루트의 기존 `cobblemon-current-settings.md`, `cobblemon-server-build-guide.md`, `server-operation-constraints.md`는 레거시 참고 문서다. 현재 서버 작업 기준은 `docs/server/` 아래 문서다.

## 작업 원칙

1. 서버 파일이나 월드를 변경하기 전 백업 가능성을 먼저 확인한다.
2. 모드 추가는 마지막 선택지로 두고, 기존 설정, gamerule, 데이터팩, bridge 스크립트로 해결할 수 있는지 먼저 본다.
3. 서버와 클라이언트 접속 조건이 바뀌면 문서를 먼저 갱신하고, 산출물 Git 보관 여부는 별도 기준을 세운 뒤 결정한다.
4. 로컬 `docs/server/`를 원본으로 수정한다. 서버 `/home/icenux/minecraft/mingle-lounge/docs/` 사본은 161 레거시 작업용이므로, 별도 필요가 있을 때만 동기화한다.
5. 콘솔/서버 변경은 검증 로그를 남긴 뒤 완료로 말한다.
