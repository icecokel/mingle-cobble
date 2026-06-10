# Gym Placement Log

마지막 갱신: 2026-06-03

이 문서는 관장/NPC/체육관 배치 작업의 실제 변경 좌표와 되돌리기 기준을 기록한다.

## Gym Candidate Survey

아래 좌표는 region/POI/heightmap 기반 1차 후보이며, 실제 배치 전에는 인게임 지면, 공간, 구조물 footprint 확인이 필요하다. Y 좌표는 heightmap 기준 후보 표면 높이다.

| Gym ID | Candidate XYZ | Biome/terrain evidence | Distance/routing | Risk |
| --- | --- | --- | --- | --- |
| `rock_gym` | `-40 175 -536` | `terralith:highlands`, 평균 Y `174.9`, 최고 Y `191`, block palette에 `stone`, `lava`, `water` 확인 | 스폰 기준 약 `537m`, 북북서 | 산/절벽형 후보로 강함. 평탄 공간 확인 필요. 기존 테스트 marker `2 68 -359`와 실제 건물 배치 후보를 혼동하지 않는다. |
| `grass_gym` | `72 132 360` | `terralith:blooming_plateau` + `highlands`, `grass_block`, 완만한 plateau | 스폰 기준 약 `367m`, 남동 | 꽃/초원 계열 대체 후보. 실제 꽃/식생 밀도와 구조물 공간 확인 필요. |
| `water_gym` | `40 127 8` | `minecraft:river`, block palette에 `water`, `sand`, `stone` 확인 | 스폰 기준 약 `41m`, 동쪽 | 스폰에 너무 가까워 3번째 관장 동선으로는 재검토 필요. |
| `electric_gym` | `-24 152 152` | `terralith:highlands`, 평균 Y `151.9`, 최고 Y `163` | 스폰 기준 약 `154m`, 남서 | 고지대/탑 컨셉 후보. 평원 마을 근거는 없음. |
| `fire_gym` | `-24 133 -56` | `terralith:highlands`, block palette에 `lava`, `stone` 확인 | 스폰 기준 약 `61m`, 북서 | 사막/악지 후보가 아니라 컨셉 근거가 약함. lava가 지표인지 동굴인지 확인 필요. 추가 탐사 권장. |
| `poison_gym` | `24 131 392` | `minecraft:river` + `terralith:blooming_valley/highlands`, `water`, `grass_block` 확인 | 스폰 기준 약 `393m`, 남남동 | 늪/어두운 숲/습지 근거가 약함. 추가 탐사 후 재선정 권장. |
| `ice_gym` | `216 137 -376` | `terralith:alpine_highlands`, block palette에 `ice`, `water`, `stone` 확인 | 스폰 기준 약 `434m`, 북동 | 설산/고산 후보. 눈 덮인 지형인지 인게임 확인 필요. CobbleBuilds 건물 구조물이 없어 수동 거점 필요. |
| `steel_gym` | `344 132 360` | 주변 POI에 `home`, `mason`, `butcher` 등 마을 흔적, 인접 강 후보 | 스폰 기준 약 `498m`, 남동 | 강변 마을형 수동 거점 후보. 큰 마을 중심인지, POI가 지표 구조물인지 인게임 확인 필요. 작은 신호기 위치 후보도 함께 확인한다. |

1차 판단:

- 우선 검증 후보: `rock_gym`, `grass_gym`, `ice_gym`, `steel_gym`
- 동선 재검토 후보: `water_gym`, `electric_gym`
- 추가 탐사 권장 후보: `fire_gym`, `poison_gym`

## Placement Command Template

실제 적용 전에는 관장 1개 단위로 백업, 배치, 저장, 검증, 기록을 끝낸다. 아래 값은 조사 결과 통합 후 채운다.

| Field | Value |
| --- | --- |
| Gym ID | 확인 필요 |
| Dimension | `minecraft:overworld` |
| Target XYZ | 확인 필요 |
| Structure ID | 구조물 지원 타입은 `cobblebuilds:<gym_id>` |
| NPC ID | 아래 NPC ID 표 기준 |
| Marker name | 확인 필요 |
| Rollback target | marker/NPC는 좌표, `gym`, `npc` data 조건으로만 제거. 구조물은 고위험 백업 복구 대상으로 본다. |

NPC ID:

| Gym ID | NPC ID | 주의 |
| --- | --- | --- |
| `rock_gym` | `gym_leader.rock_gym.brock` | 기존 테스트 marker 사용 ID |
| `grass_gym` | `gym_leader.grass_gym.erika` |  |
| `water_gym` | `gym_leader.water_gym.misty` |  |
| `electric_gym` | `gym_leader.electric_gym.ltsurge` |  |
| `fire_gym` | `gym_leader.fire_gym.blaine` |  |
| `poison_gym` | `gym_leader.poison_gym.koga` |  |
| `ice_gym` | `gym_leader.ice_gym.pryce` | NPC/party는 있으나 variation 내부값이 Lt. Surge/Steve placeholder로 보여 외형 검증 필요 |
| `steel_gym` | `gym_leader.steel_gym.jasmine` | NPC/party는 있으나 variation 내부값이 Lt. Surge/Steve placeholder로 보여 외형 검증 필요 |

명령 템플릿:

```mcfunction
# 1. 적용 전 백업: OPS_RUNBOOK.md 절차 기준으로 world/ 백업 생성

# 2. 필요 시 대상 청크 임시 로드
forceload add <x> <z>

# 3. 건물 구조물 배치, 구조물이 있는 짐만 사용
place template cobblebuilds:<gym_id> <structure_x> <structure_y> <structure_z> none none 1.0 0

# 4. gym marker 생성
summon marker <x> <y> <z> {Tags:["cobblebuilds-gym"],data:{gym:"<gym_id>",name:"<gym_id>"}}

# 5. NPC spawner marker 생성
summon marker <x>.5 <y>.5 <z>.5 {Tags:["cobblebuilds-npc_spawner"],data:{type:"gym_leader",npc_data:{},on_spawn:"",base:{npc_data:{Tags:["cobblebuilds-gym_leader"]},condition:"if function cobblebuilds:condition/npc_spawner/gym_leader"},npc:"<npc_id>",child:[I;],gym:"<gym_id>",on_delete:"",name:"<marker_name>",condition:""}}

# 6-1. 구조물 배치 확인
# 구조물은 배치된 ID를 직접 조회하기 어렵다.
# 배치 전 정한 앵커 블록 좌표를 execute if block으로 확인하거나 인게임 육안 확인한다.
execute if block <anchor_x> <anchor_y> <anchor_z> <expected_block>

# 6-2. gym marker 확인
execute positioned <x>.5 <y>.5 <z>.5 run data get entity @e[type=marker,tag=cobblebuilds-gym,nbt={data:{gym:"<gym_id>"}},distance=..1,limit=1] data

# 6-3. NPC spawner marker 확인
execute positioned <x>.5 <y>.5 <z>.5 run data get entity @e[type=marker,tag=cobblebuilds-npc_spawner,nbt={data:{gym:"<gym_id>",npc:"<npc_id>",type:"gym_leader"}},distance=..1,limit=1] data

# 6-4. 실제 cobblemon:npc 생성 확인
# CobbleBuilds spawner는 플레이어 근접 조건이 있으므로 콘솔만으로 안 보이면 확인 필요로 남긴다.
execute positioned <x>.5 <y>.5 <z>.5 run data get entity @e[type=cobblemon:npc,tag=cobblebuilds-gym_leader,distance=..32,sort=nearest,limit=1]

# 7. 저장
save-all flush

# 8. 임시 청크 로드 해제
forceload remove <x> <z>
```

되돌리기 템플릿:

```mcfunction
# 실제 좌표와 tag/data 조건을 확인한 뒤 관장 1개 범위만 제거한다.
execute positioned <x>.5 <y>.5 <z>.5 run kill @e[type=marker,tag=cobblebuilds-gym,nbt={data:{gym:"<gym_id>"}},distance=..1]
execute positioned <x>.5 <y>.5 <z>.5 run kill @e[type=marker,tag=cobblebuilds-npc_spawner,nbt={data:{gym:"<gym_id>",npc:"<npc_id>",type:"gym_leader"}},distance=..1]
save-all flush
```

실제 `cobblemon:npc` 본체는 반경 조건만으로 일괄 삭제하지 않는다. 제거가 필요하면 먼저 `data get entity`로 대상 NPC를 확인하고, UUID 또는 정확한 식별 조건을 기록한 뒤 1개 개체만 제거한다.

구조물은 `place template`에 undo가 없으므로 범용 `fill ... air` 롤백을 쓰지 않는다. 구조물 배치 후 되돌려야 하면 배치 직전 `world/` 백업 복구가 필요하다. 이 복구는 서버 정지, 파일 교체, 재시작, marker/entity 재조회, 인게임 확인 전까지 완료로 보지 않는다.

## 2026-06-03 바위 관장 테스트 배치

목적:

- 전체 체육관 구조물이 아니라 바위 관장 NPC 스포너 1개만 테스트 배치한다.
- CobbleBuilds 내장 `rock_gym` 보상/배지 흐름과 `gym_leader.rock_gym.brock` NPC를 먼저 검증한다.

사전 백업:

- 실행 중 저장 후 백업: `backups/world-20260603-170232.tar.gz`
- 서버 정지 후 백업: `backups/world-stopped-20260603-171613.tar.gz`

기준 위치:

- 월드 스폰: `0 65 0`
- 플레이어 마지막 위치: `1.82 68.00 -358.82`
- 플레이어 리스폰 위치: `11 68 -338`

배치 계획:

- 차원: `minecraft:overworld`
- Gym ID: `rock_gym`
- NPC ID: `gym_leader.rock_gym.brock`
- 테스트 배치 좌표: `2 68 -359`

배치 방식:

- `cobblebuilds:gym/create`로 gym marker 생성
- `cobblebuilds:npc_spawner/create/gym_leader`로 관장 NPC 스포너 marker 생성
- 플레이어가 gym marker 반경 32블록 안에 들어오면 CobbleBuilds tick 함수가 NPC를 소환한다.

실제 적용:

- 적용 시각: 2026-06-03 17:21 KST
- 서버를 임시 기동해 명령으로 marker를 생성한 뒤 `save-all flush` 후 다시 종료했다.
- 함수 직접 호출은 콘솔 `@s` 문제로 marker가 생성되지 않아, 같은 NBT 구조의 marker를 직접 소환했다.
- 좌표 청크를 `forceload add 2 -359`로 임시 로드해 생성/조회/저장을 확인했다.
- 저장 후 `forceload remove 2 -359`를 실행했고, 해당 청크가 force loaded 상태가 아님을 확인했다.
- 검증 로그: `logs/local-server.log` 5071-5088

생성 확인:

- Gym marker data: `{gym: "rock_gym", name: "rock_gym"}`
- NPC spawner data: `{type: "gym_leader", npc: "gym_leader.rock_gym.brock", gym: "rock_gym", name: "Rock Gym Leader Brock Test"}`

서버 재기동 후 검증:

- 검증 시각: 2026-06-03 18:40-18:42 KST
- 서버 기동 확인: `Done (2.037s)! For help, type "help"`
- 포트 확인: `*:25565` 리슨 확인
- `forceload add 2 -359` 후 marker 조회 확인
- `cobblebuilds-gym` marker와 `cobblebuilds-npc_spawner` marker가 같은 좌표에 저장되어 있음 확인
- 검증 후 `forceload remove 2 -359` 실행

현재 한계:

- 콘솔 기준으로 `cobblemon:npc` 실제 Brock NPC는 아직 생성되지 않았다.
- CobbleBuilds spawner 조건은 `execute as @a` 기반이라 플레이어가 해당 gym 상태에 들어와야 활성화된다.
- 다음 검증은 클라이언트 접속 후 `2 68 -359` 근처에서 Brock NPC가 실제로 소환되는지 확인한다.

주의:

- 이 작업은 `docs/server/GYM_TEAMS.md`의 3마리 초급 팀을 그대로 구현하지 않는다.
- 현재 테스트는 CobbleBuilds 내장 Brock 파티 스크립트를 사용한다.
- 구조물 `cobblebuilds:rock_gym`은 아직 배치하지 않는다.

## CobbleBuilds 짐 건물 확인

확인 시각: 2026-06-03

CobbleBuilds jar 기준으로 기본 건물 구조물과 월드젠 정의가 확인된 짐은 아래 6개다.

| Gym ID | 건물 구조물 | 월드젠 정의 |
| --- | --- | --- |
| `rock_gym` | `data/cobblebuilds/structure/rock_gym.nbt` | 있음 |
| `grass_gym` | `data/cobblebuilds/structure/grass_gym.nbt` | 있음 |
| `water_gym` | `data/cobblebuilds/structure/water_gym.nbt` | 있음 |
| `electric_gym` | `data/cobblebuilds/structure/electric_gym.nbt` | 있음 |
| `fire_gym` | `data/cobblebuilds/structure/fire_gym.nbt` | 있음 |
| `poison_gym` | `data/cobblebuilds/structure/poison_gym.nbt` | 있음 |

`ice_gym`, `steel_gym`은 관장 NPC/파티 리소스는 있으나 현재 jar 안에서 건물 `.nbt` 구조물과 월드젠 정의를 찾지 못했다. 이 두 타입은 기본 건물 자동 배치 대상이 아니라, `ice_gym`은 설산에, `steel_gym`은 강을 끼고 있는 마을에 수동 거점을 만든 뒤 gym marker와 NPC spawner를 붙이는 방식으로 진행한다.

`steel_gym` 마을에는 강변 공방이나 마을 광장 근처에 작은 신호기를 둔다. 이 신호기는 위치 안내용 표식이며, 초기 배치에서는 상시 Beacon 버프 제공을 목표로 하지 않는다.

건물 배치와 관장 스포너 배치는 별도 작업으로 본다. 현재 월드에 실제로 배치된 것은 `2 68 -359`의 바위 관장 테스트용 marker 2개뿐이며, `rock_gym` 건물 구조물은 아직 월드에 배치하지 않았다.

## 2026-06-03 8관장 월드 배치

목적:

- 8관장 후보 좌표에 gym marker와 gym leader spawner marker를 배치한다.
- CobbleBuilds 기본 건물이 있는 6개 타입은 `place template`으로 체육관 건물을 배치한다.
- 건물 구조물이 없는 `ice_gym`, `steel_gym`은 marker/spawner 중심으로 배치한다.
- `steel_gym`에는 위치 안내용 작은 신호기를 추가한다.

사전 백업:

- 실행 중 저장 후 백업: `backups/world-before-gyms-20260603-194053.tar.gz`
- 해시 파일: `backups/world-before-gyms-20260603-194053.tar.gz.sha256`
- 검증 결과: `sha256sum -c` OK

기존 테스트 정리:

- 기존 바위 관장 테스트 marker/spawner 위치: `2.5 68.5 -358.5`
- `rock_gym` 테스트 gym marker 제거 확인
- `rock_gym` 테스트 NPC spawner marker 제거 확인

배치 결과:

| Gym ID | Structure | Marker XYZ | NPC ID | 검증 |
| --- | --- | --- | --- | --- |
| `rock_gym` | `cobblebuilds:rock_gym` at `-158 144 -435` | `-141.5 145.5 -415.5` | `gym_leader.rock_gym.brock` | 지면 기준 재배치 후 gym marker/spawner marker 확인 |
| `grass_gym` | `cobblebuilds:grass_gym` at `24 132 331` | `40.5 133.5 350.5` | `gym_leader.grass_gym.erika` | 지면 기준 재배치 후 gym marker/spawner marker 확인 |
| `water_gym` | `cobblebuilds:water_gym` at `30 127 -23` | `46.5 128.5 -3.5` | `gym_leader.water_gym.misty` | 지면 기준 재배치 후 gym marker/spawner marker 확인 |
| `electric_gym` | `cobblebuilds:electric_gym` at `-22 136 83` | `-5.5 137.5 102.5` | `gym_leader.electric_gym.ltsurge` | 지면 기준 재배치 후 gym marker/spawner marker 확인 |
| `fire_gym` | `cobblebuilds:fire_gym` at `-30 137 -63` | `-13.5 138.5 -43.5` | `gym_leader.fire_gym.blaine` | 지면 기준 재배치 후 gym marker/spawner marker 확인 |
| `poison_gym` | `cobblebuilds:poison_gym` at `-18 128 347` | `-1.5 129.5 366.5` | `gym_leader.poison_gym.koga` | 지면 기준 재배치 후 gym marker/spawner marker 확인 |
| `ice_gym` | 없음 | `216.5 138.5 -376.5` | `gym_leader.ice_gym.pryce` | gym marker/spawner marker 지연 재조회 확인 |
| `steel_gym` | 없음 | `344.5 134.5 360.5` | `gym_leader.steel_gym.jasmine` | gym marker/spawner marker 지연 재조회 확인 |

강철 관장 신호기:

- Iron base: `fill 343 132 359 345 132 361 minecraft:iron_block`
- Beacon: `setblock 344 133 360 minecraft:beacon`
- 목적: 위치 안내용 시각 표식
- 초기 범위: 상시 Beacon 버프 제공을 목표로 하지 않음

검증:

- 6개 구조물 배치 로그 확인:
  - 최신 좌표는 아래 `2026-06-03 지면 기준 gym 재보정` 섹션을 우선한다.
- 8개 gym marker 지연 재조회 확인
- 8개 NPC spawner marker 지연 재조회 확인
- `save-all flush` 후 저장 확인
- `forceload query` 결과: `No force loaded chunks were found in minecraft:overworld`
- 서버 포트 `25565` 리슨 유지 확인

주의:

- 실제 `cobblemon:npc` 관장 본체 생성은 플레이어가 해당 gym 상태/영역에 들어가야 활성화될 수 있으므로 인게임 확인 필요.
- 관장 전투, 승리 처리, 배지/보상 지급은 아직 확인하지 않았다.
- `ice_gym`, `steel_gym`은 NPC/party 리소스는 있으나 variation 내부값이 placeholder로 보일 수 있어 외형 확인 필요.
- `fire_gym`, `poison_gym`은 원래 컨셉 바이옴 근거가 약한 후보였으므로, 인게임 지형이 어색하면 백업 기준으로 롤백하거나 후보 재선정한다.

## 2026-06-03 떠 있는 gym 구조물 1차 보정

목적:

- 인게임에서 일부 gym 구조물이 공중에 떠 있는 것처럼 보이는 문제를 줄인다.
- CobbleBuilds 기본 건물이 있는 6개 gym은 구조물을 제거한 뒤 하단 받침을 추가하고 다시 배치한다.
- `ice_gym`, `steel_gym`은 건물 구조물이 없으므로 이번 보정 대상에서 제외한다.

결론:

- 이 보정은 검증 기준이 부족했다.
- 구조물 바로 아래 한 칸만 solid인지 확인했기 때문에, 받침 자체가 실제 지면에서 수십 블록 위에 떠 있는 상태를 놓쳤다.
- 실제 최종 수정은 아래 `2026-06-03 지면 기준 gym 재보정` 섹션을 우선한다.

사전 백업:

- 실행 중 저장 후 백업: `backups/world-before-gym-fix-20260603-210538.tar.gz`
- 해시 파일: `backups/world-before-gym-fix-20260603-210538.tar.gz.sha256`
- 검증 결과: `sha256sum -c` OK

보정 방식:

- 대상 6개 구조물 범위를 먼저 `fill ... air replace`로 제거했다.
- 같은 범위의 기존 gym marker와 NPC spawner marker를 `gym`, `npc`, `type` data 조건으로 제거했다.
- 각 구조물 footprint는 `33 x 39` 기준으로 보고, 구조물 바로 아래 `Y - 1` 한 층에 `minecraft:stone` 받침을 `replace air` 방식으로 추가했다.
- `electric_gym`, `fire_gym`, `poison_gym`은 지형 기준으로 Y를 다시 잡아 재배치했다.
- 모든 재배치 후 `save-all flush`를 실행했다.
- 임시 `forceload` 청크는 모두 해제했고, `forceload query` 결과 `No force loaded chunks were found in minecraft:overworld`를 확인했다.

최종 구조물/마커:

| Gym ID | Structure | Foundation Y | Marker XYZ | NPC ID | 검증 |
| --- | --- | --- | --- | --- | --- |
| `rock_gym` | `cobblebuilds:rock_gym` at `-56 175 -555` | `174` | `-40.5 176.5 -536.5` | `gym_leader.rock_gym.brock` | 하단 비공기 블록, gym marker/spawner marker 확인 |
| `grass_gym` | `cobblebuilds:grass_gym` at `56 132 341` | `131` | `72.5 133.5 360.5` | `gym_leader.grass_gym.erika` | 하단 비공기 블록, gym marker/spawner marker 확인 |
| `water_gym` | `cobblebuilds:water_gym` at `24 127 -11` | `126` | `40.5 128.5 8.5` | `gym_leader.water_gym.misty` | 하단 비공기 블록, gym marker/spawner marker 확인 |
| `electric_gym` | `cobblebuilds:electric_gym` at `-40 133 133` | `132` | `-24.5 134.5 152.5` | `gym_leader.electric_gym.ltsurge` | 하단 비공기 블록, gym marker/spawner marker 확인 |
| `fire_gym` | `cobblebuilds:fire_gym` at `-40 138 -75` | `137` | `-24.5 139.5 -56.5` | `gym_leader.fire_gym.blaine` | 하단 비공기 블록, gym marker/spawner marker 확인 |
| `poison_gym` | `cobblebuilds:poison_gym` at `8 127 373` | `126` | `24.5 128.5 392.5` | `gym_leader.poison_gym.koga` | 하단 비공기 블록, gym marker/spawner marker 확인 |

검증 로그 요약:

- 6개 구조물 재배치 로그 확인:
  - `Loaded template "cobblebuilds:rock_gym" at -56, 175, -555`
  - `Loaded template "cobblebuilds:grass_gym" at 56, 132, 341`
  - `Loaded template "cobblebuilds:water_gym" at 24, 127, -11`
  - `Loaded template "cobblebuilds:electric_gym" at -40, 133, 133`
  - `Loaded template "cobblebuilds:fire_gym" at -40, 138, -75`
  - `Loaded template "cobblebuilds:poison_gym" at 8, 127, 373`
- `FIX_SOLID_BELOW_rock`, `FIX_SOLID_BELOW_grass`, `FIX_SOLID_BELOW_water`, `FIX_SOLID_BELOW_electric`, `FIX_SOLID_BELOW_fire`, `FIX_SOLID_BELOW_poison` 확인
- 6개 gym marker 재조회 확인
- 6개 NPC spawner marker 재조회 확인
- `save-all flush` 후 저장 확인

남은 확인:

- 콘솔 기준 구조물과 marker 저장은 확인했다.
- 실제 시야에서 어색한 절벽, 받침 노출, 진입 동선은 클라이언트 접속 후 육안 확인이 필요하다.

## 2026-06-03 지면 기준 gym 재보정

목적:

- 1차 보정의 실패 기준을 폐기하고, 실제 자연 지형 heightmap 기준으로 6개 건물형 gym을 다시 배치한다.
- `rock_gym`이 스크린샷 기준 `-55 111 -558` 근처에서 약 64블록 위에 떠 있던 문제를 해결한다.

사전 백업:

- 실행 중 저장 후 백업: `backups/world-before-gym-groundfix-20260603-212831.tar.gz`
- 해시 파일: `backups/world-before-gym-groundfix-20260603-212831.tar.gz.sha256`
- 검증 결과: `sha256sum -c` OK

검증 기준:

- 기존 구조물과 받침 제거 후 `save-all flush`를 실행했다.
- 제거 후 region heightmap을 읽어 각 후보의 `33 x 39` footprint 자연 지형 높이를 계산했다.
- heightmap 값은 지면 위 첫 공기 높이로 보고, 구조물 배치 Y는 `maxH`로 잡았다.
- 통과 기준은 `max_gap <= 6`, `center_gap <= 4`, `avg_gap <= 4`다.
- `max_gap`은 `maxH - minH`로 계산한다.

최종 구조물/마커:

| Gym ID | Structure | Marker XYZ | NPC ID | minH | maxH/baseY | max gap | center gap | avg gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `rock_gym` | `cobblebuilds:rock_gym` at `-158 144 -435` | `-141.5 145.5 -415.5` | `gym_leader.rock_gym.brock` | `139` | `144` | `5` | `2` | `2.59` |
| `grass_gym` | `cobblebuilds:grass_gym` at `24 132 331` | `40.5 133.5 350.5` | `gym_leader.grass_gym.erika` | `128` | `132` | `4` | `3` | `3.57` |
| `water_gym` | `cobblebuilds:water_gym` at `30 127 -23` | `46.5 128.5 -3.5` | `gym_leader.water_gym.misty` | `127` | `127` | `0` | `0` | `0.00` |
| `electric_gym` | `cobblebuilds:electric_gym` at `-22 136 83` | `-5.5 137.5 102.5` | `gym_leader.electric_gym.ltsurge` | `132` | `136` | `4` | `2` | `1.99` |
| `fire_gym` | `cobblebuilds:fire_gym` at `-30 137 -63` | `-13.5 138.5 -43.5` | `gym_leader.fire_gym.blaine` | `131` | `137` | `6` | `2` | `2.72` |
| `poison_gym` | `cobblebuilds:poison_gym` at `-18 128 347` | `-1.5 129.5 366.5` | `gym_leader.poison_gym.koga` | `127` | `128` | `1` | `1` | `1.00` |

배치 로그:

- `Loaded template "cobblebuilds:rock_gym" at -158, 144, -435`
- `Loaded template "cobblebuilds:grass_gym" at 24, 132, 331`
- `Loaded template "cobblebuilds:water_gym" at 30, 127, -23`
- `Loaded template "cobblebuilds:electric_gym" at -22, 136, 83`
- `Loaded template "cobblebuilds:fire_gym" at -30, 137, -63`
- `Loaded template "cobblebuilds:poison_gym" at -18, 128, 347`

콘솔 검증:

- 기존 허공 바위 gym 좌표 확인:
  - `VERIFY_OLD_ROCK_Y174_CLEAR`
  - `VERIFY_OLD_ROCK_Y175_CLEAR`
- 6개 gym의 origin/corner/center 하단 solid 확인:
  - `VERIFY_GROUND_SUPPORT_rock_origin`, `VERIFY_GROUND_SUPPORT_rock_corner`, `VERIFY_GROUND_SUPPORT_rock_center`
  - `VERIFY_GROUND_SUPPORT_grass_origin`, `VERIFY_GROUND_SUPPORT_grass_corner`, `VERIFY_GROUND_SUPPORT_grass_center`
  - `VERIFY_GROUND_SUPPORT_water_origin`, `VERIFY_GROUND_SUPPORT_water_corner`, `VERIFY_GROUND_SUPPORT_water_center`
  - `VERIFY_GROUND_SUPPORT_electric_origin`, `VERIFY_GROUND_SUPPORT_electric_corner`, `VERIFY_GROUND_SUPPORT_electric_center`
  - `VERIFY_GROUND_SUPPORT_fire_origin`, `VERIFY_GROUND_SUPPORT_fire_corner`, `VERIFY_GROUND_SUPPORT_fire_center`
  - `VERIFY_GROUND_SUPPORT_poison_origin`, `VERIFY_GROUND_SUPPORT_poison_corner`, `VERIFY_GROUND_SUPPORT_poison_center`
- 6개 gym marker와 6개 NPC spawner marker 확인:
  - `VERIFY_GYM_MARKER_*`
  - `VERIFY_NPC_SPAWNER_*`
- `save-all flush` 저장 확인
- `forceload query` 결과: `No force loaded chunks were found in minecraft:overworld`

주의:

- 이번 검증은 콘솔과 region heightmap 기준이다.
- 인게임 육안으로 입구 방향, 주변 지형의 자연스러움, 받침 노출 정도는 추가 확인이 필요하다.

## 2026-06-03 strict 10-block gym reset

목적:

- 월드에 생성된 기존 gym 구조물, gym marker, gym leader spawner marker를 모두 제거한다.
- `33 x 39` 구조물 footprint 기준으로 북서/북동/남서/남동 모서리와 중앙 5개 지점을 검사한다.
- 각 검사 지점에서 구조물 배치 Y 아래 10칸 중 공기칸이 2칸 이하인 위치만 사용한다.
- 문서에 확정 좌표를 먼저 기록한 뒤, 이 문서 기준으로 구조물과 marker/spawner를 다시 생성한다.

사전 백업:

- 실행 중 저장 후 백업: `backups/world-before-gym-full-reset-20260603-220037.tar.gz`
- 해시 파일: `backups/world-before-gym-full-reset-20260603-220037.tar.gz.sha256`
- 검증 결과: `sha256sum -c` OK

제거 방식:

- 기존 6개 건물형 gym의 현재/이전 배치 범위를 `fill ... air`로 제거했다.
- 단일 `fill` 한도 32768블록을 넘는 범위는 Y 구간을 나눠 다시 제거했다.
- 8개 gym marker와 8개 NPC spawner marker를 `gym` data 기준으로 제거했다.
- 강철 관장 마을의 기존 beacon 표식도 제거했다.
- 제거 후 `save-all flush`를 실행했고, `forceload query` 결과 `No force loaded chunks were found in minecraft:overworld`를 확인했다.

배치 기준:

- 구조물 템플릿 실제 크기는 `33 x 22 x 39`다.
- heightmap 값은 Minecraft 1.21 월드 최저 Y 오프셋을 반영해 `raw - 64`로 보정해서 사용한다.
- 배치 Y는 5개 검사 지점의 최저 지형 높이보다 2칸 위로 잡는다. 이 기준이면 가장 낮은 검사 지점도 아래 10칸 중 공기칸이 최대 2칸이다.
- 유체 위 후보는 제외하고, `fluid_samples=0`인 후보를 우선한다.

확정 배치 좌표:

| Gym ID | Structure | Marker XYZ | NPC ID | height span | burial max | 10칸 아래 공기칸 |
| --- | --- | --- | --- | --- | --- | --- |
| `rock_gym` | `cobblebuilds:rock_gym` at `-240 70 -572` | `-223.5 71.5 -552.5` | `gym_leader.rock_gym.brock` | `2` | `0` | NW `2`, NE `0`, SW `2`, SE `0`, Center `0` |
| `grass_gym` | `cobblebuilds:grass_gym` at `-233 68 382` | `-216.5 69.5 401.5` | `gym_leader.grass_gym.erika` | `2` | `0` | NW `1`, NE `2`, SW `0`, SE `0`, Center `0` |
| `water_gym` | `cobblebuilds:water_gym` at `-46 69 31` | `-29.5 70.5 50.5` | `gym_leader.water_gym.misty` | `1` | `0` | NW `0`, NE `1`, SW `1`, SE `2`, Center `1` |
| `electric_gym` | `cobblebuilds:electric_gym` at `-17 66 286` | `-0.5 67.5 305.5` | `gym_leader.electric_gym.ltsurge` | `0` | `0` | NW `2`, NE `2`, SW `2`, SE `1`, Center `1` |
| `fire_gym` | `cobblebuilds:fire_gym` at `-61 67 -271` | `-44.5 68.5 -251.5` | `gym_leader.fire_gym.blaine` | `0` | `0` | NW `2`, NE `2`, SW `1`, SE `2`, Center `2` |
| `poison_gym` | `cobblebuilds:poison_gym` at `41 71 390` | `57.5 72.5 409.5` | `gym_leader.poison_gym.koga` | `0` | `0` | NW `1`, NE `1`, SW `2`, SE `2`, Center `2` |
| `ice_gym` | 없음 | `216.5 74.5 -376.5` | `gym_leader.ice_gym.pryce` | marker-only | marker-only | 단일 지점 아래 10칸 중 공기칸 `1` |
| `steel_gym` | 없음 | `344.5 72.5 360.5` | `gym_leader.steel_gym.jasmine` | marker-only | marker-only | 단일 지점 아래 10칸 중 공기칸 `1` |

강철 관장 표식:

- `steel_gym` 위치에는 작은 beacon 표식을 둔다.
- 표식은 `343 70 359`부터 `345 70 361`까지 `iron_block` 3x3 바닥을 두고, `344 71 360`에 `beacon`을 놓는다.
- 이 표식은 위치 안내용이며, 서버 핵심 기능으로 보지 않는다.

강철 일반 트레이너 추가:

- 배경: `steel_gym`은 CobbleBuilds 건물 구조물이 없어 기존 배치가 `gym marker + gym_leader` 스포너 1개뿐이었다. 건물형 6개 체육관은 구조물 안에 일반 트레이너 스포너가 포함되지만, 강철 수동 거점에는 자동으로 생성되지 않는다.
- 변경 전 백업: `backups/world-before-steel-trainers-20260604-070355.tar.gz`
- 배치 방식: CobbleBuilds 내장 `cobblebuilds:npc_spawner/create/gym_trainer` 사용. 추가 블록 공사 없이 기존 강철 신호기 철 블록 발판 위에 marker만 추가했다.

| 역할 | NPC ID | Spawner XYZ | 발판 |
| --- | --- | --- | --- |
| 일반 트레이너 | `gym_trainer.steel_gym.youngster` | `343.5 71.5 359.5` | `343 70 359` |
| 일반 트레이너 | `gym_trainer.steel_gym.camper` | `344.5 71.5 359.5` | `344 70 359` |
| 일반 트레이너 | `gym_trainer.steel_gym.acetrainer` | `345.5 71.5 359.5` | `345 70 359` |

검증:

- 각 후보 지점에서 발 위치와 머리 공간이 `minecraft:air`이고, 바로 아래 블록이 공기가 아님을 콘솔 조건으로 확인했다.
- 추가 후 세 marker 모두 `data.type = "gym_trainer"`, `data.gym = "steel_gym"`, `base.condition = "if function cobblebuilds:condition/npc_spawner/gym_trainer"`로 저장된 것을 확인했다.
- 작업 시점에는 접속자가 없어 실제 `cobblebuilds-gym_trainer` NPC 엔티티 생성은 다음 접속 시 확인해야 한다.

배치 후 검증:

- 6개 구조물 `place template` 로그 확인:
  - `Loaded template "cobblebuilds:rock_gym" at -240, 70, -572`
  - `Loaded template "cobblebuilds:grass_gym" at -233, 68, 382`
  - `Loaded template "cobblebuilds:water_gym" at -46, 69, 31`
  - `Loaded template "cobblebuilds:electric_gym" at -17, 66, 286`
  - `Loaded template "cobblebuilds:fire_gym" at -61, 67, -271`
  - `Loaded template "cobblebuilds:poison_gym" at 41, 71, 390`
- 저장된 region 파일을 재다운로드해 6개 구조물의 5개 지점 아래 10칸 공기칸을 재계산했고, 모두 `2` 이하로 통과했다.
- `ice_gym`, `steel_gym` marker-only 지점도 단일 기준 아래 10칸 중 공기칸 `1`로 통과했다.
- marker 청크를 force-load한 뒤 8개 gym marker와 8개 NPC spawner marker를 콘솔 selector로 확인했다.
- 강철 관장 표식 `344 71 360`의 `minecraft:beacon` 확인.
- `forceload query` 결과: `No force loaded chunks were found in minecraft:overworld`

최종 백업:

- 백업: `backups/world-after-gym-strict-reset-20260603-222230.tar.gz`
- 해시 파일: `backups/world-after-gym-strict-reset-20260603-222230.tar.gz.sha256`
- 검증 결과: `sha256sum -c` OK

남은 확인:

- 콘솔과 region 기준으로는 조건을 통과했다.
- 실제 입구 방향, 주변 지형의 자연스러움, 관장 NPC 본체 생성은 클라이언트 접속 후 육안 확인이 필요하다.
