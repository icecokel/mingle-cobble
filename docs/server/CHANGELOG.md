# Server Changelog

이 문서는 `icecoke-cobblemon` 서버의 주요 설정과 문서 변경을 기록한다.

## 기록 형식

서버 작업을 했으면 날짜 아래에 아래 항목을 기본으로 남긴다.

```markdown
- 요청:
- 목표:
- 작업내용:
- 기대작용:
- 특이사항:
```

필요하면 `백업`, `검증`, `재시작`, `클라이언트 영향`, `확인 필요`를 같은 기록에 추가한다. 작업 중 계획과 실제 결과가 달라졌으면 최종 기록은 실제 수행 내용 기준으로 고친다.

## 2026-06-11

- 요청: 워크스페이스를 문서와 스크립트 중심으로 정리하고, 나중에 기준을 다시 잡을 수 있게 비운다.
  목표: 로컬 저장소에서 모드 jar, 데이터팩, 리소스팩, 샘플 zip, 임시 산출물을 제거해 운영 문서와 보조 스크립트 중심으로 유지한다.
  작업내용: `client-mods/`, `datapacks/`, `resourcepacks/`, `sample/`, `backups/`, `work/`, `.tmp/`, `.playwright-mcp/`, `.DS_Store`, 루트의 0바이트 오생성 파일을 제거했다. `.gitignore`, `README.md`, `AGENTS.md`, `docs/server/README.md`를 문서/스크립트 중심 보관 기준에 맞춰 갱신했다. 삭제된 데이터팩/리소스팩에 의존하던 로컬 테스트 디렉터리는 기준 재정의 전까지 제거한다.
  기대작용: Git 저장소가 서버 운영 지식과 자동화 스크립트 중심으로 가벼워지고, 산출물 관리 정책을 후속 작업에서 새로 정할 수 있다.
  특이사항: 샘플 원본은 서버 `/home/icenux/minecraft/source-archives/포켓몬 100일 생존 1.21.zip`에 보관했고, 173 정기 백업은 서버 cron으로 유지한다. 서버 재시작과 클라이언트 영향은 없다.
  검증: 워크스페이스에는 `.git` 제외 기준으로 `.md`, `.py`, `.sh`, `.command`, Git 설정 파일만 남는 것을 확인했다.

- 요청: 프로젝트 토대가 되는 샘플 zip을 워크스페이스 대신 서버에 별도 보관.
  목표: 로컬 워크스페이스를 문서/스크립트 중심으로 가볍게 유지하면서, 원본 샘플 패키지는 서버에 보존한다.
  작업내용: `sample/포켓몬 100일 생존 1.21.zip`을 `scp`로 `/home/icenux/minecraft/source-archives/포켓몬 100일 생존 1.21.zip`에 업로드했다.
  기대작용: 로컬에서 샘플 zip을 제거해도 서버에 기준 원본을 보관할 수 있고, 173/161 운영 디렉터리와는 분리된다.
  특이사항: 서버 실행 디렉터리에는 넣지 않았고, 별도 보관 경로 `source-archives`를 사용했다. 서버 재시작과 클라이언트 영향은 없다.
  검증: 로컬과 서버 sha256이 `3fd3d266f5d30f0cbae7a539bcabad9424c3c5c05ebe071236d6eca5acd94931`로 일치함을 확인했다.

- 요청: 정기 백업을 173 라인만 진행하도록 변경.
  목표: 현재 플레이 기준인 `icecoke-cobblemon-173`의 월드만 매일 19:00 KST에 자동 백업하고, 161 레거시 라인의 자동 백업은 중단한다.
  작업내용: `tools/mc_world_backup.sh` 기본값을 `/home/icenux/minecraft/icecoke-cobblemon-173-test`, `icecoke-173` screen, 173 전용 lock 파일로 변경했다. 원격 173 서버의 `tools/mc_world_backup.sh`에 배포했고, crontab을 173 백업 한 줄만 남도록 교체했다. 실행 중 월드 tar 실패를 막기 위해 백업 흐름을 `save-off -> save-all flush -> tar -> save-on -> sha256 검증`으로 보강했다. `OPS_RUNBOOK.md`의 정기 백업 절차도 173 기준으로 갱신했다.
  기대작용: 현재 실제 플레이 중인 173 월드가 매일 자동 백업되고, 161 레거시 백업으로 저장 공간과 운영 기준이 분산되는 문제를 줄인다.
  특이사항: 서버 재시작은 하지 않았다. 백업 중에는 짧게 `save-off` 상태가 되지만 백업 완료 또는 실패 시 `save-on`을 다시 보내도록 처리했다.
  백업: 수동 검증으로 `backups/world-auto-backup-20260611-073449.tar.gz`와 `.sha256`을 생성했다.
  검증: 수동 실행 결과 `backups/world-auto-backup-20260611-073449.tar.gz: OK`를 확인했고, crontab이 173 경로 한 줄만 남은 것을 확인했다.
  클라이언트 영향: 없음.

## 2026-06-10

- 요청: 서버 작업마다 `요청`, `목표`, `작업내용`, `기대작용`, `특이사항` 등을 기록하는 프로젝트 룰 추가.
  목표: 이후 서버 변경 이력을 단순 나열이 아니라 의도와 기대 효과까지 추적 가능한 형식으로 남긴다.
  작업내용: `AGENTS.md`, `docs/server/README.md`, `OPS_RUNBOOK.md`, `CHANGELOG.md`에 서버 작업 기록 규칙과 템플릿을 추가했다.
  기대작용: 설정 변경, 모드 추가, 재시작, 문서 변경의 맥락과 검증 상태를 나중에 빠르게 파악할 수 있다.
  특이사항: 기존 과거 changelog 전체를 새 형식으로 재작성하지는 않고, 신규 서버 작업부터 적용한다.
- 173 라인에서 관장/일반 트레이너 레벨이 배지 수 기준보다 높게 나오는 원인을 확인했다. 173의 `cobblebuilds-leaders-0.1.1-hf.1.jar`는 Molang 파티 경로가 `data/cobblebuilds/molang/party/gym_leader/...`인데, 기존 `mingle-gym-party-overrides.zip`은 `data/cobblebuilds/molang/parties/...`에 파일을 넣어 실제 원본 파티를 덮지 못했다.
- `mingle-gym-party-overrides` 데이터팩 구조를 173 경로에 맞게 수정하고, 8개 관장 파티 override를 `gym_leader/<type>/party.gym_leader.<gym>.<leader>.molang` 아래로 옮겼다.
- 일반 트레이너도 원본 CobbleBuilds 파티가 플레이어 최고 레벨이나 높은 하한값을 직접 사용하므로, 현재 8개 체육관 타입의 `gym_trainer` 파티 override를 추가했다. 일반 트레이너는 `gym_badge_count`만 기준으로 `badge_cap - 8` 근처에서 시작하며, trainer class별로 소폭만 상승한다.
- `tests/test_gym_party_overrides.py`에 173 Molang 경로와 packaged zip 내부 경로 검증을 추가했다.
- RCTMod 자연 스폰 일반 트레이너는 CobbleBuilds 배지 수가 아니라 플레이어 파티 최고 레벨 기준으로 후보를 고르는 것을 확인했다. `config/rctmod-server.toml`의 `maxLevelDiff`를 `25`에서 `5`로 낮춰 과한 고레벨 자연 트레이너 스폰을 완화했다.
- 변경 전 백업은 `backups/rctmod-server-before-max-level-diff-5-20260610-230730.toml`이다. 173 라인 재시작 후 로그 기준 `Done (1.750s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`, 로컬 TCP 접속 성공을 확인했다.
- 현재 RCTMod 주요 설정은 `initialLevelCap = 100`, `maxLevelDiff = 5`, `forceBattleMaxLevelDiff = 16`, `relativeLevelCap = 0`, `allowOverLeveling = false`다. 파티 평균 레벨 기준으로 전환하는 설정은 확인되지 않아 필요 시 별도 모드/믹스인/포크 설계가 필요하다.
- 실제 173 서버 상태에 맞춰 `README.md`, `AGENTS.md`, `docs/server/README.md`, `SERVER_CONCEPT.md`, `SERVER_RULES.md`, `OPS_RUNBOOK.md`, `MODS_AND_CLIENT.md`, `COBBLEMON_173_LINE.md`, `COBBLEMON_173_MOD_GAP.md`, `CHANGELOG.md`를 갱신했다.

## 2026-06-08

- 서버 라인 명칭을 `icecoke-cobblemon-173` 현재 플레이 라인과 `icecoke-cobblemon-161` 레거시 보존 라인으로 정리했다. 173 라인은 `192.168.219.110:25566`, 161 라인은 `192.168.219.110:25565`를 사용한다.
- 173 서버의 실제 디렉터리 `/home/icenux/minecraft/icecoke-cobblemon-173-test`는 안정성을 위해 이동하지 않고, `server.properties` MOTD와 스크립트 기본 screen 명칭만 `icecoke-cobblemon-173`, `icecoke-173`으로 정리했다.
- 161 서버의 `server.properties` MOTD를 `icecoke-cobblemon-161`로 변경했다. screen 명칭은 기존 `mingle-sample`을 유지한다.
- 변경 전/후 보존을 위해 161 인스턴스 백업 `instance-before-version-line-promotion-161-20260608-083756.tar.gz`와 173 인스턴스 백업 `instance-before-version-line-promotion-173-20260608-083756.tar.gz`를 만들고 sha256 검증 `OK`를 확인했다.
- 이 Mac의 Modrinth App DB를 백업한 뒤 로컬 173 프로필을 `icecoke-cobblemon-173-test`에서 `icecoke-cobblemon-173`으로 rename했다. 기존 1.6.1 프로필 `icecoke-cobblemon`은 161 레거시용으로 보존한다.
- 문서 파일명을 이전 173 라인 문서에서 `COBBLEMON_173_LINE.md`, 이전 173 로컬 계획 문서에서 `COBBLEMON_173_LOCAL_PROFILE.md`로 정리했다.
- `README.md`, `AGENTS.md`, `docs/server/README.md`, `SERVER_CONCEPT.md`, `MODS_AND_CLIENT.md`, `OPS_RUNBOOK.md`, `COBBLEMON_173_LINE.md`, `COBBLEMON_173_LOCAL_PROFILE.md`, `COBBLEMON_173_MOD_GAP.md`를 173/161 라인 기준으로 갱신했다.
- `DAILY_REWARD.md`와 `HERMES_BRIDGE.md`는 현재 161 레거시 라인 기준 기능이며, 173 라인 이관은 별도 작업이라고 명시했다.
- 173/161 서버를 재시작해 새 표시명을 반영했다. 검증 결과 screen은 `icecoke-173`, `mingle-sample`, 포트는 `25566`, `25565`, 로그는 각각 `Done`, 콘솔 `list`는 0명 응답, 로컬 TCP 접속은 두 포트 모두 성공이다.

## 2026-06-07

- 이 Mac에 1.7.3 전용 Modrinth 173 프로필 `icecoke-cobblemon-173`를 만들고, 173 라인 `192.168.219.110:25566` 서버 항목을 추가했다. 기존 운영 프로필 `icecoke-cobblemon`은 수정하지 않았다.
- 공식 `Cobblemon Official Modpack [Fabric]` 복사본 20개 모드만으로는 173 라인 접속 직후 `cobblefurnies`, `legendarymonuments`, `geckolib`, `trinkets` registry mismatch로 disconnect됨을 확인했다.
- 173 프로필에 173 라인과 같은 월드젠/블록 의존 모드 13개를 추가해 총 33개 모드로 맞췄고, 서버 로그 기준 `Icecokel joined the game`까지 확인했다. 테스트 종료 후 클라이언트를 닫았으며 서버 접속자는 0명이다.
- 1.7.3 테스트 클라이언트로 추가 인게임 검증을 진행했다. `Icecokel`이 5분 이상 접속 유지됐고, 월드 렌더링, Cobblemon 파티 UI, PC UI, 주변 포켓몬 모델, 미니맵 표시를 확인했다. 전투/포획/관장/배지/스폰 알림은 실제 인게임 조작이 더 필요해 확인 필요로 남겼다.
- 사용자가 173 라인에서 전투 1회 성공과 포획 성공을 확인했다. 남은 핵심 검증은 관장/NPC/배지, 스폰 알림, Xaero World Map 전체 화면, 가방/배지 보관/보상 호환성이다.
- 161 레거시 `mods/` 90개와 173 라인 `mods/` 33개를 비교해 `COBBLEMON_173_MOD_GAP.md`를 추가했다. 1.7.3용 대체 전환 8개와 미전환 67개를 분리하고, JEI, 관장/배지, 탈것, 가방, 월드 잔여 참조, 성능 모드 순으로 검토 후보를 정리했다.
- 미전환 67개 모드의 1.7.3/1.21.1 Fabric 대응 존재성을 조사해 `COBBLEMON_173_MOD_GAP.md`에 추가했다. CobbleCuisine, Cobblemon Repel, Cobbreeding, SimpleTMs, Cobblemon Armors, Drop Loot Tables, More Cobblemon Move Anims는 1.7.x 계열 후보가 확인됐고, JEI/Immersive Aircraft/Gliders/Farmer's Delight/성능 모드 대부분은 1.21.1 Fabric 후보가 확인됐다. Shearems, Unimplemented Items, Whiteout 등은 1.6 계열까지만 확인되어 제외 또는 후순위로 남겼다.
- 173 라인과 로컬 173 프로필에 핵심 기능 모드 17개와 의존성 조정 2개를 적용해 173 라인 모드 수를 50개로 늘렸다. 적용 항목은 CobbleCuisine, Cobblemon Repel, Cobbreeding, SimpleTMs, Cobblemon Armors, DropLootTables, Extra Move Animations, CobbleBuilds Leaders, BadgeBox, RCTApi/RCTMod, Farmer's Delight 3.2.8, CobbleCuisine Delight, Immersive Aircraft, Gliders, ForgeConfigAPIPort, Common Network이며, `GeckoLib 4.8.4`, `Tim Core 1.32.0`으로 의존성을 교체했다. 편의 UI/검색/줌/단순 성능 모드는 보류했다. 현재 실행 중인 25566 서버는 재시작 전이라 아직 새 모드를 로드하지 않았고, 별도 임시 포트 25567 부팅 검증에서 `Done (10.514s)!`와 RCT trainer 1559개 등록을 확인했다.
- 관장/NPC/탈것 추가 테스트 전 현재 1.7.3 테스트 인스턴스를 백업했다. 서버 백업은 `backups/instance-before-gym-ride-trainer-20260607-182450.tar.gz`, 로컬 173 프로필 모드 백업은 `backups/local-173-mods/icecoke-173-local-mods-before-gym-ride-trainer-20260607-182449.tar.gz`이다.
- 관장/NPC 보조용 `Easy NPC 6.2.0 bundle`과 Cobblemon riding 확장용 `Gotta Ride 'Em All 1.0`을 173 라인, 로컬 173 프로필, `client-mods/required`에 추가해 173 라인 모드 수를 52개로 늘렸다. 최신 `Easy NPC 6.17.0`은 Fabric Loader `0.18.3+`를 요구해 제외했고, 기존 161 레거시의 `Cobblemon: Ride On! / cobbleride 0.3.3`은 `Cobblemon >=1.7`과 명시 충돌해 제거했다. 별도 임시 포트 25567 부팅 검증에서 `Done (9.118s)!`와 RCT trainer 1559개 등록을 확인했다.
- 173 라인을 재시작해 52개 모드셋을 실제 25566 서버에 로드했다. 서버 로그 기준 `Done (1.602s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`, 콘솔 `list` 응답을 확인했다. 로컬 173 프로필도 같은 52개 모드셋이다.
- 173 라인에서 RCTMod 기본 레벨캡 `initialLevelCap = 15`가 다시 적용된 것을 확인했다. 기존 운영 원칙과 맞춰 `config/rctmod-server.toml`을 `initialLevelCap = 100`으로 변경했다. 변경 전 백업은 `backups/rctmod-server-before-levelcap-173-20260607-193024.toml`이다.
- 173 라인을 재시작해 RCTMod `initialLevelCap = 100`을 실제 서버에 반영했다. 서버 로그 기준 `Done (1.590s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`, 콘솔 `list` 응답을 확인했다.
- 161 레거시의 남은 모드 중 가벼운 항목을 173 라인에 추가 검증하기 전 현재 테스트 인스턴스를 백업했다. 백업은 `backups/instance-before-light-main-mods-test-20260607-194954.tar.gz`이고, 해시 검증 결과 `OK`다. `COBBLEMON_173_MOD_GAP.md`에 1차 후보 `fightorflight`, `JEI`, `Clumps`, `FerriteCore`, `Krypton`, `EntityCulling`, `Just Zoom`, `Show Held Items`와 보류/제외 기준을 기록했다.
- 1차 가벼운 후보를 적용했다. 173 라인에는 `Fight or Flight 0.10.7`, `Clumps`, `FerriteCore`, `Krypton`을 추가해 서버 모드 수가 56개가 됐고, 로컬 173 프로필에는 `Fight or Flight`, `JEI`, `EntityCulling`, `Just Zoom`, `Konkrete`를 추가했다. `Show Held Items 0.2.3`은 `Cobblemon 1.6.1` 고정 의존성이라 제외했다. 25566 서버 재시작 후 `Done (1.823s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`를 확인했고, 로컬 클라이언트 접속 로그와 서버 `Icecokel joined/lost connection` 로그까지 확인했다.
- `Berry Pouch 0.5.4-beta`와 `Cobblemon Extra Structures 1.3.0`을 173 라인과 로컬 173 프로필에 추가해 서버 모드 수가 58개가 됐다. 적용 전 서버 백업 `backups/instance-before-berry-structures-20260607-210909.tar.gz`와 로컬 모드 백업 `backups/local-173-mods/icecoke-173-local-mods-before-berry-structures-20260607-210943.tar.gz`를 만들고 해시 검증했다. 25566 서버 재시작 후 `Done (1.665s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`를 확인했고, 로컬 클라이언트 접속도 확인했다. 단 `Cobblemon Extra Structures`의 `sprout_tower` advancement 경고와 신규 청크 구조물 생성 검증은 남아 있다.

## 2026-06-05

- `Cobblemon 1.7.3` 173 라인 접속을 이 Mac에서 검증하기 위한 `COBBLEMON_173_LOCAL_PROFILE.md`를 추가했다. 기존 1.6.1 로컬 프로필을 보존하고, 별도 `icecoke-cobblemon-173` 프로필로 `192.168.219.110:25566` 접속, 클라이언트 crash, 서버 모드 불일치, 인게임 기능을 단계적으로 확인하는 절차를 정의했다.
- 클라이언트 UI에 남는 영어 문구를 줄이기 위해 클라이언트 전용 `icecoke-ko-ui-overlay.zip` 리소스팩을 생성했다. `Cobblemon 1.6.1` 한국어에서 빠졌지만 `Cobblemon 1.7.3` 한국어에 있는 1255개 키를 재사용하고, `Cobblemon Spawn Alerts` 45개 키, `Xaero Minimap` 566개 키, `Xaero World Map` 주요 75개 키를 보강했다. 로컬 `icecoke-cobblemon` 프로필에 설치하고 `options.txt`에서 `CCC_MAL_1.5.4.zip`, `cobblemon-ko-tooltip-overlay.zip`, `icecoke-ko-ui-overlay.zip` 순서로 활성화했다.
- 서버 사용자 crontab에 매일 19:00 KST 정기 월드 백업을 추가했다. `tools/mc_world_backup.sh`가 `save-all flush` 후 `backups/world-auto-backup-YYYYMMDD-HHMMSS.tar.gz`와 `.sha256`을 생성하며, 로그는 `logs/mc-world-backup-cron.log`에 남긴다.
- 운영 서버를 유지한 채 `/home/icenux/minecraft/icecoke-cobblemon-173-test`에 `Cobblemon 1.7.3` 173 라인을 만들었다. 포트는 `25566`, screen은 `icecoke-173`이며, 운영 월드 백업 복사본으로 기동한다. Fabric Loader `0.17.3`과 1.7.3 공식 프로필 기반 모드에 운영 월드 로딩용 월드젠/블록 의존 모드를 추가했고, `Done`, 포트 리슨, 콘솔 `list`, 로컬 TCP 접속을 확인했다.

## 2026-06-04

- `Cobblemon 1.6.1` 한국어 아이템 tooltip 부족을 보완하기 위해 클라이언트 전용 `cobblemon-ko-tooltip-overlay.zip` 리소스팩을 생성했다. `Cobblemon 1.7.3` 한국어 번역에서 1.6.1이 실제 사용하는 `item.cobblemon.*tooltip*` 키 405개를 추출했고, 빠진 설명 288개와 짧은 설명 84개를 보강했다. 로컬 `icecoke-cobblemon` 프로필에 설치하고 `options.txt`에서 활성화했다.
- `steel_gym`은 CobbleBuilds 건물 구조물이 없는 수동 거점이라 기존 배치에는 관장 스포너만 있었음을 확인했다. 신호기 철 블록 발판 위에 `gym_trainer.steel_gym.youngster`, `gym_trainer.steel_gym.camper`, `gym_trainer.steel_gym.acetrainer` 스포너를 추가했다. 변경 전 백업은 `backups/world-before-steel-trainers-20260604-070355.tar.gz`이다.
- `mingle-gym-party-overrides` 관장 파티 분기 기준을 CobbleBuilds `rank`에서 `q.player.data.gym_badge_count`로 변경했다. 배지 기반 레벨캡은 `0개=15`, `1개=25`, `2개=35`, `3개=45`, `4개=55`, `5개=65`, `6개=75`, `7개=85`, `8개=100`이며, 관장 파티는 이 캡을 넘지 않는 범위에서 플레이어 최고 레벨을 참고해 보정한다.
- 강철 관장 클리어 후 재도전이 막힌 것은 CobbleBuilds `steel_gym` 배지가 플레이어 데이터에 기록된 정상 1회 클리어 동작으로 확인했다.
- 파이리 Lv.15 경험치 정지는 RCTMod 기본 `initialLevelCap=15`와 CobbleBuilds 관장 배지 진행이 서로 연동되지 않아 발생한 것으로 확인했다. 서버 설정 `config/rctmod-server.toml`의 `initialLevelCap`을 `100`으로 변경했고, 적용에는 서버 재시작이 필요하다. 변경 전 백업은 `backups/rctmod-server-before-levelcap-fix-20260604-001519.toml`이다.
- Hermes bridge가 질문마다 `mods/*.jar`의 `fabric.mod.json`, `quilt.mod.json`, `META-INF/mods.toml` 메타데이터를 요약해 답변 프롬프트에 포함하도록 변경했다.
- Hermes 답변 기준을 서버 문서 최우선으로 유지하되, 문서가 부족한 Minecraft/Fabric/Cobblemon/설치 모드 질문에는 일반 지식을 사용할 수 있게 했다. 버전 차이가 있을 수 있으면 확인 필요로 답한다.
- Hermes가 루트 플레이어 가이드 `cobblemon-newbie-guide.md`, `cobblemon-mod-usage-guide.md`, `cobblemon-client-setup-guide.md`를 관련 질문에서 참조하도록 프롬프트에 추가했다.

## 2026-06-03

- `sample/포켓몬 100일 생존 1.21.zip` 기반 개인용 서버 컨셉 확정.
- 서버 이름/MOTD를 `icecoke-cobblemon`으로 정리.
- 일반 Minecraft 적대 몬스터 비활성화: `spawn-monsters=false`.
- 사망 보호 활성화: `gamerule keepInventory true`.
- 보이스챗, 리플레이, 쉐이더, 선택 연출 관련 클라이언트 모드 제거.
- 서버의 비활성 `.jar.disabled` 파일 정리.
- 관장 컨셉 문서 작성.
- 관장별 초급/표준/상급 포켓몬 팀 문서 작성.
- 서버 작업용 문서 세트 `docs/server/` 생성.
- 바위 관장 테스트용 `rock_gym` marker와 `gym_leader.rock_gym.brock` NPC 스포너 marker를 `2 68 -359`에 배치.
- 관장 실제 배치 기록 문서 `GYM_PLACEMENT_LOG.md` 추가.
- 서버 재기동 후 바위 관장 marker/spawner 저장 상태 확인. 실제 `cobblemon:npc` 생성은 플레이어 근접 인게임 테스트 필요로 남김.
- CobbleBuilds 기본 짐 건물 구조물 확인: `rock_gym`, `grass_gym`, `water_gym`, `electric_gym`, `fire_gym`, `poison_gym` 6개는 건물 있음. `ice_gym`, `steel_gym`은 관장 NPC는 있으나 건물 구조물은 없음.
- 강철 관장 마을 컨셉에 위치 안내용 작은 신호기 추가. 초기에는 상시 Beacon 버프 제공이 아니라 시각 표식으로만 다룸.
- 서브 에이전트 기반 관장 추가 실행 계획 `GYM_IMPLEMENTATION_PLAN.md` 추가.
- 서브 에이전트 기반 관장 추가 작업을 위한 후보 조사와 배치 명령 템플릿 준비.
- 월드 region/POI/heightmap 기반 8관장 1차 후보 좌표와 CobbleBuilds 배치 명령 조사 결과를 `GYM_PLACEMENT_LOG.md`에 통합.
- 관장 배치 문서 리뷰 결과 반영: 현재 샘플 서버 `Cobblemon 1.6.1` 기준 가드 추가, marker-only 상태 정정, 구조물 롤백 고위험 표기, `stop.sh` 경고 추가.
- Minecraft 채팅 `@hermes` 질문을 Hermes/Codex로 답변하는 브리지 스크립트와 운영 문서 추가.
- `mc-hermes-bridge` screen 세션으로 Hermes 브리지 기동. 인게임 `@hermes` end-to-end 테스트는 확인 필요로 남김.
- 8관장 월드 배치 진행: 6개 CobbleBuilds 기본 gym 건물 배치, 8개 gym marker와 8개 gym leader spawner marker 배치, 강철 관장 마을 신호기 배치. 인게임 NPC 생성/전투/보상 검증은 확인 필요.
- 서버 실제 날짜와 플레이어 접속 이벤트 기준 하루 1회 랜덤 데일리 보상 구현 계획 `DAILY_REWARD_IMPLEMENTATION_PLAN.md` 추가.
- 플레이어 접속 이벤트 기준 데일리 보상 bridge 스크립트와 운영 문서 `DAILY_REWARD.md` 추가. 새 모드/클라이언트 변경 없이 `mc-daily-reward` screen 세션으로 운영.
- 서버 재시작 뒤 Hermes bridge가 이전 삭제 로그를 따라가던 문제를 확인하고, `latest.log` 교체/truncate 감지 후 재오픈하도록 `mc_hermes_bridge.py`를 갱신. `mc-hermes-bridge` 세션 재기동 완료.
- Hermes bridge의 `@hermes` prefix 요구를 제거하고 개인 서버 기준 모든 플레이어 채팅을 질문으로 처리하도록 변경. `메모:`, `메모해줘`, `기억해줘` 요청은 `data/hermes-memos.jsonl`에 저장하고 최근 메모를 답변 컨텍스트에 포함하도록 구현.
- Hermes가 플레이어 사망 위치를 관리자형 답변으로 제공하기 위한 계획 문서 `HERMES_DEATH_LOCATION_PLAN.md` 추가. 현재는 문서화만 완료했고, 사망 좌표 기록 기능은 아직 구현 전이다.
- 드롭 아이템이 물리 오브젝트처럼 눕고 굴러가는 `ItemPhysic_FABRIC_v1.8.7_mc1.21.1.jar`를 성능/안정성 우선 기준으로 비활성화. 서버는 `disabled-mods/`, 로컬 클라이언트는 `disabled-client-mods/`에 jar를 보관한다.
- 로컬 Modrinth 클라이언트 프로필에 선택 지도 모드 `xaerominimap-fabric-1.21.1-25.3.12.jar`, `xaeroworldmap-fabric-1.21.1-1.40.16.jar` 추가. 서버 모드는 변경하지 않는다.
- Xaero 미니맵 위치를 우측 중앙 기준으로 변경하고, `cobblemon:pokemon` radar 카테고리에 이름 표시를 활성화.
- 현재 샘플 서버의 `Cobblemon 1.6.1`에 맞춰 `cobblemon_spawn_alerts-fabric-1.6.1.jar`를 서버와 로컬 클라이언트에 설치. 이로치/전설/환상/울트라비스트/패러독스 알림을 켜고, 미도감/미포획 전체 알림은 끔. 서버 재시작 후 로드 확인 완료.
- 공중에 떠 있는 gym 구조물 보정을 위해 `backups/world-before-gym-fix-20260603-210538.tar.gz` 백업을 만들고 해시 검증 후, 6개 CobbleBuilds gym 건물을 제거/재배치. 각 구조물 하단에 `stone` 받침을 추가했고 `electric_gym`, `fire_gym`, `poison_gym`은 지형 기준 Y 좌표를 조정했다. 콘솔 기준 하단 블록, marker/spawner, 저장, forceload 해제 확인 완료.
- 프로젝트 개요를 `icecoke-cobblemon` 개인 서버 운영 워크스페이스 기준으로 정리. 루트 `README.md`를 추가하고, `AGENTS.md`, `SERVER_CONCEPT.md`, `SERVER_RULES.md`, `MODS_AND_CLIENT.md`, `docs/server/README.md`를 현재 운영 상태 기준으로 갱신. 이전 Mingle Lounge `Cobblemon 1.7.3` 루트 문서는 레거시 참고용 경고를 추가했다.
- 1차 gym 보정의 검증 기준 오류를 확인하고 `GYM_FLOATING_FIX_PLAN.md`를 추가. `backups/world-before-gym-groundfix-20260603-212831.tar.gz` 백업 후 6개 CobbleBuilds gym 건물을 자연 지형 heightmap 기준으로 재배치했다. 기존 허공 바위 gym 위치 `-55 174~175 -558` 비움, 새 6개 gym 하단 sample solid, marker/spawner, 저장, forceload 해제 확인 완료.
- `backups/world-before-gym-full-reset-20260603-220037.tar.gz` 백업 후 기존 gym 구조물/marker/spawner/beacon을 제거하고, `33 x 39` 구조물 footprint의 네 모서리와 중앙 기준 아래 10칸 공기칸 2칸 이하 조건으로 gym 재배치 좌표를 다시 산정. 확정 좌표와 검증 기준을 `GYM_PLACEMENT_LOG.md`에 먼저 기록했다.
- 문서 기준 좌표로 6개 CobbleBuilds gym 구조물, 8개 gym marker, 8개 gym leader spawner marker, 강철 관장 beacon 표식을 재생성했다. 저장된 region 파일 재검증 결과 6개 구조물의 네 모서리/중앙 아래 10칸 공기칸은 모두 2칸 이하이며, marker/spawner selector 조회와 `forceload query` 해제 확인 완료. 최종 백업 `backups/world-after-gym-strict-reset-20260603-222230.tar.gz` 생성 및 해시 검증 완료.
- CobbleBuilds 원본 `gym_leader.steel_gym.jasmine` 파티가 불꽃 타입 팀으로 매핑된 것을 확인하고, `mingle-gym-party-overrides` 데이터팩으로 `party.gym_leader.steel_gym.jasmine.molang`만 강철 타입 라인업으로 override하도록 추가했다.
- CobbleBuilds 원본 관장 파티 전체를 재검토하고 `mingle-gym-party-overrides` 데이터팩을 8개 관장 전체 override로 확장했다. `ice_gym.pryce`의 풀 타입 오매핑과 `steel_gym.jasmine`의 불꽃 타입 오매핑을 교정하고, Grass Shaymin, Electric Regieleki, Fire Heatran, Poison Naganadel 같은 전설/환상/울트라비스트급 구성을 초기 관장전에서 제외했다.
