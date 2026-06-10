# Mods And Client

마지막 갱신: 2026-06-10

이 문서는 `icecoke-cobblemon` 서버 라인과 로컬 Modrinth 클라이언트의 모드/접속 상태를 정리한다.

## 현재 접속 기준

현재 플레이 기준은 `icecoke-cobblemon-173`이다. `icecoke-cobblemon-161`은 기존 1.6.1 서버를 보존하는 레거시 라인이다.

| 항목 | 173 현재 라인 | 161 레거시 라인 |
| --- | --- | --- |
| 서버 주소 | `192.168.219.110:25566` | `192.168.219.110:25565` |
| 서버 MOTD | `icecoke-cobblemon-173` | `icecoke-cobblemon-161` |
| 서버 경로 | `/home/icenux/minecraft/icecoke-cobblemon-173-test` | `/home/icenux/minecraft/mingle-lounge` |
| 로컬 프로필 | `icecoke-cobblemon-173` | `icecoke-cobblemon` |
| 로컬 프로필 경로 | `/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon-173` | `/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon` |
| Minecraft | `1.21.1` | `1.21.1` |
| Fabric Loader | 서버 `0.17.3`, 로컬 `0.18.4` | `0.16.14` |
| Cobblemon | `1.7.3` | `1.6.1` |
| 서버 모드 수 | 58개 | 90개 |

173 라인의 실제 서버 경로에는 과거 테스트 이름인 `icecoke-cobblemon-173-test`가 남아 있다. 파일 이동은 하지 않고, 표시명과 Modrinth 프로필명은 `icecoke-cobblemon-173`으로 통일한다.

## 173 현재 라인 모드 상태

| 영역 | 상태 |
| --- | --- |
| Cobblemon | `Cobblemon-fabric-1.7.3+1.21.1.jar` |
| 필수 접속 | 서버 58개 모드 기준, 로컬 173 프로필에 필수/의존 모드 반영 |
| 아이템 검색 | 로컬 173 프로필에 JEI 적용 |
| 지도 | 로컬 173 프로필에 Xaero 계열 적용 |
| 희귀 스폰 알림 | 1.7.3용 Cobblemon Spawn Alerts 사용 |
| 탈것/이동 | Immersive Aircraft, Gliders, Gotta Ride 'Em All 적용 |
| 베리/구조물 | Berry Pouch, Cobblemon Extra Structures 적용 |
| 레벨캡 | RCTMod `initialLevelCap = 100` |
| 자연 트레이너 | RCTMod `maxLevelDiff = 5`, `forceBattleMaxLevelDiff = 16` |
| 확인 필요 | 관장 marker/NPC/배지, 신규 청크 구조물 생성, 173 라인 Daily/Hermes 이관 |

173 상세 기록은 [COBBLEMON_173_LINE.md](COBBLEMON_173_LINE.md), 로컬 프로필 조건은 [COBBLEMON_173_LOCAL_PROFILE.md](COBBLEMON_173_LOCAL_PROFILE.md), 161 대비 모드 차이는 [COBBLEMON_173_MOD_GAP.md](COBBLEMON_173_MOD_GAP.md)를 기준으로 본다.

## 161 레거시 서버 모드 상태

| 항목 | 값 |
| --- | --- |
| 활성 서버 모드 | 90개 |
| 비활성 서버 모드 | `ItemPhysic_FABRIC_v1.8.7_mc1.21.1.jar` |
| 제외한 서버 모드 | `DistantHorizons-2.2.1-a-1.21.1-neo-fabric.jar`, `voicechat-fabric-1.21.1-2.5.30.jar`, `ItemPhysic_FABRIC_v1.8.7_mc1.21.1.jar` |
| 관장 관련 | `cobblebuilds-leaders`, `easy_npc`, `badgebox` 있음 |
| 백팩 관련 | `sophisticatedbackpacks`, `sophisticatedcore` 있음 |
| 스폰 알림 | `cobblemon_spawn_alerts-fabric-1.6.1.jar` 설치 및 서버 로드 확인 |
| 데일리 보상 | 새 모드 없이 `tools/mc_daily_reward_bridge.py` bridge 프로세스로 처리 |
| RCTMod 레벨캡 | `config/rctmod-server.toml`의 `initialLevelCap=100` 기준. CobbleBuilds 관장 배지와 RCTMod 시리즈 진행은 자동 연동되지 않으므로 RCTMod 15레벨 캡은 사용하지 않음 |

## 161 레거시 클라이언트 상태

| 항목 | 값 |
| --- | --- |
| 런처 | Modrinth App |
| 프로필 | `icecoke-cobblemon` |
| 프로필 경로 | `/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon` |
| Minecraft | `1.21.1` |
| Fabric Loader | `0.16.14` |
| 활성 클라이언트 모드 | 103개 |
| 서버 목록 | `icecoke-cobblemon-161` -> `192.168.219.110:25565` |
| 활성 리소스팩 | `fabric`, `file/CCC_MAL_1.5.4.zip`, `file/cobblemon-ko-tooltip-overlay.zip`, `file/icecoke-ko-ui-overlay.zip` |

## 161 레거시 누락 포켓몬 디자인 보강 리소스팩

161 레거시 서버/클라이언트 기준 `Cobblemon 1.6.1`에는 일부 포켓몬의 species/dex/sound 데이터는 있으나, 클라이언트 표시용 모델/텍스처가 없는 경우가 있다. 확인된 예시는 마릴이며, 기본 jar에는 `marill` species와 dex/sound는 있지만 `marill.geo.json` 모델과 `marill.png` 텍스처가 없다.

이를 보완하기 위해 로컬 클라이언트 전용 리소스팩 `CCC_MAL_1.5.4.zip`을 활성화한다.

| 항목 | 값 |
| --- | --- |
| 리소스팩 | `CCC_MAL_1.5.4.zip` |
| 로컬 설치 위치 | `/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon/resourcepacks/CCC_MAL_1.5.4.zip` |
| 활성화 상태 | `options.txt`의 `resourcePacks:["fabric","file/CCC_MAL_1.5.4.zip","file/cobblemon-ko-tooltip-overlay.zip","file/icecoke-ko-ui-overlay.zip"]` |
| 확인 예시 | 마릴 모델/텍스처/poser/animation 포함 |
| 서버 영향 | 클라이언트 표시 리소스 보강 목적. 서버 재시작 불필요 |

리소스팩 순서는 `CCC_MAL_1.5.4.zip`, 한국어 tooltip overlay, 한국어 UI overlay 순서로 둔다. `CCC_MAL_1.5.4.zip`에는 한국어 lang 파일이 없으므로 현재 한국어 보강팩과 충돌하지 않는다.

## 161 레거시 한국어 UI 보강 리소스팩

일부 클라이언트 UI와 알림 문구는 `ko_kr` 번역이 없거나, 내장 한국어 파일이 깨져 영어로 표시될 수 있다. 이를 서버 모드 변경 없이 보완하기 위해 클라이언트 전용 리소스팩 `icecoke-ko-ui-overlay.zip`을 사용한다.

| 항목 | 값 |
| --- | --- |
| 저장소 산출물 | `resourcepacks/icecoke-ko-ui-overlay.zip` |
| 로컬 설치 위치 | `/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon/resourcepacks/icecoke-ko-ui-overlay.zip` |
| 활성화 상태 | `options.txt`의 `resourcePacks:["fabric","file/CCC_MAL_1.5.4.zip","file/cobblemon-ko-tooltip-overlay.zip","file/icecoke-ko-ui-overlay.zip"]` |
| 생성 스크립트 | `tools/generate_icecoke_ko_ui_overlay.py` |
| 서버 영향 | 클라이언트 표시 문자열만 변경. 서버 재시작 불필요 |

현재 포함 범위는 아래와 같다.

| 구분 | 처리 |
| --- | --- |
| Cobblemon | `1.6.1` 한국어에서 빠진 키 중 `1.7.3` 한국어에 있는 1255개 키를 재사용 |
| Cobblemon Spawn Alerts | 희귀 포켓몬 스폰/디스폰 알림 45개 키 수동 한글화 |
| Xaero Minimap | 내장 `ko_kr.json`의 깨진 escape를 보정해 566개 키 활성화 |
| Xaero World Map | 지도 선택, 설정, 웨이포인트, 조작 안내 등 주요 UI 75개 키 수동 한글화 |

이 리소스팩은 다른 한글 보강팩보다 뒤에 둔다. 같은 번역 키가 있을 경우 `icecoke-ko-ui-overlay.zip`의 값이 우선 적용된다.

## 161 레거시 한국어 아이템 설명 보강 리소스팩

161 레거시 서버/클라이언트는 샘플팩 기준 `Cobblemon 1.6.1`을 사용한다. `Cobblemon 1.6.1`의 한국어 `ko_kr` 아이템 tooltip은 영어 원문보다 적어, 인벤토리에서 Shift 설명이 짧거나 빠진 아이템이 있다.

이를 서버 모드 업그레이드 없이 보완하기 위해 클라이언트 전용 리소스팩 `cobblemon-ko-tooltip-overlay.zip`을 사용한다.

| 항목 | 값 |
| --- | --- |
| 저장소 산출물 | `resourcepacks/cobblemon-ko-tooltip-overlay.zip` |
| 로컬 설치 위치 | `/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon/resourcepacks/cobblemon-ko-tooltip-overlay.zip` |
| 활성화 상태 | `options.txt`의 `resourcePacks:["fabric","file/CCC_MAL_1.5.4.zip","file/cobblemon-ko-tooltip-overlay.zip","file/icecoke-ko-ui-overlay.zip"]` |
| 언어 조건 | `lang:ko_kr` |
| 생성 스크립트 | `tools/generate_cobblemon_ko_tooltip_overlay.py` |
| 소스 번역 | 로컬 `Cobblemon-fabric-1.7.3+1.21.1.jar`의 `assets/cobblemon/lang/ko_kr.json` |
| 대상 범위 | `Cobblemon 1.6.1`에서 실제 사용 가능한 `item.cobblemon.*tooltip*` 키 |

추출 결과는 아래와 같다.

| 구분 | 개수 |
| --- | ---: |
| overlay 아이템 tooltip 키 | 405 |
| 1.6.1 한국어에 없어서 새로 채운 키 | 288 |
| 1.6.1 한국어가 있었지만 1.7.3의 더 자세한 문구로 교체한 키 | 84 |
| 기존과 동일한 키 | 33 |

이 리소스팩은 클라이언트 표시 텍스트만 바꾸며, 서버 접속 조건이나 게임 데이터에는 영향을 주지 않는다. 서버에는 설치하지 않는다.

## 선택 지도 모드

지도 모드는 로컬 클라이언트 전용 편의 기능으로 사용한다. 서버 `mods/`에는 추가하지 않는다.

```text
xaerominimap-fabric-1.21.1-25.3.12.jar
xaeroworldmap-fabric-1.21.1-1.40.16.jar
```

기본 사용 키는 개인 키 설정에 따라 달라질 수 있으나, 기존 가이드 기준 전체 지도는 `,`, 미니맵 설정은 `Y`, 확대 지도는 `Z`다.

### 지도 표시 설정

로컬 Modrinth 프로필의 Xaero HUD 설정에서 미니맵을 우측 중앙 기준으로 옮겼다.

```text
config/xaerohud.txt
module;id=xaerominimap:minimap;x=-16;y=110;centered=false;fromRight=true;fromBottom=false;flippedVer=false;flippedHor=false;
```

`config/xaero/minimap/default_radar_categories_client.json`에는 `cobblemon:pokemon` 전용 radar 카테고리를 추가했고, 해당 카테고리만 이름 표시를 켰다. 일반 엔티티 전체 이름 표시는 켜지 않는다.

## 희귀 포켓몬 스폰 알림

173 현재 라인은 `Cobblemon 1.7.3`에 맞춰 `cobblemon_spawn_alerts-fabric-1.13.2.jar`를 사용한다. 161 레거시 라인은 `Cobblemon 1.6.1`에 맞춰 `cobblemon_spawn_alerts-fabric-1.6.1.jar`를 유지한다.

| 위치 | 상태 |
| --- | --- |
| 173 서버 | `mods/cobblemon_spawn_alerts-fabric-1.13.2.jar` 설치 및 로드 |
| 173 서버 설정 | `config/cobblemon-spawn-alerts/server.json`, `configVersion = 1.13.2` |
| 161 서버/로컬 기록 | `cobblemon_spawn_alerts-fabric-1.6.1.jar` 사용 |
| 알림 기준 | 이로치, 전설, 환상, 울트라비스트, 패러독스 알림 켬. `ULTRA_RARE` bucket 알림 켬 |

현재 173 서버 설정값은 아래와 같다.

```json
{
  "configVersion": "1.13.2",
  "alertShinies": true,
  "broadcastShiny": true,
  "alertLegendaries": true,
  "alertMythicals": true,
  "alertUltraBeasts": true,
  "alertParadox": true,
  "alertStarters": false,
  "alertHiddenAbility": false,
  "bucketsToAlert": ["ULTRA_RARE"],
  "broadcastBucket": true,
  "broadcastIVs": true,
  "broadcastEVs": true,
  "broadcastNature": true,
  "broadcastAbility": true,
  "sendWebhook": false
}
```

현재 로컬 클라이언트 설정값은 아래와 같다.

```json
{
  "configVersion": "1.13.2",
  "enableAlerts": true,
  "enableDespawnAlerts": true,
  "enableSounds": true,
  "alertAllShinies": true,
  "alertAllHA": true,
  "alertAllLegendaries": true,
  "alertAllMythicals": true,
  "alertAllUltraBeasts": true,
  "alertAllParadox": true,
  "alertAllStarter": false,
  "bucketsToAlert": ["ULTRA_RARE"],
  "alertAllNotInDex": false,
  "alertAllUncaught": false,
  "alertEverything": false
}
```

## 제거한 클라이언트 모드

개인 플레이 기준에서 필요 없는 방송/녹화/보이스챗/선택 연출 모드는 제거했다.

```text
DistantHorizons-2.2.1-a-1.21.1-neo-fabric.jar
hdskins-6.14.3+1.21.1.jar
iris-fabric-1.8.8+mc1.21.1.jar
replaymod-1.21-2.6.19.jar
sound-physics-remastered-fabric-1.21.1-1.4.12.jar
voicechat-fabric-1.21.1-2.5.30.jar
ItemPhysic_FABRIC_v1.8.7_mc1.21.1.jar
```

현재 클라이언트 `mods/`에는 `.jar.disabled` 파일을 남기지 않는다. `ItemPhysic_FABRIC_v1.8.7_mc1.21.1.jar`는 되돌릴 수 있도록 로컬 프로필의 `disabled-client-mods/`에 보관한다.

## ItemPhysic 제거 기록

`ItemPhysic_FABRIC_v1.8.7_mc1.21.1.jar`는 드롭 아이템을 바닐라 아이템 엔티티가 아니라 물리 오브젝트처럼 눕고 굴러가게 만드는 모드다. 개인 서버 기준 필수 플레이 기능이 아니며, 드롭 아이템 처리와 클라이언트 렌더링을 추가로 건드리므로 성능/안정성 우선 원칙에 따라 비활성화했다.

| 위치 | 상태 |
| --- | --- |
| 서버 | `mods/`에서 제거, `disabled-mods/`에 보관 |
| 로컬 클라이언트 | `mods/`에서 제거, `disabled-client-mods/`에 보관 |
| 적용 시점 | 서버 재시작 후 비활성화 확인, 클라이언트는 다음 실행부터 |

## 접속 조건

- 서버와 클라이언트는 같은 샘플팩 계열을 기준으로 맞춘다.
- 서버가 요구하는 주요 모드가 클라이언트에서 빠지면 접속 실패할 수 있다.
- 서버 모드 변경이 있으면 클라이언트 프로필도 함께 판단한다.
- 클라이언트만 필요한 편의/렌더링 모드는 서버 접속 검증 후 별도 선택으로 둔다.
- Xaero 지도 모드는 선택 클라이언트 모드이므로 없어도 서버 접속 자체에는 영향을 주지 않는다.
- `Cobblemon Spawn Alerts`는 서버와 클라이언트 모두에 설치했으므로, 서버 재시작 후 클라이언트도 같은 버전으로 실행한다.

## RCTMod 레벨/트레이너 운영

173 현재 서버에는 `rctapi-fabric-1.21.1-0.15.2-beta.jar`와 `rctmod-fabric-1.21.1-0.18.1-beta.jar`가 설치되어 있다. RCTMod는 자연 스폰 일반 트레이너 1559개를 등록하며, 트레이너 후보 레벨 판단은 배지 수가 아니라 플레이어 파티의 가장 높은 레벨 포켓몬을 기준으로 한다.

현재 `config/rctmod-server.toml`의 주요 값은 아래와 같다.

```toml
globalSpawnChance = 0.85
maxTrainersPerPlayer = 12
maxLevelDiff = 5
forceBattleMaxLevelDiff = 16
initialLevelCap = 100
relativeLevelCap = 0
allowOverLeveling = false
```

운영 기준:

- RCTMod 기본 초기 레벨캡 15는 사용하지 않는다. 개인 서버 기준에서는 `initialLevelCap = 100`으로 둔다.
- CobbleBuilds 관장/체육관 일반 트레이너 진행은 `mingle-gym-party-overrides` 데이터팩과 배지 수가 맡는다.
- CobbleBuilds의 `gym_badge_count`와 RCTMod의 `currentSeries`/레벨캡 진행은 자동으로 연결되지 않는다.
- RCTMod 자연 스폰 트레이너는 배지 수가 아니라 파티 최고 레벨 기준이다. 과한 고레벨 스폰을 줄이기 위해 `maxLevelDiff = 5`로 낮췄다.
- RCTMod 설정은 서버 시작 시 읽히므로 `initialLevelCap`, `maxLevelDiff`, `forceBattleMaxLevelDiff` 변경 후에는 서버 재시작이 필요하다.
- 파티 평균 레벨 기준으로 바꾸는 설정은 확인되지 않았다. 필요하면 별도 모드/믹스인/포크 설계가 필요하다.

## 관장 관련 모드

| 모드 | 역할 |
| --- | --- |
| `cobblebuilds-leaders` | 관장/체육관 일반 트레이너 리소스 |
| `easy_npc` | NPC 기반 |
| `badgebox` | 배지 아이템/보관 |
| `rctmod`/`rctapi` | 자연 스폰 일반 트레이너와 관련 API |

현재 관장 리소스는 있고, 월드에는 8개 gym marker와 8개 gym leader spawner marker가 배치되어 있다. 6개 기본 gym 건물도 배치했으며, `ice_gym`, `steel_gym`은 건물 없이 수동 거점/marker 방식이다. 관장과 체육관 일반 트레이너 파티는 `mingle-gym-party-overrides` 데이터팩으로 173 경로에 맞춰 override한다. 실제 `cobblemon:npc` 본체 생성, 전투, 배지/보상은 플레이어 근접 인게임 확인이 필요하다.

## 데일리 보상

데일리 보상은 서버/클라이언트 모드가 아니라 별도 Python bridge로 처리한다.

| 항목 | 값 |
| --- | --- |
| 스크립트 | `tools/mc_daily_reward_bridge.py` |
| 서버 세션 | `mc-daily-reward` |
| 기점 | 플레이어 접속 로그 |
| 기준 | `Asia/Seoul` 날짜 기준 하루 1회 |
| 클라이언트 영향 | 없음 |
