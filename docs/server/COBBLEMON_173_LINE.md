# Cobblemon 173 Line

마지막 갱신: 2026-06-10

이 문서는 현재 플레이 기준으로 승격한 `icecoke-cobblemon-173` 라인의 상태를 기록한다. 기존 `1.6.1` 서버는 `icecoke-cobblemon-161` 레거시 라인으로 보존한다.

## 서버 라인 분리

| 항목 | 161 레거시 라인 | 173 현재 라인 |
| --- | --- | --- |
| 경로 | `/home/icenux/minecraft/mingle-lounge` | `/home/icenux/minecraft/icecoke-cobblemon-173-test` |
| screen | `mingle-sample` | `icecoke-173` |
| 포트 | `25565` | `25566` |
| MOTD | `icecoke-cobblemon-161` | `icecoke-cobblemon-173` |
| 월드 | 기존 `world/` | `world-auto-backup-20260605-190011.tar.gz`에서 복원한 복사본 |
| JVM | `Xms2G`, `Xmx6G` | `Xms1G`, `Xmx4G` |

173 라인의 실제 경로에는 과거 테스트 인스턴스 이름인 `icecoke-cobblemon-173-test`가 남아 있다. 안정성을 위해 파일 이동은 하지 않고, 표시명과 운영 명칭만 `icecoke-cobblemon-173`으로 사용한다.

## 접속 정보

```text
192.168.219.110:25566
```

로컬에서 TCP 접속 확인:

```bash
nc -vz -G 3 192.168.219.110 25566
```

## 기동 명령

```bash
ssh icenux-ms7b23
cd /home/icenux/minecraft/icecoke-cobblemon-173-test
./start-screen.sh
./stop.sh
./attach.sh
```

콘솔 명령:

```bash
screen -S icecoke-173 -p 0 -X stuff $'list\r'
```

## 현재 검증 결과

1. 최초 기동 실패: 운영 서버의 Fabric Loader `0.16.14`는 `Cobblemon 1.7.3` 요구 조건을 만족하지 못했다.
2. 173 라인 전용 Fabric server launcher를 `Minecraft 1.21.1 / Fabric Loader 0.17.3 / launcher 1.0.3`으로 교체했다.
3. 두 번째 기동 실패: 운영 월드의 `level.dat`가 `terralith:*` 바이옴/월드젠을 참조했지만 173 라인 모드셋에 Terralith 계열이 없어 `Overworld settings missing`으로 종료됐다.
4. 173 라인에 월드젠 필수 모드 `Terralith`, `TerraBlender`, `lithostitched`, `Oh The Trees You'll Grow`, `Woodlands Extra`, `Woodlands Vanilla`를 추가했다.
5. 이후 서버 기동 성공: `Done (2.168s)!`, 25566 리슨 확인, `list` 응답 확인.
6. `LegendaryMonuments` 블록 registry 오류를 줄이기 위해 `LegendaryMonuments`, `chipped`, `resourcefullib`, `athena`, `CobbleFurnies`, `geckolib`, `trinkets`를 173 라인에 추가했다.
7. 재기동 성공: `Done (2.147s)!`, 25566 리슨 확인, `list` 응답 확인, 로컬 TCP 접속 확인.
8. 로컬 Mac에 별도 Modrinth 프로필 `icecoke-cobblemon-173`를 만들고, 서버와 같은 33개 모드 구성으로 `192.168.219.110:25566` 접속을 확인했다.
9. 서버 로그 기준 `Icecokel joined the game` 확인 후 약 1분 동안 즉시 disconnect가 없었다. 테스트 종료 후 클라이언트를 닫았고 서버 `list` 기준 접속자는 0명이다.
10. 추가 인게임 검증에서 `Icecokel`이 16:40:29 접속 후 16:46:26 `list` 기준 온라인 상태로 남아 있어 5분 이상 접속 유지 조건을 통과했다.
11. 화면 기준 월드 렌더링, Cobblemon 파티 UI, PC UI, 주변 포켓몬 모델, 미니맵 표시를 확인했다.
12. 사용자가 인게임에서 전투 1회 성공과 포획 성공을 확인했다.
13. 1.7.3 적용 가능 후보 중 핵심 gameplay/관장/진행/이동/음식 계열 17개를 173 라인과 로컬 173 프로필에 추가했다. 편의 UI/단순 시각/성능 튜닝 모드는 보류했다.
14. 당시 실행 중이던 25566 서버는 재시작 전이라 새 모드가 로드되지 않았고, 별도 임시 디렉터리에서 같은 모드셋으로 포트 25567 부팅 검증을 수행해 `Done (10.514s)!`, `Registered 1559 trainers`를 확인했다.
15. 추가로 관장/NPC 보조용 `Easy NPC 6.2.0 bundle`과 Cobblemon 1.7 riding 데이터 확장용 `Gotta Ride 'Em All 1.0`을 173 라인과 로컬 173 프로필에 추가했다. `Cobblemon: Ride On! / cobbleride 0.3.3`은 metadata상 `Cobblemon >=1.7`과 충돌해 제외했다.
16. 추가 후 별도 임시 디렉터리에서 같은 모드셋으로 포트 25567 부팅 검증을 다시 수행했고 `Done (9.118s)!`, `Registered 1559 trainers`를 확인했다.
17. 25566 173 라인을 재시작해 실제 서버에 52개 모드셋을 로드했다. 로그 기준 `Done (1.602s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`, 콘솔 `list` 응답을 확인했다.
18. RCTMod 기본 설정으로 `initialLevelCap = 15`가 다시 생성되어 경험치 상한이 걸리는 것을 확인했다. 기존 운영 원칙에 맞춰 `config/rctmod-server.toml`을 `initialLevelCap = 100`으로 변경했다. 변경 전 백업은 `backups/rctmod-server-before-levelcap-173-20260607-193024.toml`이다.
19. 25566 173 라인을 재시작해 `initialLevelCap = 100`을 반영했다. 로그 기준 `Done (1.590s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`, 콘솔 `list` 응답을 확인했다.
20. 161 레거시의 남은 가벼운 모드를 173 라인에 추가 검증하기 전 현재 인스턴스를 백업했다. 백업은 `backups/instance-before-light-main-mods-test-20260607-194954.tar.gz`이며, `sha256sum -c` 검증 결과 `OK`다. 후보 목록은 `COBBLEMON_173_MOD_GAP.md`에 기록했다.
21. 1차 가벼운 후보 중 서버 적용 대상 `Fight or Flight 0.10.7`, `Clumps 19.0.0.1`, `FerriteCore 7.0.3`, `Krypton 0.2.8`을 173 라인에 추가했다. 로컬 173 프로필에는 필수 `Fight or Flight`와 클라이언트 편의 `JEI 19.27.0.340`, `EntityCulling 1.10.2`, `Just Zoom 2.1.0`, `Konkrete 1.9.9`를 추가했다.
22. 25566 173 라인을 재시작해 56개 서버 모드셋을 로드했다. 로그 기준 `Fight or Flight`, `FOF tasks injected`, `Krypton`, `Done (1.823s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`를 확인했다.
23. 로컬 `icecoke-cobblemon-173` 프로필을 CLI로 1회 실행해 `192.168.219.110:25566`에 접속했다. 로컬 로그 기준 `Connecting to 192.168.219.110, 25566`, `Applying server overrides`, `Minimap updated server level id`를 확인했고, 서버 로그 기준 `Icecokel joined the game` 후 테스트 종료 시 `lost connection: Disconnected`를 확인했다.
24. `Berry Pouch 0.5.4-beta`와 `Cobblemon Extra Structures 1.3.0`을 추가하기 전 173 인스턴스를 백업했다. 백업은 `backups/instance-before-berry-structures-20260607-210909.tar.gz`이며, `sha256sum -c` 검증 결과 `OK`다.
25. 25566 173 라인을 재시작해 58개 서버 모드셋을 로드했다. 로그 기준 `Found new data pack berrypouch`, `Found new data pack cobblemonextrastructures`, `Done (1.665s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`를 확인했다.
26. 로컬 `icecoke-cobblemon-173` 프로필을 CLI로 실행해 `192.168.219.110:25566`에 접속했다. 로컬 로그 기준 `Connecting to 192.168.219.110, 25566`, `Applying server overrides`, `Minimap updated server level id`를 확인했고, 서버 로그 기준 `Icecokel joined the game` 후 테스트 종료 시 `lost connection: Disconnected`를 확인했다.
27. 173 라인에서 CobbleBuilds 관장/체육관 일반 트레이너 파티 override 경로를 `data/cobblebuilds/molang/party/...`로 맞췄고, `mingle-gym-party-overrides.zip`이 서버 datapack으로 로드되는 것을 확인했다.
28. RCTMod 자연 스폰 일반 트레이너가 배지 수가 아니라 파티 최고 레벨 기준으로 후보를 고르는 것을 확인했다. 과한 고레벨 일반 트레이너를 줄이기 위해 `config/rctmod-server.toml`의 `maxLevelDiff`를 `25`에서 `5`로 낮췄다. 변경 전 백업은 `backups/rctmod-server-before-max-level-diff-5-20260610-230730.toml`이다.
29. 25566 173 라인을 재시작해 `maxLevelDiff = 5`를 반영했다. 로그 기준 `Done (1.750s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`, 로컬 TCP 접속 성공을 확인했다.

## 현재 173 라인 모드 구성

공식 `Cobblemon 1.7.3` 프로필 기반 모드 20개에 운영 월드 로딩에 필요한 월드젠/블록 의존 모드와 1.7.3 적용 가능 핵심 기능 모드를 추가한 상태다. 현재 173 라인 모드 수는 58개다.

핵심 버전:

| 항목 | 값 |
| --- | --- |
| Minecraft | `1.21.1` |
| Fabric Loader | `0.17.3` |
| Cobblemon | `1.7.3+1.21.1` |
| Mega Showdown | `1.8.4+1.7.3+1.21.1` |
| Cobblemon Spawn Alerts | `1.13.2` |
| 포트 | `25566` |

추가 적용한 핵심 모드:

| 구분 | 모드 |
| --- | --- |
| Cobblemon 1.7.x 명시 대응 | `CobbleCuisine 2.0.1-1.7-rc1`, `CobblemonRepel 1.7-1.4`, `Cobbreeding 2.2.1`, `SimpleTMs 2.3.3`, `Cobblemon Armors 1.6.0+1.7.3`, `DropLootTables 1.7.3-fabric-1.9.1`, `Extra Move Animations 1.7v1.0.2` |
| 관장/배지/진행 | `CobbleBuilds Leaders 0.1.1-hf.1`, `BadgeBox 1.3.0`, `RCTApi 0.15.2-beta`, `RCTMod 0.18.1-beta`, `Easy NPC 6.2.0 bundle` |
| 음식/잔여 참조 | `Farmer's Delight Refabricated 1.21.1-3.2.8`, `CobbleCuisine Delight 1.1` |
| 이동 콘텐츠 | `Immersive Aircraft 1.4.6`, `Gliders 1.1.8`, `Gotta Ride 'Em All 1.0` |
| 본섭 체감/성능 1차 테스트 | `Fight or Flight 0.10.7`, `Clumps 19.0.0.1`, `FerriteCore 7.0.3`, `Krypton 0.2.8` |
| 베리/구조물 2차 테스트 | `Berry Pouch 0.5.4-beta`, `Cobblemon Extra Structures 1.3.0` |
| 의존성 조정 | `ForgeConfigAPIPort 21.1.6`, `Common Network 1.0.21`, `GeckoLib 4.8.4`, `Tim Core 1.7.3-fabric-1.32.0` |

로컬 173 프로필 전용 추가:

| 구분 | 모드 |
| --- | --- |
| 서버 필수 대응 | `Fight or Flight 0.10.7`, `Berry Pouch 0.5.4-beta` |
| 클라이언트 편의 | `JEI 19.27.0.340`, `EntityCulling 1.10.2`, `Just Zoom 2.1.0`, `Konkrete 1.9.9`, `Cobblemon Extra Structures 1.3.0` |

보류한 모드:

- 편의 UI/표시: `Show Held Items`, `Sound Physics`, 사진/카메라 계열. `Show Held Items 0.2.3`은 metadata 기준 `Cobblemon 1.6.1` 고정 의존성이라 1.7.3 테스트에서 제외했다.
- 단순 성능 튜닝: `Lithium`, `ServerCore`. `Clumps`, `FerriteCore`, `Krypton`은 1차 서버 테스트에 추가했다.
- 중복 가능성이 큰 보관 모드: `Sophisticated Backpacks` 계열. 1.7.3 테스트에는 이미 `Inmis`가 있다.
- 출처 또는 1.7.3 호환성이 불명확한 항목: `Cobblemon Legends Reborn`, `rocket_mons`, `Farsight`, `Cupboard`.
- 1.6 계열까지만 확인된 항목: `Shearems`, `Unimplemented Items`, `Whiteout`.

## 남은 이슈

현재 173 라인은 켜지고 접속/전투/포획까지 확인됐지만, 161 레거시 라인의 모든 기능과 parity가 맞는 상태는 아니다.

확인된 로그 이슈:

- `LegendaryMonuments` 일부 loot table이 `mega_showdown:blueorb`, `mega_showdown:redorb`, `mega_showdown:firium-z`를 찾지 못한다. 1.7.3용 Mega Showdown에서 아이템 ID가 바뀐 것으로 보이며, loot table 패치 또는 모드 조합 재검토가 필요하다.
- `Cobblemon Extra Structures 1.3.0`은 서버 부팅과 로컬 접속은 통과했지만, 로그에 `cobblemonextrastructures:sprout_tower` advancement가 `cobblemonextrastructures:bellsprout_statue` 아이템을 찾지 못하는 경고가 남는다. 구조물 월드젠 자체 영향은 신규 청크 탐색으로 추가 확인이 필요하다.
- `cobblemon-unimplementeditems-1.6-fabric-1.1.0.jar`는 metadata 기준 `cobblemon <=1.7.0`이라 1.7.3 173 라인에 넣지 않았다. 운영 월드에 남아 있는 `unimplemented_items:dry_root` 참조는 invalid item으로 기록된다.
- `Farmer's Delight`, `CobbleCuisine`, `CobbleCuisine Delight`를 173 라인에 추가했고, 25566 173 라인 재시작 후 로드했다.
- 클라이언트에는 Cobblemon/Xaero 한국어 파일 parse 경고, Cobblemon particle `LICENSE` invalid path 경고, 일부 missing texture/sound 경고가 남아 있다.
- 161 레거시 라인의 데일리/Hermes 전체 기능은 아직 1.7.3 173 라인으로 이관하지 않았다.
- 관장/배지/체육관 일반 트레이너는 데이터팩 override와 서버 로드는 확인했지만, 실제 배지 지급과 장기 밸런스는 추가 인게임 검증이 필요하다.
- RCTMod 설정은 `initialLevelCap = 100`, `maxLevelDiff = 5`, `forceBattleMaxLevelDiff = 16`으로 맞췄고, 25566 173 라인 재시작 후 반영 확인까지 완료했다.

## 다음 검증 순서

1. 관장 marker/NPC/전투/배지 지급과 데이터팩 override 밸런스를 확인한다.
2. 스폰 알림이 실제 조건에서 표시되는지 확인한다.
3. Xaero World Map 전체 화면 키 바인딩을 확인한다.
4. 가방, 배지 보관, 보상, 지도, 리소스팩 호환성을 확인한다.
5. 로그에서 unknown registry key가 실제 플레이에 미치는 영향을 분류한다.

173 라인은 현재 플레이 기준으로 승격했지만, 관장/배지/데일리/Hermes 이관은 위 검증이 끝난 뒤 별도 작업으로 진행한다.
