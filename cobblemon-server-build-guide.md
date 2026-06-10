# Mingle Lounge Cobblemon 서버 구축 가이드

마지막 갱신: 2026-06-03

> 현재 `icecoke-cobblemon` 서버를 새로 재현하기 위한 최신 구축 절차가 아닙니다. 이 문서는 이전 Mingle Lounge `Cobblemon 1.7.3` 기준 참고용입니다. 현재 서버 운영/복구/재구축 판단은 [docs/server/README.md](/Users/smlee/mingle-lounge/docs/server/README.md), [docs/server/OPS_RUNBOOK.md](/Users/smlee/mingle-lounge/docs/server/OPS_RUNBOOK.md), [docs/server/MODS_AND_CLIENT.md](/Users/smlee/mingle-lounge/docs/server/MODS_AND_CLIENT.md)를 우선합니다.

이 문서는 새 `mingle-lounge` Cobblemon 서버를 처음부터 구축할 때 사용하는 작업 가이드입니다. 목표는 에이전트가 이 문서만 보고 새 Fabric 서버를 현재 안정화 기준과 같은 상태로 만들 수 있게 하는 것입니다.

구축 완료 후 결과 비교는 [기준 세팅](/Users/smlee/mingle-lounge/cobblemon-current-settings.md)을 기준으로 합니다.

## 1. 기본 원칙

안정성을 최우선으로 둡니다. 새 기능보다 서버 기동 성공, 서버 로그 안정성, 서버 모드 버전 일치가 우선입니다.

현재 기준선은 Minecraft `1.21.1`, Fabric Loader `0.19.2`, Java 21, Cobblemon `1.7.3`입니다. 이 기준을 벗어나는 모드는 설치하지 않습니다.

서버 접속에 필요한 모드는 18개만 유지합니다. 역할이 겹치거나 충돌 이력이 있는 모드는 넣지 않습니다.

## 2. 새 서버 생성

| 항목 | 값 |
| --- | --- |
| 서버 이름 | `mingle-lounge` |
| 서버 주소 | 신규 서버에서 발급된 주소 사용 |
| 플랫폼 | 일반 Minecraft Java 서버 호스팅 또는 직접 구동 서버 |
| Software/Loader | Fabric |
| Minecraft | `1.21.1` |
| Fabric Loader | `0.19.2` |
| Java | Java 21 |

작업 순서:

1. 새 Minecraft Java 서버를 생성합니다.
2. 서버 이름을 `mingle-lounge`로 맞춥니다.
3. 서버 소프트웨어를 Fabric으로 선택합니다.
4. Minecraft 버전을 `1.21.1`로 맞춥니다.
5. Fabric Loader를 `0.19.2`로 맞춥니다.
6. Java가 Java 21로 잡히는지 확인합니다.
7. 서버를 아직 시작하지 말고 먼저 모드를 설치합니다.

## 3. 설치할 서버 모드

서버의 `mods` 폴더에 아래 모드만 설치합니다. 버전은 가능한 한 파일명과 일치시킵니다.

| 구분 | 모드/파일 |
| --- | --- |
| 필수 코어 | `Cobblemon-fabric-1.7.3+1.21.1.jar` |
| 필수 코어 | `fabric-api-0.116.12+1.21.1.jar` |
| 보상볼 | `cobbleloots-fabric-2.3.0.jar` |
| 알림 | `cobblemon_spawn_alerts-fabric-1.13.2.jar` |
| 포획 경험치 | `capturexp-fabric-1.7.3-1.3.0.jar` |
| 전투 보조 | `cobblemon-battle-extras-fabric-1.13.45.jar` |
| 관장 배지 | `cobblemonpokemonbadges-fabric-0.1.1.jar` |
| 메가진화 | `mega_showdown-fabric-1.8.4+1.7.3+1.21.1.jar` |
| 전설 소환 | `MythsAndLegends-fabric-1.9.0.jar` |
| 전설 소지 제한 | `LimitedLegends-fabric-1.9.0.jar` |
| 백팩 | `inmis-2.8.2-1.21.1.jar` |
| 의존성 | `accessories-fabric-1.1.0-beta.53+1.21.1.jar` |
| 의존성 | `architectury-13.0.8-fabric.jar` |
| 의존성 | `cloth-config-15.0.140-fabric.jar` |
| 의존성 | `emberstextapi-fabric-1.21.1-3.0.0-alpha.2.jar` |
| 의존성 | `fabric-language-kotlin-1.13.11+kotlin.2.3.21.jar` |
| 의존성 | `owo-lib-0.13.0-alpha.15+1.21.jar` |
| 의존성 | `timcore-fabric-1.7.3-1.31.0.jar` |

모드 설치 후 서버를 한 번 시작했다가 정상 기동 로그를 확인합니다. 설정 파일이 생성되면 서버를 다시 끄고 다음 설정을 진행합니다.

## 4. 설치하지 않을 모드

아래 모드는 현재 안정화 기준에서 제외합니다.

| 모드 | 제외 이유 |
| --- | --- |
| `CobblemonRider` | Cobblemon 기본 라이딩과 역할이 겹치고 안정성 우선 기준에서 제거함 |
| `timcore-fabric-1.8.0...` | Cobblemon 1.8 계열 기준이라 현재 Cobblemon `1.7.3`과 맞지 않음 |
| `particular` | `owo-lib` 충돌 이력이 있어 제거함 |
| `Iris`, `Sodium`, 쉐이더팩 | 서버 모드가 아니므로 설치하지 않음 |

## 5. 데이터팩 설치

스타터 보상, 6시간 접속 보상, 도감 보상, 관장 NPC, 시간 설정, 전설 소환 데이터팩을 새 서버 월드에 설치합니다.

워크스페이스에 준비된 데이터팩 원본:

```text
/Users/smlee/mingle-lounge/datapacks/mingle-starter-balls
/Users/smlee/mingle-lounge/datapacks/mingle-starter-balls.zip
/Users/smlee/mingle-lounge/datapacks/mingle-login-reward
/Users/smlee/mingle-lounge/datapacks/mingle-login-reward.zip
/Users/smlee/mingle-lounge/datapacks/mingle-dex-rewards
/Users/smlee/mingle-lounge/datapacks/mingle-dex-rewards.zip
/Users/smlee/mingle-lounge/datapacks/cobblemon-indigo.zip
/Users/smlee/mingle-lounge/datapacks/mingle-time-settings
/Users/smlee/mingle-lounge/datapacks/mingle-time-settings.zip
/Users/smlee/mingle-lounge/datapacks/mingle-gym-party-overrides
/Users/smlee/mingle-lounge/datapacks/mingle-gym-party-overrides.zip
```

서버 파일 위치:

```text
world/datapacks/mingle-starter-balls
world/datapacks/mingle-login-reward.zip
world/datapacks/mingle-dex-rewards.zip
world/datapacks/cobblemon-indigo.zip
world/datapacks/mingle-time-settings.zip
world/datapacks/mingle-gym-party-overrides.zip
world/datapacks/MythsAndLegends-Datapack-v1.0.5.zip
```

zip 배포가 불편한 환경이면 폴더를 직접 만들고 아래 파일을 같은 구조로 생성합니다.

```text
world/datapacks/mingle-starter-balls/pack.mcmeta
world/datapacks/mingle-starter-balls/data/minecraft/tags/function/load.json
world/datapacks/mingle-starter-balls/data/minecraft/tags/function/tick.json
world/datapacks/mingle-starter-balls/data/mingle_starter/function/load.mcfunction
world/datapacks/mingle-starter-balls/data/mingle_starter/function/tick.mcfunction
world/datapacks/mingle-starter-balls/data/mingle_starter/function/grant.mcfunction
world/datapacks/mingle-login-reward.zip
world/datapacks/mingle-dex-rewards.zip
world/datapacks/cobblemon-indigo.zip
world/datapacks/mingle-time-settings.zip
```

`cobblemon-indigo.zip`은 Cobblemon NPC 데이터팩입니다. 관동 8관장, 사천왕, 챔피언 프리셋과 배지 지급 흐름을 추가합니다. 배지 아이템 지급을 위해 서버와 클라이언트 모두 `cobblemonpokemonbadges-fabric-0.1.1.jar`가 필요합니다. 관장 NPC는 자동 배치되지 않으므로 OP 권한으로 `/spawnnpc cobblemon:indigo_leader_brock` 같은 명령을 사용해 직접 배치합니다.

File Browser 기반 서버에 Indigo를 반영할 때 업로드했던 파일과 기준 해시는 아래와 같습니다.

| 서버 경로 | 로컬 파일 | SHA-256 |
| --- | --- | --- |
| `mods/cobblemonpokemonbadges-fabric-0.1.1.jar` | `work/indigo-20260528/server-upload/mods/cobblemonpokemonbadges-fabric-0.1.1.jar` | `a5011078a804bdff0d299fe2e0e33010c92c976408524d9b0df041030d73f941` |
| `world/datapacks/cobblemon-indigo.zip` | `work/indigo-20260528/server-upload/world/datapacks/cobblemon-indigo.zip` | `8aff092a0009b0a3de79c0652f5a26a067ad8b7941e721b8a5257b1bc1643303` |

2026-05-28 File Browser 기반 서버에는 위 두 파일을 업로드했고, 서버에서 다시 읽은 파일의 SHA-256이 기준 해시와 일치함을 확인했습니다. 모드 jar 추가는 서버 재시작 전에는 반영되지 않으므로, 업로드 검증 뒤 사용자가 서버 관리 버튼으로 재시작해야 합니다.

`mingle-time-settings.zip`은 데이터팩 로드 시 아래 gamerule을 적용합니다. 이는 Cobblemon 기본 흐름에 맞춰 밤/날씨 순환을 켜는 설정이며, `doMobSpawning`은 바닐라 적대 몹 억제 목적과 별개라 건드리지 않습니다.

```mcfunction
gamerule doDaylightCycle true
gamerule doWeatherCycle true
```

`grant.mcfunction`은 아래 내용이어야 합니다.

```mcfunction
# === 스타터 보상 ===
execute store success score @s ml_starter_balls run give @s cobblemon:poke_ball 20
execute if score @s ml_starter_balls matches 1 run give @s cobblemon:great_ball 5
execute if score @s ml_starter_balls matches 1 run give @s minecraft:cooked_beef 30
execute if score @s ml_starter_balls matches 1 run tellraw @s {"text":"스타터 보상: 몬스터볼 20개 + 슈퍼볼 5개 + 스테이크 30개","color":"green"}
```

`load.mcfunction`은 objective 생성만 담당합니다.

```mcfunction
scoreboard objectives add ml_starter_balls dummy
scoreboard objectives add ml_starter_pokedex dummy
scoreboard objectives add ml_starter_backpack dummy
```

`tick.mcfunction`은 접속 중인 모든 플레이어를 점수가 없을 때만 `0`으로 초기 등록하고, 아직 받지 않은 보상만 지급합니다.

```mcfunction
scoreboard players add @a ml_starter_balls 0
scoreboard players add @a ml_starter_pokedex 0
scoreboard players add @a ml_starter_backpack 0
execute as @a[scores={ml_starter_balls=0}] run function mingle_starter:grant
execute as @a[scores={ml_starter_pokedex=0}] store success score @s ml_starter_pokedex run give @s cobblemon:pokedex_red 1
execute as @a[scores={ml_starter_pokedex=1}] run tellraw @s {"text":"스타터 도감 보상: 포켓몬 도감 1개","color":"green"}
scoreboard players set @a[scores={ml_starter_pokedex=1}] ml_starter_pokedex 2
execute as @a[scores={ml_starter_backpack=0}] store success score @s ml_starter_backpack run give @s inmis:baby_backpack 1
execute as @a[scores={ml_starter_backpack=1}] run tellraw @s {"text":"스타터 백팩 보상: Baby Backpack 1개","color":"green"}
scoreboard players set @a[scores={ml_starter_backpack=1}] ml_starter_backpack 2
```

이 데이터팩은 scoreboard `ml_starter_balls`, `ml_starter_pokedex`, `ml_starter_backpack`으로 플레이어별 지급 여부를 기록합니다. 새 서버에 처음 접속하거나 아직 지급 기록이 없는 플레이어는 몬스터볼 20개, 슈퍼볼 5개, 스테이크 30개, 포켓몬 도감 1개, Baby Backpack 1개를 1회 받습니다. 이미 기존 스타터 보상을 받은 플레이어도 도감이나 백팩 지급 기록이 없으면 다음 접속 시 해당 보상을 1회 받습니다. 도감/백팩 지급 성공 후 각 값은 `2`로 고정됩니다.

`mingle-login-reward`는 마지막 보상 수령 후 서버 가동시간 기준 6시간이 지난 플레이어에게 접속 보상을 지급합니다. 데이터팩은 scoreboard `ml_login_clock`, `ml_login_seen`, `ml_login_last`, `ml_login_elapsed`로 서버 가동시간과 플레이어별 마지막 보상 수령 시각을 기록합니다. 서버가 꺼져 있던 시간은 데이터팩만으로 계산하지 못하므로 카운트에 포함되지 않습니다. 보상은 몬스터볼 5개 확정 지급이며, 추가 보상은 40% 추가 없음, 25% 슈퍼볼 3개, 15% 경험치 사탕 XS 2개, 10% 경험치 사탕 XS 5개, 5% 부활초 1개, 3% 하이퍼볼 1개, 2% 기력의 조각 1개입니다.

`mingle-dex-rewards`는 hidden advancement로 일반 포켓몬 920종, 전설/환상/울트라비스트 105종을 분리 추적합니다. 서버 데이터팩 적용 이후 새로 잡거나 진화로 등록한 고유 종 기준으로 일반 도감 10/30/50/100/250/500/750종 보상과 전설/환상 첫 등록 보상을 지급합니다. 기존 도감 기록은 자동 소급하지 않습니다.

주의: 플레이어 인벤토리가 꽉 차 있으면 몬스터볼이 인벤토리에 들어가지 않고 플레이어 근처 바닥에 드랍될 수 있습니다.

## 6. 서버 명령어 세팅

서버를 켠 뒤 서버 콘솔에서 아래 명령을 실행합니다.

```mcfunction
gamerule doMobSpawning false
difficulty normal
gamerule spawnRadius 0
setworldspawn -344 80 232
reload
```

의도는 기본 Minecraft 몬스터를 막고, Cobblemon 플레이와 포켓몬센터 근처 시작 위치를 유지하는 것입니다.

새 월드 초기 기동 중 적대 몬스터가 이미 생성됐다면 필요한 경우에만 적대 몬스터를 정리합니다.

```mcfunction
kill @e[type=minecraft:zombie]
kill @e[type=minecraft:skeleton]
kill @e[type=minecraft:creeper]
kill @e[type=minecraft:spider]
kill @e[type=minecraft:enderman]
kill @e[type=minecraft:witch]
```

넓은 범위의 `kill @e[...]` 명령은 아이템, NPC, 포켓몬 외 엔티티까지 지울 수 있으므로 피합니다.

## 7. Cobbleloots 설정

직장인 플레이 기준으로 몬스터볼과 회복템 수급을 완화합니다.

서버 파일에서 Cobbleloots 설정 파일을 찾아 아래 값으로 맞춥니다. 파일명은 모드 버전에 따라 다를 수 있으므로 `config` 폴더에서 `cobbleloots`가 들어간 파일을 찾습니다.

| 설정 | 값 |
| --- | --- |
| `loot_ball_bonus_chance` | `0.25` |
| `generation_chance` | `0.08` |
| `generation_attempts_per_chunk` | `3` |
| `generation_chunk_cap` | `6` |
| `spawning_chance` | `0.5` |
| `spawning_cooldown_min` | `2400` |
| `spawning_cooldown_max` | `12000` |
| `fishing_chance` | `0.03` |
| `fishing_luck_of_the_sea_multiplier` | `1.5` |

설정 파일이 아직 생성되지 않았으면 서버를 한 번 켰다가 끈 뒤 다시 서버의 `config` 폴더를 확인합니다.

## 8. 전투 속도 설정

전투 속도는 `2.0`을 기준으로 둡니다.

서버의 `config` 폴더에서 Cobblemon Battle Extras 설정 파일을 찾아 battle speed 계열 값을 `2.0`으로 맞춥니다.

전투 속도 설정은 설정 파일 값과 서버 재시작 후 로그를 함께 확인합니다.

## 9. 전설 포켓몬 제한 설정

`Limited Legends` 설정 파일은 서버의 `config/limitedlegends.json`에 둡니다.

현재 운영 기준:

| 설정 | 값 |
| --- | --- |
| `SetLimitsPerPlayer` | `true` |
| `MaxLimitedPerPlayer` | `1` |
| `SetGlobalLimits` | `false` |
| `DisableSpawning` | `false` |

의도는 서버 전체 1마리가 아니라 플레이어 1인당 전설/환상 포켓몬 1마리만 허용하는 것입니다. 기존 플레이어 포획 기록이 있는 서버에 적용한 뒤에는 서버 재시작 후 필요하면 `/limitedlegends backfill`을 1회 실행해 기존 보유 기록을 반영합니다.

## 10. 새 서버 검증 순서

서버 구축 후 아래 순서로 확인합니다.

1. 서버를 시작합니다.
2. 서버 콘솔에서 정상 기동됐는지 확인합니다.
3. 서버 콘솔에서 데이터팩 로딩 로그를 확인합니다.

```text
Found new data pack file/mingle-starter-balls, loading it automatically
```

4. 서버 콘솔에서 아래 명령으로 데이터팩을 확인합니다.

```mcfunction
datapack list
```

5. `datapack list`에 `MythsAndLegends-Datapack-v1.0.5.zip`이 로드되는지 확인합니다.
6. 서버 콘솔에서 테스트 플레이어 접속 로그를 확인합니다.
7. 테스트 플레이어 접속 후 아래 보상 메시지가 기록되는지 확인합니다.

```text
스타터 보상: 몬스터볼 20개 + 슈퍼볼 5개 + 스테이크 30개
스타터 도감 보상: 포켓몬 도감 1개
스타터 백팩 보상: Baby Backpack 1개
6시간 접속 보상: 몬스터볼 5개와 랜덤 추가 보상을 확인하세요.
```

8. 지급 점수를 확인합니다.

```mcfunction
scoreboard players get <플레이어명> ml_starter_balls
scoreboard players get <플레이어명> ml_starter_pokedex
scoreboard players get <플레이어명> ml_starter_backpack
scoreboard players get <플레이어명> ml_login_last
scoreboard players get <플레이어명> ml_login_elapsed
```

9. Myths and Legends 아이템 ID가 등록됐는지 OP 계정이나 콘솔 권한으로 확인합니다.

```mcfunction
give <플레이어명> mythsandlegends:tidal_bell 1
give <플레이어명> mythsandlegends:dr_fujis_diary 1
give <플레이어명> mythsandlegends:azure_flute 1
```

10. 일반 플레이어 계정에서는 `/give`가 권한 문제로 차단되는 것이 정상입니다. 채팅 입력 중 `mythsandlegends:` 뒤에 키 아이템 자동완성이 보이면 클라이언트/서버 모드 등록은 된 상태로 봅니다.
11. 접속 후 5분 이상 서버 크래시, 강제 종료, 반복 오류 로그가 없는지 봅니다.

## 11. 종료 규칙

서버 테스트가 끝났고 사용자가 종료를 요청하면 서버 프로세스를 정상 종료합니다.
