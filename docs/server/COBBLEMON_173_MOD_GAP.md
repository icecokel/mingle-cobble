# Cobblemon 173 Mod Gap

마지막 갱신: 2026-06-10

이 문서는 161 레거시 라인 `icecoke-cobblemon-161`의 `mods/`와 현재 173 라인 `icecoke-cobblemon-173`의 `mods/`를 비교해, 173 라인으로 전환된 모드와 보류된 모드를 정리한다.

## 현재 읽는 기준

2026-06-10 기준 현재 플레이 라인은 `icecoke-cobblemon-173`이다. 아래 표는 161 레거시 모드가 173 라인에 같은 파일로 남았는지, 1.7.3 대응 파일로 대체됐는지, 보류됐는지를 구분한다. 상세 검증 이력은 각 섹션의 "적용 완료", "보류", "제외" 기록을 우선한다.

| 구분 | 상태 |
| --- | --- |
| 현재 플레이 라인 | `icecoke-cobblemon-173`, `192.168.219.110:25566`, 서버 경로 `/home/icenux/minecraft/icecoke-cobblemon-173-test` |
| 레거시 라인 | `icecoke-cobblemon-161`, `192.168.219.110:25565`, 서버 경로 `/home/icenux/minecraft/mingle-lounge` |
| 173 서버 모드 수 | 58개 |
| 173에 적용 완료 | 관장/배지/RCT, 탈것, Fight or Flight, JEI 로컬, Berry Pouch, Cobblemon Extra Structures, 일부 성능 모드 |
| 계속 보류 | Sophisticated Backpacks, CobbleDollars, Cobblemon Smartphone, 사진/음향/편의 계열, WorldEdit/Chunky, Lithium/ServerCore |

## 비교 기준

| 항목 | 경로 | 모드 수 |
| --- | --- | --- |
| 161 레거시 | `/home/icenux/minecraft/mingle-lounge/mods` | 90 |
| 173 라인 | `/home/icenux/minecraft/icecoke-cobblemon-173-test/mods` | 58 |

판정 기준:

- 파일명이 완전히 같은 모드는 이미 넘어온 것으로 본다.
- Cobblemon, Fabric API처럼 1.7.3용 파일로 교체된 모드는 "대체 전환됨"으로 분류한다.
- 아래 "미전환" 목록은 현재 173 라인에 같은 파일이나 명확한 대체 파일이 없는 161 레거시 모드다.
- 미전환은 "불가능"을 뜻하지 않는다. 현재 173 라인 범위에서 아직 검증/추가하지 않았다는 뜻이다.

## 이미 대체 전환된 모드

| 161 레거시 1.6.1 계열 | 173 라인 계열 |
| --- | --- |
| `Cobblemon-fabric-1.6.1+1.21.1.jar` | `Cobblemon-fabric-1.7.3+1.21.1.jar` |
| `Cobblemon_MegaShowdown-9.7.6-release-fabric.jar` | `mega_showdown-fabric-1.8.4+1.7.3+1.21.1.jar` |
| `MythsAndLegends-fabric-1.7.2.jar` | `MythsAndLegends-fabric-1.9.0.jar` |
| `accessories-fabric-1.1.0-beta.43+1.21.1.jar` | `accessories-fabric-1.1.0-beta.53+1.21.1.jar` |
| `fabric-api-0.116.4+1.21.1.jar` | `fabric-api-0.116.12+1.21.1.jar` |
| `fabric-language-kotlin-1.13.3+kotlin.2.1.21.jar` | `fabric-language-kotlin-1.13.11+kotlin.2.3.21.jar` |
| `owo-lib-0.12.15.4+1.21.jar` | `owo-lib-0.13.0-alpha.15+1.21.jar` |
| `cobblemon_spawn_alerts-fabric-1.6.1.jar` | `cobblemon_spawn_alerts-fabric-1.13.2.jar` |

## 초기 미전환 요약

초기 비교 당시 명확히 미전환인 161 레거시 모드는 67개였다. 2026-06-07 21:16 KST 기준으로 핵심 gameplay, 관장, 진행, 음식, 이동, 1차 성능, 베리 보관, 추가 구조물 계열을 일부 적용한 뒤 173 라인 모드 수는 58개이며, 161 레거시 모드 ID 기준 미반영 항목은 49개다.

| 분류 | 개수 | 대표 영향 |
| --- | ---: | --- |
| Cobblemon 애드온/서버 시스템 | 25 | 관장, 배지 보관, 레벨캡, 경제, 추가 아이템, 포켓몬 부가 콘텐츠 |
| 월드/생활/탈것 콘텐츠 | 14 | 요리, 농사, 비행선, 글라이더, 가방, 상호작용 |
| 편의/성능/운영 | 15 | JEI 검색, 줌, 최적화, 서버 관리, 표시 편의 |
| 의존성/라이브러리 | 11 | 위 모드들의 필수 의존성 |

## Cobblemon 애드온/서버 시스템

| 모드 | 현재 판단 |
| --- | --- |
| `CobbleCuisine-1.2.1.jar` | 대체 적용. 173 라인에는 `cobblecuisine-2.0.1-1.7-rc1.jar` 적용 |
| `CobbleDollars-fabric-2.0.0+Beta-5.1+1.21.1.jar` | 미전환. 돈/경제 계열 |
| `CobblemonRepel-1.6-1.2.jar` | 대체 적용. 173 라인에는 `CobblemonRepel-1.7-1.4.jar` 적용 |
| `Cobblemon_Legends_Reborn-3.0.0-fabric.jar` | 미전환. 전설/확장 콘텐츠 계열 |
| `Cobbreeding-fabric-1.9.0.jar` | 대체 적용. 173 라인에는 `Cobbreeding-fabric-2.2.1.jar` 적용 |
| `SafePastures-1.1.0+1.21.1.jar` | 미전환. 목장/보관 안정성 계열로 보임 |
| `SimpleTMs-fabric-2.1.2.jar` | 대체 적용. 173 라인에는 `SimpleTMs-fabric-2.3.3.jar` 적용 |
| `badgebox-fabric-1.3.0.jar` | 적용. 173 라인에도 같은 버전 적용 |
| `berrypouch-fabric-1.21.1-0.4.2-beta.jar` | 대체 적용. 173 라인에는 `berrypouch-fabric-1.21.1-0.5.4-beta.jar` 적용 및 접속 검증 완료 |
| `cobblebuilds-leaders-1.0.0-beta.4.jar` | 대체 적용. 173 라인에는 `cobblebuilds-leaders-0.1.1-hf.1.jar` 적용 |
| `cobbledelight-0.1.jar` | 대체 적용. 173 라인에는 `cobblecuisine-delight-1.1.jar` 적용 |
| `cobblemon-armors-1.5.1+1.6.1.jar` | 대체 적용. 173 라인에는 `cobblemon-armors-1.6.0+1.7.3.jar` 적용 |
| `cobblemon-droploottables-1.6-fabric-1.4.1.jar` | 대체 적용. 173 라인에는 `droploottables-fabric-1.7.3-1.9.1.jar` 적용 |
| `cobblemon-progress-items-4.0.0.jar` | 미전환. 진행도/아이템 게이트 계열 |
| `cobblemon-shearems-1.6-fabric-1.1.2.jar` | 미전환. 파일명 기준 1.6 계열이라 1.7.3 호환 확인 필요 |
| `cobblemon-unimplementeditems-1.6-fabric-1.1.0.jar` | 미전환. metadata 기준 `cobblemon <=1.7.0`이라 1.7.3에는 제외한 상태 |
| `cobblemon-whiteout-1.6-fabric-1.1.1.jar` | 미전환. 파일명 기준 1.6 계열이라 1.7.3 호환 확인 필요 |
| `cobblemon_smartphone-fabric-1.0.3.jar` | 미전환. 스마트폰 UI/기능 계열 |
| `cobblemonextrastructures-1.21.1-1.1.0-fabric.jar` | 대체 적용. 173 라인에는 `cobblemonextrastructures-1.21.1-1.3.0-fabric.jar` 적용 및 접속 검증 완료. 단 `sprout_tower` advancement 경고와 신규 청크 구조물 확인은 남음 |
| `eggs-cobblemon-addon-0.7.jar` | 미전환. 알 관련 Cobblemon 애드온 |
| `fightorflight-fabric-0.8.1.jar` | 대체 적용. 173 라인에는 `fightorflight-fabric-0.10.7.jar` 적용 |
| `more-cobblemon-move-anims-1.3.af.jar` | 대체 적용. 173 라인에는 `extra-move-anims-cobblemon-1.7v1.0.2.jar` 적용 |
| `poke-clothing-1.0+1.21.1-fabric.jar` | 미전환. 의상 계열 |
| `pokeblocks-1.4.0-1.21.1.jar` | 미전환. 포켓블록 계열 |
| `rctapi-fabric-1.21.1-0.13.4-beta.jar` | 대체 적용. 173 라인에는 `rctapi-fabric-1.21.1-0.15.2-beta.jar` 적용 |
| `rctmod-fabric-1.21.1-0.16.1-beta.jar` | 대체 적용. 173 라인에는 `rctmod-fabric-1.21.1-0.18.1-beta.jar` 적용. 현재 설정은 `initialLevelCap = 100`, `maxLevelDiff = 5` |
| `rocket_mons-1.0.jar` | 미전환. 추가 Cobblemon 콘텐츠 계열 |

## 월드/생활/탈것 콘텐츠

| 모드 | 현재 판단 |
| --- | --- |
| `FarmersDelight-1.21.1-3.1.0+refabricated.jar` | 대체 적용. 173 라인에는 `FarmersDelight-1.21.1-3.2.8+refabricated.jar` 적용 |
| `amendments-1.21-1.2.24-fabric.jar` | 미전환. 생활/장식 확장 계열 |
| `carryon-fabric-1.21.1-2.2.2.11.jar` | 미전환. 블록/엔티티 운반 편의 |
| `easy_npc-fabric-1.21.1-5.9.0.jar` | 대체 적용. 173 라인에는 `easy_npc_bundle-6.2.0-fabric-1.21.1.jar` 적용 |
| `exposure-fabric-1.21.1-1.9.9.jar` | 미전환. 카메라/사진 계열 |
| `exposure_polaroid-fabric-1.21.1-1.1.2.jar` | 미전환. 사진 확장 계열 |
| `gliders-1.21.1-fabric-1.1.7.jar` | 대체 적용. 173 라인에는 `gliders-1.21.1-fabric-1.1.8.jar` 적용 |
| `hardcorerevival-fabric-1.21.1-21.1.7.jar` | 미전환. 부활/다운 상태 계열 |
| `immersive_aircraft-1.2.4+1.21.1-fabric.jar` | 대체 적용. 173 라인에는 `immersive_aircraft-1.4.6+1.21.1-fabric.jar` 적용 |
| `cobbleride-fabric-0.3.2+1.21.1.jar` | 검증 후 제외. Modrinth 해시 기준 `Cobblemon: Ride On!`이며 1.7.3과 충돌 |
| `sittingplus-2.0.6-1.21.1-FABRIC.jar` | 미전환. 앉기/상호작용 편의 |
| `sophisticatedbackpacks-1.21.1-3.23.4.2.103.jar` | 미전환. 고급 백팩. 1.7.3 테스트에는 별도 `Inmis` 가방만 있음 |
| `sophisticatedcore-1.21.1-1.2.9.14.154.jar` | 미전환. SophisticatedBackpacks 의존성 |
| `sound-physics-remastered-fabric-1.21.1-1.4.12.jar` | 미전환. 사운드 물리 효과 |

## 편의/성능/운영

| 모드 | 현재 판단 |
| --- | --- |
| `Chunky-Fabric-1.4.23.jar` | 미전환. 청크 사전 생성/관리 |
| `Clumps-fabric-1.21.1-19.0.0.1.jar` | 적용. 173 라인에도 같은 버전 적용 |
| `dynamic-light-0.6.jar` | 미전환. 동적 조명 |
| `entity-view-distance-1.3.0+1.21.jar` | 미전환. 엔티티 표시 거리 조정 |
| `entityculling-fabric-1.7.4-mc1.21.jar` | 로컬 대체 적용. 173 로컬 프로필에는 `entityculling-fabric-1.10.2-mc1.21.1.jar` 적용 |
| `farsight-fabric-1.21-4.4.jar` | 미전환. 먼 청크 표시 |
| `ferritecore-7.0.2-hotfix-fabric.jar` | 대체 적용. 173 라인에는 `ferritecore-7.0.3-fabric.jar` 적용 |
| `jei-1.21.1-fabric-19.21.2.313.jar` | 로컬 대체 적용. 173 로컬 프로필에는 `jei-1.21.1-fabric-19.27.0.340.jar` 적용 |
| `justzoom_fabric_2.1.0_MC_1.21.1.jar` | 로컬 적용. 173 로컬 프로필에도 같은 버전 적용 |
| `krypton-0.2.8.jar` | 적용. 173 라인에도 같은 버전 적용 |
| `lithium-fabric-0.15.0+mc1.21.1.jar` | 미전환. 서버/게임 로직 최적화 |
| `netprodis-1.1.0+1.21.2.jar` | 미전환. 네트워크/프로토콜 계열로 보임. 버전 표기가 `1.21.2`라 주의 필요 |
| `servercore-fabric-1.5.5+1.21.1.jar` | 미전환. 서버 성능/운영 설정 |
| `show-held-items-0.2.3.jar` | 미전환. 손에 든 아이템 표시 |
| `worldedit-mod-7.3.8.jar` | 미전환. 월드 편집/관리 |

## 의존성/라이브러리

| 모드 | 현재 판단 |
| --- | --- |
| `CreativeCore_FABRIC_v2.13.5_mc1.21.1.jar` | 미전환. 일부 클라이언트/상호작용 모드 의존성 |
| `ForgeConfigAPIPort-v21.1.3-1.21.1-Fabric.jar` | 미전환. 설정 API 의존성 |
| `Necronomicon-Fabric-1.6.0+1.21.jar` | 미전환. 라이브러리 계열 |
| `YSNS-Fabric_Quilt-MC1.21-1.0.6.jar` | 미전환. 라이브러리/보조 계열 |
| `balm-fabric-1.21.1-21.0.46.jar` | 미전환. 라이브러리 계열 |
| `cupboard-fabric-1.21-2.9.jar` | 미전환. 라이브러리 계열 |
| `konkrete_fabric_1.9.9_MC_1.21.jar` | 미전환. 라이브러리 계열 |
| `midnightlib-1.6.9-fabric+1.21.jar` | 미전환. 설정/라이브러리 계열 |
| `moonlight-1.21-2.18.16-fabric.jar` | 미전환. 라이브러리 계열 |
| `player-animation-lib-fabric-2.0.1+1.21.1.jar` | 미전환. 애니메이션 라이브러리 |
| `supermartijn642configlib-1.1.8-fabric-mc1.21.jar` | 미전환. 설정 라이브러리 |

## 우선 검토 후보

운영 서버와 같은 플레이 감각을 원하면 아래 순서로 1.7.3 호환성을 확인한다.

1. `jei`: 인벤토리 우측 아이템 검색/레시피 UI.
2. 관장/배지 계열: `cobblebuilds-leaders`, `easy_npc`, `badgebox`, `rctmod`, `rctapi`.
3. 이동/탈것 계열: `immersive_aircraft`, `gliders`, `Gotta Ride 'Em All`. `cobbleride`는 1.7.3과 충돌해 제외.
4. 가방/보관 계열: 현재 1.7.3에는 `Inmis`가 있으므로 `sophisticatedbackpacks`가 정말 필요한지 먼저 판단한다.
5. 월드 잔여 참조 계열: `FarmersDelight`, `CobbleCuisine`, `cobbledelight`.
6. 성능 계열: `lithium`, `ferritecore`, `krypton`, `servercore`, `Clumps`.

## 1.7.3 대응 존재성 조사

조사일: 2026-06-07

확인 방법:

- 로컬 161 레거시 클라이언트 jar의 SHA1을 계산해 Modrinth `version_files` API로 프로젝트를 매칭했다.
- 매칭된 프로젝트는 Modrinth `project/{id}/version` API에서 `game_versions=["1.21.1"]`, `loaders=["fabric"]`로 후보 버전을 조회했다.
- Modrinth 해시 매칭이 안 된 파일은 Modrinth 검색과 jar 내부 `fabric.mod.json`을 보조 근거로 확인했다.
- 아래의 "있음"은 바로 운영 반영 가능을 뜻하지 않는다. 173 라인과 로컬 173 프로필에 넣고 기동/접속/기능 검증을 해야 한다.

### Cobblemon 1.7.x 대응 명시 후보

버전명 또는 파일명에 Cobblemon `1.7`, `1.7.1`, `1.7.3` 대응이 명시된 후보다. 우선 검토 가치가 가장 높다.

| 161 레거시 모드 | 확인된 1.7.x 후보 | 판정 |
| --- | --- | --- |
| `CobbleCuisine-1.2.1.jar` | `2.0.1-1.7-rc1`, `2.0.0-rc1` | 1.7 계열 후보 있음. 현재 서버 로그의 `cobblecuisine:*` 잔여 참조 해결 후보 |
| `CobblemonRepel-1.6-1.2.jar` | `1.7-1.4`, `1.7-1.3` | 1.7 계열 후보 있음 |
| `Cobbreeding-fabric-1.9.0.jar` | `2.2.1`, `2.2.0`, `2.1.1`, `2.1.0` with `Cobblemon 1.7` 표시 | 1.7 계열 후보 있음 |
| `SimpleTMs-fabric-2.1.2.jar` | `2.3.3`~`2.3.0` with `Cobblemon 1.7.1`, `2.2.1` with `Cobblemon 1.7+1.7.1` | 1.7 계열 후보 있음 |
| `cobblemon-armors-1.5.1+1.6.1.jar` | `1.6.0+1.7.3`, `1.6.0+1.7.2`, `1.6.0+1.7.1` | 1.7.3 후보 있음 |
| `cobblemon-droploottables-1.6-fabric-1.4.1.jar` | `1.7.3-fabric-1.9.1`, `1.7.3-fabric-1.9.0`, `1.7.3-fabric-1.8.0` | 1.7.3 후보 있음 |
| `more-cobblemon-move-anims-1.3.af.jar` | `1.7v1.0.2`, `1.7v1.0.1`, `1.7v1.0` | 1.7 계열 후보 있음 |

### 1.21.1 Fabric 후보 있음

Minecraft `1.21.1` + Fabric 후보는 확인됐지만, Cobblemon `1.7.3` 대응이 버전명에서 직접 확인되지는 않은 모드다. Cobblemon 비의존 모드는 이 정도면 충분한 후보지만, Cobblemon 애드온은 별도 기능 검증이 필요하다.

| 161 레거시 모드 | 확인된 후보 상태 | 판정 |
| --- | --- | --- |
| `CobbleDollars-fabric-2.0.0+Beta-5.1+1.21.1.jar` | 1.21.1 Fabric 후보 있음 | 경제 기능 후보. 1.7.3 기능 검증 필요 |
| `SafePastures-1.1.0+1.21.1.jar` | `1.1.1+1.21.1` 후보 있음 | 후보 있음 |
| `badgebox-fabric-1.3.0.jar` | 1.21.1 Fabric 후보 있음 | 배지 보관 후보. 관장/배지 검증과 묶어 테스트 |
| `berrypouch-fabric-1.21.1-0.4.2-beta.jar` | `0.5.4` 등 1.21.1 Fabric 후보 있음 | 후보 있음 |
| `cobblebuilds-leaders-1.0.0-beta.4.jar` | Modrinth 검색 기준 1.21.1 후보 있음. 최신명은 `0.1.1-hf.1+mod` 계열 | 관장/NPC 핵심 후보. 최우선 별도 테스트 |
| `cobbledelight-0.1.jar` | 1.21.1 Fabric 후보 있음 | Farmer's Delight/CobbleCuisine와 함께 테스트 |
| `cobblemon-progress-items-4.0.0.jar` | 1.21.1 Fabric 후보 있음 | 진행도 아이템 후보 |
| `cobblemon_smartphone-fabric-1.0.3.jar` | `1.0.9` 등 1.21.1 Fabric 후보 있음 | 후보 있음 |
| `cobblemonextrastructures-1.21.1-1.1.0-fabric.jar` | `1.21.1-1.3.0` 등 후보 있음 | 구조물 추가 후보 |
| `cobbleride-fabric-0.3.2+1.21.1.jar` | `0.3.3` 등 1.21.1 Fabric 후보는 있으나 metadata상 `Cobblemon >=1.7`과 충돌 | 1.7.3 제외 |
| `eggs-cobblemon-addon-0.7.jar` | `0.9+mod` 등 1.21.1 Fabric 후보 있음 | 후보 있음 |
| `fightorflight-fabric-0.8.1.jar` | `0.10.7` 등 1.21.1 Fabric 후보 있음 | 전투/AI 계열 후보. 기능 검증 필요 |
| `poke-clothing-1.0+1.21.1-fabric.jar` | `1.21.1-1.2.2` 등 후보 있음 | 후보 있음 |
| `pokeblocks-1.4.0-1.21.1.jar` | `1.5.0-1.21.1` 등 후보 있음 | 후보 있음 |
| `rctapi-fabric-1.21.1-0.13.4-beta.jar` | `0.15.2-beta` 등 후보 있음 | RCTMod와 함께 테스트 |
| `rctmod-fabric-1.21.1-0.16.1-beta.jar` | `0.18.1-beta` 등 후보 있음 | 레벨캡/진행 설계 후보. 관장/배지와 충돌 주의 |
| `FarmersDelight-1.21.1-3.1.0+refabricated.jar` | `1.21.1-3.3.3` 등 후보 있음 | 서버 로그의 `farmersdelight:*` 잔여 참조 해결 후보 |
| `amendments-1.21-1.2.24-fabric.jar` | `1.21-2.0.15-fabric` 등 후보 있음 | 후보 있음 |
| `carryon-fabric-1.21.1-2.2.2.11.jar` | `2.2.4` 후보 있음 | 후보 있음 |
| `easy_npc-fabric-1.21.1-5.9.0.jar` | `6.17.0` 등 후보 있음 | NPC 후보. 관장 구현과 별도 검증 |
| `exposure-fabric-1.21.1-1.9.9.jar` | `1.9.16` 등 후보 있음 | 사진 기능 후보 |
| `exposure_polaroid-fabric-1.21.1-1.1.2.jar` | `1.1.4` 등 후보 있음 | 사진 확장 후보 |
| `gliders-1.21.1-fabric-1.1.7.jar` | `1.1.8+fabric` 후보 있음 | 글라이더 후보 |
| `hardcorerevival-fabric-1.21.1-21.1.7.jar` | `21.1.14+fabric-1.21.1` 등 후보 있음 | 개인 서버에서는 필요성 재검토 |
| `immersive_aircraft-1.2.4+1.21.1-fabric.jar` | `1.4.6+1.21.1` 등 후보 있음 | 비행선/항공기 후보 |
| `sittingplus-2.0.6-1.21.1-FABRIC.jar` | 1.21.1 Fabric 후보 있음 | 후보 있음 |
| `sophisticatedbackpacks-1.21.1-3.23.4.2.103.jar` | `1.21.1-3.23.4.3.106` 후보 있음 | 1.7.3 테스트에는 이미 `Inmis`가 있으므로 중복 여부 판단 필요 |
| `sophisticatedcore-1.21.1-1.2.9.14.154.jar` | `1.21.1-1.2.9.21.168` 후보 있음 | SophisticatedBackpacks 의존성 |
| `sound-physics-remastered-fabric-1.21.1-1.4.12.jar` | `fabric-1.21.1-1.5.1` 후보 있음 | 선택적 클라이언트 체감 기능 |
| `Chunky-Fabric-1.4.23.jar` | 1.21.1 Fabric 후보 있음 | 운영/청크 사전 생성 후보 |
| `Clumps-fabric-1.21.1-19.0.0.1.jar` | 1.21.1 Fabric 후보 있음 | 성능 후보 |
| `dynamic-light-0.6.jar` | `0.7+mod` 등 후보 있음 | 클라이언트 편의 후보 |
| `entity-view-distance-1.3.0+1.21.jar` | 1.21.1 Fabric 후보 있음 | 성능/표시 후보 |
| `entityculling-fabric-1.7.4-mc1.21.jar` | `1.10.2` 등 1.21.1 Fabric 후보 있음 | 클라이언트 성능 후보 |
| `ferritecore-7.0.2-hotfix-fabric.jar` | `7.0.3-fabric` 후보 있음 | 성능 후보 |
| `jei-1.21.1-fabric-19.21.2.313.jar` | `19.27.0.340` 등 1.21.1 Fabric 후보 있음 | 인벤토리 우측 검색 UI. 우선 추가 후보 |
| `justzoom_fabric_2.1.0_MC_1.21.1.jar` | 1.21.1 Fabric 후보 있음 | 클라이언트 편의 후보 |
| `krypton-0.2.8.jar` | 1.21.1 Fabric 후보 있음 | 네트워크 성능 후보 |
| `lithium-fabric-0.15.0+mc1.21.1.jar` | `0.15.3` 등 1.21.1 Fabric 후보 있음 | 성능 후보. 서버/클라이언트 검증 필요 |
| `netprodis-1.1.0+1.21.2.jar` | 1.21/1.21.2 계열 후보 있음 | 기존 파일이 1.21.2 표기라 1.21.1 적용은 주의 |
| `servercore-fabric-1.5.5+1.21.1.jar` | `1.5.17+1.21.1` 후보 있음 | 서버 성능 후보 |
| `show-held-items-0.2.3.jar` | 1.21.1 Fabric 후보 있음 | 표시 편의 후보 |
| `worldedit-mod-7.3.8.jar` | 1.21~1.21.1 Fabric 후보 있음 | 운영 도구 후보. 운영 반영 전 권한/리스크 고려 |
| `CreativeCore_FABRIC_v2.13.5_mc1.21.1.jar` | `2.13.39` 등 후보 있음 | 의존성 |
| `ForgeConfigAPIPort-v21.1.3-1.21.1-Fabric.jar` | `v21.1.6-1.21.1-Fabric` 후보 있음 | 의존성 |
| `Necronomicon-Fabric-1.6.0+1.21.jar` | 1.21.1 Fabric 후보 있음 | 의존성 |
| `YSNS-Fabric_Quilt-MC1.21-1.0.6.jar` | 1.21.1 Fabric 후보 있음 | 의존성 |
| `balm-fabric-1.21.1-21.0.46.jar` | `21.0.58+fabric-1.21.1` 등 후보 있음 | 의존성 |
| `konkrete_fabric_1.9.9_MC_1.21.jar` | 1.21.1 Fabric 후보 있음 | 의존성 |
| `midnightlib-1.6.9-fabric+1.21.jar` | `1.9.3+1.21.1-fabric` 등 후보 있음 | 의존성 |
| `moonlight-1.21-2.18.16-fabric.jar` | `1.21.1-3.0.14` 등 후보 있음 | 의존성 |
| `player-animation-lib-fabric-2.0.1+1.21.1.jar` | `2.0.4+1.21.1-fabric` 후보 있음 | 의존성 |
| `supermartijn642configlib-1.1.8-fabric-mc1.21.jar` | 1.21.1 Fabric 후보 있음 | 의존성 |

### 1.6 전용 또는 1.7.3 후보 미확인

현재 조사 기준으로 1.7.x 대응 후보를 찾지 못했거나, 기존 파일 metadata가 1.6 계열에 묶인 항목이다.

| 161 레거시 모드 | 확인 결과 | 판정 |
| --- | --- | --- |
| `cobblemon-shearems-1.6-fabric-1.1.2.jar` | Modrinth 후보가 `1.6-fabric-*`까지만 확인됨 | 1.7.3 후보 미확인 |
| `cobblemon-unimplementeditems-1.6-fabric-1.1.0.jar` | Modrinth 후보가 `1.6-fabric-*`까지만 확인됨. 기존 metadata도 `cobblemon <=1.7.0` | 1.7.3 제외 유지 |
| `cobblemon-whiteout-1.6-fabric-1.1.1.jar` | Modrinth 후보가 `1.6-fabric-*`까지만 확인됨 | 1.7.3 후보 미확인 |
| `Cobblemon_Legends_Reborn-3.0.0-fabric.jar` | Modrinth 해시/검색 매칭 실패. jar metadata는 `minecraft=1.21.1`, `cobblemon >=1.6.0` | 배포 출처/1.7.3 실사용 검증 필요 |
| `rocket_mons-1.0.jar` | Modrinth 검색 매칭 실패. jar metadata는 `minecraft >=1.20`, 이름은 `Apocalypse Origins`, 설명은 Celesteela 추가 | 배포 출처/1.7.3 실사용 검증 필요 |
| `farsight-fabric-1.21-4.4.jar` | Modrinth 검색 매칭 실패. jar metadata는 `minecraft=1.21.x`, `cupboard >=1.21-1.5` | 기존 파일 자체는 1.21.x 범위이나 출처/최신성 확인 필요 |
| `cupboard-fabric-1.21-2.9.jar` | Modrinth 검색 매칭 실패. jar metadata는 `minecraft=1.21.x` | 기존 파일 자체는 1.21.x 범위이나 출처/최신성 확인 필요 |

## 1.7.3 전환 우선순위 제안

2026-06-07 적용 기준:

1. **바로 적용**: Cobblemon 1.7.x 대응이 명시된 핵심 gameplay 애드온, 관장/배지/진행, 음식 잔여 참조, 이동 콘텐츠 중 기존 모드와 직접 대응되는 항목.
2. **보류**: 편의 UI, 검색, 줌, 단순 표시, 사진/카메라, 성능 튜닝, 중복 보관 모드.
3. **제외 또는 후순위**: 1.6 전용, 출처 불명확, 기존 모드와 다른 대체 모드.

### 2026-06-07 173 라인 적용 완료

아래 항목은 173 라인 `/home/icenux/minecraft/icecoke-cobblemon-173-test/mods`, 로컬 Modrinth 프로필 `icecoke-cobblemon-173`, repo `client-mods/required`에 배치했다. 2026-06-07 19:20 KST에 25566 173 라인을 재시작해 실제 로드까지 확인했다.

| 구분 | 적용 파일 |
| --- | --- |
| Cobblemon 1.7.x 명시 대응 | `cobblecuisine-2.0.1-1.7-rc1.jar` |
| Cobblemon 1.7.x 명시 대응 | `CobblemonRepel-1.7-1.4.jar` |
| Cobblemon 1.7.x 명시 대응 | `Cobbreeding-fabric-2.2.1.jar` |
| Cobblemon 1.7.x 명시 대응 | `SimpleTMs-fabric-2.3.3.jar` |
| Cobblemon 1.7.x 명시 대응 | `cobblemon-armors-1.6.0+1.7.3.jar` |
| Cobblemon 1.7.x 명시 대응 | `droploottables-fabric-1.7.3-1.9.1.jar` |
| Cobblemon 1.7.x 명시 대응 | `extra-move-anims-cobblemon-1.7v1.0.2.jar` |
| 관장/배지 | `cobblebuilds-leaders-0.1.1-hf.1.jar` |
| 관장/배지 | `badgebox-fabric-1.3.0.jar` |
| 관장/NPC 보조 | `easy_npc_bundle-6.2.0-fabric-1.21.1.jar` |
| 레벨/진행 | `rctapi-fabric-1.21.1-0.15.2-beta.jar` |
| 레벨/진행 | `rctmod-fabric-1.21.1-0.18.1-beta.jar` |
| 음식/잔여 참조 | `FarmersDelight-1.21.1-3.2.8+refabricated.jar` |
| 음식/잔여 참조 | `cobblecuisine-delight-1.1.jar` |
| 이동 콘텐츠 | `immersive_aircraft-1.4.6+1.21.1-fabric.jar` |
| 이동 콘텐츠 | `gliders-1.21.1-fabric-1.1.8.jar` |
| Cobblemon riding 확장 | `gotta-ride-em-all.jar` |
| 의존성 | `ForgeConfigAPIPort-v21.1.6-1.21.1-Fabric.jar` |
| 의존성 | `common-networking-fabric-1.0.21-1.21.1.jar` |
| 의존성 교체 | `geckolib-fabric-1.21.1-4.8.4.jar` |
| 의존성 교체 | `timcore-fabric-1.7.3-1.32.0.jar` |

의존성 조정:

- `Cobblemon Armors 1.6.0+1.7.3` 때문에 `GeckoLib`을 `4.7.6`에서 `4.8.4`로 올렸다.
- `DropLootTables 1.7.3-fabric-1.9.1` 때문에 `Tim Core`를 `1.31.0`에서 `1.32.0`으로 올렸다.
- 최신 `Farmer's Delight 3.3.3`은 `Fabric Loader 0.19+`를 요구해 현재 173 라인의 `Fabric Loader 0.17.3`과 맞지 않는다. Loader를 올리지 않고 `3.2.8`로 낮췄다.
- `Gliders`의 jar metadata가 `commonnetworking`을 요구해 `Common Network 1.0.21`을 추가했다.
- 최신 `Easy NPC 6.17.0`은 `Fabric Loader 0.18.3+`를 요구해 현재 173 라인의 `Fabric Loader 0.17.3`과 맞지 않는다. Loader를 올리지 않고 `6.2.0 bundle`로 낮췄다.
- 기존 161 레거시의 `cobbleride`는 Modrinth 해시 기준 `Cobblemon: Ride On!`으로 확인됐지만, 검증 결과 `Cobblemon >=1.7`과 명시 충돌해 제거했다. 1.7 riding 확장 후보로 `Gotta Ride 'Em All 1.0`을 적용했다.

검증:

- 임시 부팅 검증 디렉터리 `/tmp/icecoke-173-bootcheck-20260607-181903`에서 같은 모드셋을 포트 25567로 실행했다.
- 로그 기준 `Done (10.514s)!`까지 도달했다.
- RCTMod가 `Registered 1559 trainers`를 출력했다.
- 이 검증은 현재 실행 중인 25566 서버를 재시작하지 않고 수행했다.
- 추가 적용 후 임시 부팅 검증 디렉터리 `/tmp/icecoke-173-bootcheck-20260607-183158`에서 같은 모드셋을 포트 25567로 실행했다.
- 로그 기준 `Done (9.118s)!`까지 도달했고, RCTMod가 다시 `Registered 1559 trainers`를 출력했다.
- 실제 25566 173 라인 재시작 후 로그 기준 `Done (1.602s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`, 콘솔 `list` 응답을 확인했다.

### 1차 적용 전 보류 유지

아래 판단은 2026-06-07 1차 가벼운 추가 테스트 전 기준이다. 이후 `JEI`, `JustZoom`, `EntityCulling`, `Clumps`, `FerriteCore`, `Krypton`은 일부 적용됐다.

- 편의 UI/검색/줌/표시: `JEI`, `JustZoom`, `Show Held Items`, `Sound Physics`, 사진/카메라 계열.
- 단순 성능 튜닝: `Lithium`, `FerriteCore`, `Krypton`, `ServerCore`, `Clumps`, `EntityCulling`.
- 중복 가능성이 큰 보관 모드: `Sophisticated Backpacks` 계열. 1.7.3 테스트에는 이미 `Inmis`가 있다.
- 구조물/월드젠 추가: `Cobblemon Extra Structures`는 2차 테스트에 적용했으며, 신규 청크 구조물 생성은 아직 인게임 확인 전이다.
- `Cobblemon: Ride On! / cobbleride`는 1.7.3과 충돌해 제외한다.
- 1.6 전용 또는 출처 불명확 항목은 제외 또는 후순위로 둔다.

### 2026-06-07 가벼운 추가 테스트 후보

현재 173 라인 상태는 아래 백업으로 되돌릴 수 있다.

| 항목 | 값 |
| --- | --- |
| 백업 시각 | `2026-06-07 19:49:54 KST` |
| 백업 파일 | `/home/icenux/minecraft/icecoke-cobblemon-173-test/backups/instance-before-light-main-mods-test-20260607-194954.tar.gz` |
| 해시 파일 | `/home/icenux/minecraft/icecoke-cobblemon-173-test/backups/instance-before-light-main-mods-test-20260607-194954.tar.gz.sha256` |
| 검증 | `sha256sum -c` 결과 `OK` |
| 크기 | `466M` |

본섭 플레이 감각을 1.7.3 서버에 조금씩 맞추려면 아래 순서가 가장 작다.

| 우선순위 | 후보 | 적용 범위 | 이유 | 현재 상태 |
| --- | --- | --- | --- | --- |
| 1 | `fightorflight-fabric-0.10.7.jar` 계열 | 서버+클라이언트 | 본섭의 "포획 실패 후 야생 포켓몬 반격/추격" 체감 복구 후보 | 적용 및 접속 검증 완료 |
| 2 | `jei` | 클라이언트 우선 | 인벤토리 우측 아이템 검색/레시피 UI 복구 | 로컬 프로필 적용 및 접속 검증 완료 |
| 3 | `Clumps` | 서버 우선 | 경험치 오브 병합 성능 개선, gameplay 영향 작음 | 서버 적용 및 부팅 검증 완료 |
| 4 | `FerriteCore` | 서버+클라이언트 가능 | 메모리 최적화, 콘텐츠 추가 없음 | 서버 적용 및 부팅 검증 완료 |
| 5 | `Krypton` | 서버+클라이언트 가능 | 네트워크 최적화, 콘텐츠 추가 없음 | 서버 적용 및 부팅 검증 완료 |
| 6 | `EntityCulling` | 클라이언트 | 렌더링 최적화, 서버 영향 없음 | 로컬 프로필 적용 및 접속 검증 완료 |
| 7 | `Just Zoom` | 클라이언트 | 단순 조작 편의 | `Konkrete`와 함께 로컬 프로필 적용 및 접속 검증 완료 |
| 8 | `Show Held Items` | 클라이언트 중심 | 손에 든 아이템 표시 편의 | 제외. `show-held-items-0.2.3.jar` metadata가 `cobblemon: 1.6.1` 고정 의존성 |

적용 결과:

| 위치 | 추가 파일 |
| --- | --- |
| 173 라인 `mods/` | `fightorflight-fabric-0.10.7.jar`, `Clumps-fabric-1.21.1-19.0.0.1.jar`, `ferritecore-7.0.3-fabric.jar`, `krypton-0.2.8.jar` |
| 로컬 `icecoke-cobblemon-173` 프로필 | `fightorflight-fabric-0.10.7.jar`, `jei-1.21.1-fabric-19.27.0.340.jar`, `entityculling-fabric-1.10.2-mc1.21.1.jar`, `justzoom_fabric_2.1.0_MC_1.21.1.jar`, `konkrete_fabric_1.9.9_MC_1.21.jar` |
| repo `client-mods/required` | `fightorflight-fabric-0.10.7.jar` |
| repo `client-mods/optional` | `jei-1.21.1-fabric-19.27.0.340.jar`, `entityculling-fabric-1.10.2-mc1.21.1.jar`, `justzoom_fabric_2.1.0_MC_1.21.1.jar`, `konkrete_fabric_1.9.9_MC_1.21.jar` |

검증:

- 25566 173 라인 재시작 후 `Fight or Flight`, `FOF tasks injected`, `Krypton`, `Done (1.823s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`를 확인했다.
- `fightorflight.json5`가 생성됐고, `do_pokemon_attack=true`, `failed_capture_counted_as_provocation=true`, `minimum_attack_level=5`로 본섭의 핵심 동작과 같은 방향이다.
- 로컬 173 프로필 실행 후 로그 기준 `Connecting to 192.168.219.110, 25566`, `Applying server overrides`, `Minimap updated server level id`를 확인했다.
- 서버 로그 기준 `Icecokel joined the game` 후 테스트 종료 시 `lost connection: Disconnected`를 확인했다.

2차 후보는 기능은 작지만 서버/클라이언트 양쪽 영향 또는 gameplay 영향이 있으므로 1차 후보 검증 후 본다.

| 후보 | 적용 범위 | 판단 |
| --- | --- | --- |
| `Berry Pouch` | 서버+클라이언트 | 적용 및 접속 검증 완료. 베리 보관 UI/아이템 실제 사용은 인게임 확인 필요 |
| `Safe Pastures` | 서버+클라이언트 | 포켓몬 보관/목장 안정성 계열 후보. 실제 사용 목적 확인 후 테스트 |
| `SittingPlus` | 서버+클라이언트 가능 | 상호작용 편의. 기능 작음 |
| `CobbleDollars` | 서버+클라이언트 | 경제/상점 목적이 생기면 후보. 현재는 보상 시스템으로 대체 가능 |
| `Cobblemon Smartphone` | 서버+클라이언트 | UI 기능 후보. 현재 개인 서버 필수 기능은 아님 |
| `Pokeblocks`, `Eggs`, `Poke Clothing` | 서버+클라이언트 | Cobblemon 부가 콘텐츠. 1.7.3 대응 확인 후 별도 묶음 테스트 |

이번 라운드에서 계속 보류할 항목은 아래처럼 둔다.

| 보류/제외 | 이유 |
| --- | --- |
| `Sophisticated Backpacks` | 1.7.3 테스트에는 이미 `Inmis`가 있어 가방 기능 중복 |
| `Exposure`, `Exposure Polaroid` | 사진/카메라 계열이며 이전에 녹화/방송 불필요 모드를 줄인 방향과 맞지 않음 |
| `Sound Physics` | 시각/청각 체감 모드라 필수 아님 |
| `Lithium`, `ServerCore` | 효과는 크지만 서버 로직/설정 영향이 있어 별도 분리 검증 |
| `WorldEdit`, `Chunky` | 운영 도구 성격. 일반 플레이 감각 복구 목적과 다름 |
| `Hardcore Revival` | 개인 서버에서는 필요성이 낮고 사망/부활 규칙과 충돌 여지 있음 |
| `cobbleride` | 1.7.3과 충돌 확인으로 제외 유지 |
| `Shearems`, `Unimplemented Items`, `Whiteout` | 1.6 계열까지만 확인되어 1.7.3 후보 미확인 또는 제외 유지 |

다음 권장 테스트 단위:

1. 인게임에서 `Fight or Flight` 동작을 확인한다. 야생 포켓몬 포획 실패 후 반격/추격 여부가 핵심이다.
2. 로컬에서 `JEI`, `Just Zoom`, `EntityCulling`의 UI/키 충돌을 확인한다.
3. 서버 성능 후보 `Clumps`, `FerriteCore`, `Krypton` 적용 후 10분 이상 접속 유지와 로그 경고를 확인한다.
4. 2차 gameplay 후보 중 `Berry Pouch`, `Cobblemon Extra Structures`는 적용됐으므로, 베리 파우치 실제 사용과 신규 청크 구조물 생성을 확인한다.

### 2026-06-07 Berry Pouch / Extra Structures 적용

`Berry Pouch`와 `Cobblemon Extra Structures`는 사용자가 직접 테스트해보고 싶은 대상으로 지정해 별도 백업 후 적용했다.

| 항목 | 값 |
| --- | --- |
| 서버 백업 | `/home/icenux/minecraft/icecoke-cobblemon-173-test/backups/instance-before-berry-structures-20260607-210909.tar.gz` |
| 서버 백업 검증 | `sha256sum -c` 결과 `OK` |
| 로컬 모드 백업 | `/Users/smlee/mingle-lounge/backups/local-173-mods/icecoke-173-local-mods-before-berry-structures-20260607-210943.tar.gz` |
| 로컬 백업 검증 | `shasum -a 256 -c` 결과 `OK` |

적용 결과:

| 위치 | 추가 파일 |
| --- | --- |
| 173 라인 `mods/` | `berrypouch-fabric-1.21.1-0.5.4-beta.jar`, `cobblemonextrastructures-1.21.1-1.3.0-fabric.jar` |
| 로컬 `icecoke-cobblemon-173` 프로필 | `berrypouch-fabric-1.21.1-0.5.4-beta.jar`, `cobblemonextrastructures-1.21.1-1.3.0-fabric.jar` |
| repo `client-mods/required` | `berrypouch-fabric-1.21.1-0.5.4-beta.jar` |
| repo `client-mods/optional` | `cobblemonextrastructures-1.21.1-1.3.0-fabric.jar` |

검증:

- 25566 173 라인 재시작 후 `Found new data pack berrypouch`, `Found new data pack cobblemonextrastructures`, `Done (1.665s)!`, `Data pack initialized: rctmod`, `Registered 1559 trainers`를 확인했다.
- 로컬 173 프로필 실행 후 로그 기준 `Connecting to 192.168.219.110, 25566`, `Applying server overrides`, `Minimap updated server level id`를 확인했다.
- 서버 로그 기준 `Icecokel joined the game` 후 테스트 종료 시 `lost connection: Disconnected`를 확인했다.
- `Cobblemon Extra Structures`는 `cobblemonextrastructures:sprout_tower` advancement가 없는 아이템 `cobblemonextrastructures:bellsprout_statue`를 참조하는 경고가 남는다. 서버 부팅과 접속은 통과했지만, 신규 청크에서 구조물이 정상 생성되는지는 별도 확인이 필요하다.

## 전환 원칙

- 남은 후보를 한 번에 넣지 않는다.
- 1.7.3 대응 버전과 의존성을 확인한 뒤 기능 묶음별로 추가한다.
- 클라이언트가 필요한 모드는 로컬 `icecoke-cobblemon-173` 프로필에도 같은 조건으로 넣는다.
- 추가 후에는 최소 `서버 기동`, `클라이언트 접속`, `5분 유지`, `기능 1회 사용`, `로그 확인`을 반복한다.
- 1.6 전용으로 보이는 파일명은 그대로 복사하지 않고 1.7.3 대응 파일을 찾는다.
