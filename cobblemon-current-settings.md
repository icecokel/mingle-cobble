# Mingle Lounge Cobblemon 기준 세팅

마지막 갱신: 2026-06-03

> 현재 `icenux-ms7b23`에서 실행 중인 서버 기준 문서가 아닙니다. 이 문서는 이전 Mingle Lounge `Cobblemon 1.7.3` 구성 참고용으로 남겨 둡니다. 현재 운영 기준은 [docs/server/README.md](/Users/smlee/mingle-lounge/docs/server/README.md)와 [docs/server/SERVER_CONCEPT.md](/Users/smlee/mingle-lounge/docs/server/SERVER_CONCEPT.md)입니다.

이 문서는 Mingle Lounge Cobblemon 서버를 새로 구성하거나 비교할 때 사용하는 기준 세팅입니다. 서버 접속 주소나 관리 페이지 주소는 이 문서에 기록하지 않습니다. 처음 접속하는 사람에게 공유할 설치 절차는 [접속 가이드](/Users/smlee/mingle-lounge/cobblemon-client-setup-guide.md)를 사용합니다.

## 서버 기본 정보

| 항목 | 값 |
| --- | --- |
| 서버 MOTD | `이든모 서버` |
| 서버 플랫폼 | 일반 Minecraft Java 서버 |
| Minecraft | `1.21.1` |
| Loader | Fabric |
| Fabric Loader | `0.19.2` |
| Cobblemon | `1.7.3` |
| 권장 Java | Java 21 |

## 서버 접근 권한 메모

| 항목 | 현재 확인/메모 |
| --- | --- |
| 파일 관리 | 관리자용 File Browser `admin` 계정으로 접근 가능 |
| 파일 작업 | 서버 파일 읽기, 편집, 업로드, 다운로드, 삭제, 이동, 이름 변경 가능 |
| 표준 작업 방식 | 서버 파일은 로컬에서 수정한 뒤 File Browser로 업로드하고, 업로드 후 재다운로드로 확인 |
| 서버 터미널 | 현재 사용할 수 없음. File Browser 파일 권한과 터미널 권한은 별개로 취급 |
| 주요 수정 가능 범위 | `mods`, `config`, `world/datapacks`, `server.properties`, `start.sh`, `user_jvm_args.txt` |
| 서버 재시작 | 사용자가 별도 버튼으로 재시작 가능 |
| 서버 정지 | 현재 관리자가 서버를 완전히 정지할 수 없음 |
| 에이전트 주의 | 재시작이 필요한 변경 후에는 사용자가 버튼으로 재시작해야 함 |

운영 제약 상세는 [서버 운영 제약](/Users/smlee/mingle-lounge/server-operation-constraints.md)을 기준으로 봅니다. 특히 `.mca` 월드 파일 교체 작업은 서버 정지가 불가능한 환경에서는 업로드 완료와 복구 완료를 분리해서 판단합니다.

## 서버 설치 모드

서버 접속을 위해 로컬 클라이언트에도 같은 주요 모드가 필요합니다.

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

## 서버 게임 설정

| 항목 | 현재 값 |
| --- | --- |
| 기본 Minecraft 몬스터 | 비활성화 |
| Cobblemon 포켓몬 스폰 | 활성 유지 |
| 서버 전투 속도 | `2.0` |
| 월드 스폰 | 포켓몬센터가 있는 마을 근처 |
| 스폰 반경 | `0` |
| 월드 스폰 좌표 | `-344 80 232` |
| 기준 포켓몬센터 근처 좌표 | 약 `-352, 224` |
| 스타터 보상 | 데이터팩 기준 미수령 플레이어에게 몬스터볼 20개, 슈퍼볼 5개, 스테이크 30개, 포켓몬 도감 1개, Baby Backpack 1개 1회 지급 |
| 전설 소지 제한 | `LimitedLegends` 기준 플레이어 1인당 전설/환상 포켓몬 1마리 |

서버는 기본 Minecraft 좀비, 해골 같은 적대 몬스터를 막고 Cobblemon 플레이에 집중하는 방향으로 맞춰져 있습니다.

## 서버 데이터팩

| 데이터팩 | 역할 |
| --- | --- |
| `mingle-starter-balls` | 처음 접속하거나 아직 스타터 보상을 받지 않은 플레이어에게 몬스터볼 20개, 슈퍼볼 5개, 스테이크 30개, 포켓몬 도감 1개, Baby Backpack 1개를 1회 지급 |
| `mingle-login-reward.zip` | 마지막 보상 수령 후 서버 가동시간 기준 6시간이 지난 플레이어에게 몬스터볼 5개 확정 지급 + 랜덤 추가 보상 1회 지급 |
| `mingle-dex-rewards` | 데이터팩 적용 이후 새로 잡거나 진화로 등록한 고유 종 기준으로 일반 도감 10/30/50/100/250/500/750종 보상과 전설/환상 첫 등록 보상 지급 |
| `cobblemon-indigo.zip` | 관동 8관장, 사천왕, 챔피언 NPC 프리셋과 관장 격파 배지 지급 |
| `MythsAndLegends-Datapack-v1.0.5.zip` | 특수 조건/아이템 기반 전설 포켓몬 소환 콘텐츠 |
| `mingle-time-settings.zip` | Cobblemon 기본 흐름에 맞춰 데이터팩 로드 시 `doDaylightCycle=true`, `doWeatherCycle=true` 적용 |
| `mingle-gym-party-overrides.zip` | CobbleBuilds 8관장 원본 파티를 서버 컨셉의 단계식 관장 라인업으로 override |

데이터팩은 scoreboard `ml_starter_balls`, `ml_starter_pokedex`, `ml_starter_backpack`으로 플레이어별 지급 여부를 기록합니다. `ml_starter_balls`는 몬스터볼/슈퍼볼/스테이크 보상, `ml_starter_pokedex`는 포켓몬 도감 보상, `ml_starter_backpack`은 Baby Backpack 보상입니다. 기존에 스타터 보상을 이미 받은 유저도 `ml_starter_pokedex` 또는 `ml_starter_backpack` 기록이 없으면 다음 접속 시 해당 보상을 1회 받습니다.

6시간 접속 보상 데이터팩은 scoreboard `ml_login_clock`, `ml_login_seen`, `ml_login_last`, `ml_login_elapsed`로 서버 가동시간과 플레이어별 마지막 보상 수령 시각을 기록합니다. 플레이어는 마지막 보상 수령 후 서버가 켜져 있던 시간이 6시간 이상 지나면 몬스터볼 5개를 확정으로 받고, 추가 보상은 아래 확률 중 하나로 정해집니다. 서버가 꺼져 있던 시간은 데이터팩만으로 계산하지 못하므로 카운트에 포함되지 않습니다.

| 확률 | 랜덤 추가 보상 |
| --- | --- |
| 40% | 추가 없음 |
| 25% | 슈퍼볼 3개 |
| 15% | 경험치 사탕 XS 2개 |
| 10% | 경험치 사탕 XS 5개 |
| 5% | 부활초 1개 |
| 3% | 하이퍼볼 1개 |
| 2% | 기력의 조각 1개 |

도감 보상 데이터팩은 hidden advancement로 일반 포켓몬 920종, 전설/환상/울트라비스트 105종을 분리 추적합니다. 일반 도감 보상은 scoreboard `ml_dex_count`와 `ml_dex_r10`, `ml_dex_r30`, `ml_dex_r50`, `ml_dex_r100`, `ml_dex_r250`, `ml_dex_r500`, `ml_dex_r750`으로 지급 여부를 기록합니다. 전설/환상 첫 등록 보상은 `ml_dex_special_count`, `ml_dex_special_first`로 기록합니다. 이 방식은 서버 데이터팩 적용 이후 새로 잡거나 진화로 등록한 고유 종 기준이며, 데이터팩 설치 이전의 기존 도감 기록은 자동 소급하지 않습니다.

시간 설정 데이터팩은 2026-05-25 `world/datapacks/mingle-time-settings.zip`에 업로드했고 재다운로드 해시 검증을 완료했습니다. 실제 gamerule 반영은 서버 재시작 또는 `/reload` 이후 확인합니다.

Gym party override 데이터팩은 2026-06-03 `world/datapacks/mingle-gym-party-overrides.zip`에 업로드했고 `/reload` 후 enabled datapack 목록에서 확인했습니다. 현재 역할은 CobbleBuilds 8관장 파티를 문서 기준 초급/표준/상급 라인업으로 덮어쓰는 것입니다. 특히 `ice_gym.pryce`의 풀 타입 오매핑과 `steel_gym.jasmine`의 불꽃 타입 오매핑을 교정합니다.

Cobblemon Indigo는 `Cobblemon Pokemon Badges` 모드와 함께 사용합니다. 관장은 자동 배치되지 않으며 OP 권한으로 `/spawnnpc cobblemon:indigo_leader_brock` 같은 명령을 사용해 원하는 위치에 직접 배치합니다. 사천왕 도전은 Indigo 내부 진행 데이터 기준으로 관동 배지 8개가 필요합니다.

2026-05-28 기준 로컬 준비, Git 반영, File Browser 기반 서버 업로드, 업로드 파일 재다운로드 해시 검증을 완료했습니다. 모드 jar 추가는 서버 재시작 전에는 반영되지 않으므로, 사용자가 서버 관리 버튼으로 재시작한 뒤 접속/명령어 테스트를 해야 합니다.

| 업로드 대상 | 로컬 파일 | SHA-256 |
| --- | --- | --- |
| `mods/cobblemonpokemonbadges-fabric-0.1.1.jar` | `work/indigo-20260528/server-upload/mods/cobblemonpokemonbadges-fabric-0.1.1.jar` | `a5011078a804bdff0d299fe2e0e33010c92c976408524d9b0df041030d73f941` |
| `world/datapacks/cobblemon-indigo.zip` | `work/indigo-20260528/server-upload/world/datapacks/cobblemon-indigo.zip` | `8aff092a0009b0a3de79c0652f5a26a067ad8b7941e721b8a5257b1bc1643303` |

확인 명령:

```mcfunction
/datapack list enabled
/spawnnpc cobblemon:indigo_leader_brock
/give <플레이어명> cobblemonpokemonbadges:boulder_badge 1
```

`/give`는 배지 모드 아이템 ID 등록 확인용입니다. 실제 관장 플레이는 NPC 배치 후 전투에서 승리하고 다시 대화해 배지를 받는 흐름입니다.

## 서버 전설 포켓몬 설정

전설/환상 포켓몬은 `Myths and Legends`와 `Limited Legends` 조합으로 관리합니다.

| 항목 | 현재 값 |
| --- | --- |
| 소환 방식 | `MythsAndLegends-Datapack-v1.0.5.zip` 기준 특수 조건/아이템 기반 소환 |
| 소지 제한 파일 | `config/limitedlegends.json` |
| 플레이어별 제한 | `SetLimitsPerPlayer=true`, `MaxLimitedPerPlayer=1` |
| 서버 전체 종 제한 | `SetGlobalLimits=false` |
| 자연 스폰 비활성화 | `DisableSpawning=false` |

서버 전체에서 특정 전설 포켓몬을 1마리만 허용하는 전역 제한은 꺼 두었습니다. 현재 의도는 플레이어마다 전설/환상 포켓몬을 최대 1마리만 보유하게 하는 것입니다.

2026-05-23 재시작 후 실제 접속 테스트에서 서버 접속은 정상으로 확인했습니다. 일반 플레이어 계정에서 `/give @s mythsandlegends:` 입력 시 `mythsandlegends:tidal_bell` 자동완성이 표시되어 Myths and Legends 아이템 ID가 클라이언트/서버에 등록된 것도 확인했습니다. 같은 테스트에서 `/give`는 OP 권한이 없어 차단됐으므로, 강제 지급/강제 소환 테스트는 OP 계정이나 콘솔 권한으로만 진행합니다.

관리자 테스트용 확인 명령:

```mcfunction
/datapack list enabled
/give <플레이어명> mythsandlegends:tidal_bell 1
/give <플레이어명> mythsandlegends:dr_fujis_diary 1
/give <플레이어명> mythsandlegends:azure_flute 1
```

Myths and Legends는 조합 레시피 중심이 아니라 키 아이템과 바이옴/보유 아이템 조건을 Cobblemon 스폰 조건에 추가하는 방식입니다. 예를 들어 `tidal_bell`과 특정 진화석 조건은 일부 전설 조류 스폰 조건에 사용되고, `dr_fujis_diary`는 Mewtwo 조건, `azure_flute`는 Arceus 조건에 사용됩니다.

## 서버 Cobbleloots 설정

직장인 플레이 기준으로 몬스터볼과 회복템 수급이 너무 빡빡하지 않게 보상볼 설정을 올려 두었습니다.

| 설정 | 현재 값 |
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

## 서버 라이딩 설정

안정성을 우선해서 별도 라이딩 모드인 `CobblemonRider`는 제거했습니다. 현재는 Cobblemon `1.7.3`의 기본 라이딩 기능만 사용합니다.

이전 `CobblemonRider` 설정 파일인 `world/pokemonRideConfig.json`은 서버에 남아 있을 수 있지만, 모드가 제거된 상태에서는 라이딩 동작에 사용되지 않습니다.

라이딩 동작은 Cobblemon 기본 데이터와 `Mega Showdown` 호환 범위에 따릅니다. 라이딩 문제가 다시 생기면 추가 라이딩 모드를 넣기보다 기본 Cobblemon 설정/데이터팩 기준으로 조정합니다.

## 로컬 프로필

| 항목 | 값 |
| --- | --- |
| 런처 | Modrinth App |
| 프로필 | `Cobblemon Official Modpack [Fabric]` |
| 프로필 경로 | `/Users/smlee/Library/Application Support/ModrinthApp/profiles/Cobblemon Official Modpack [Fabric]` |
| Minecraft | `1.21.1` |
| Loader | Fabric |
| Java | Modrinth App 내장 Java 21 |

운영 메모: 이 Mac에서 실제 플레이 실행 프로그램은 `Modrinth App`입니다. `Prism Launcher`는 현재 기준 사용하지 않습니다.

## 로컬 설치 모드

현재 로컬 Modrinth 프로필의 `mods` 폴더에는 서버 접속 필수 18개 jar와 선택 지도 모드 2개가 들어 있습니다.

```text
Cobblemon-fabric-1.7.3+1.21.1.jar
accessories-fabric-1.1.0-beta.53+1.21.1.jar
architectury-13.0.8-fabric.jar
capturexp-fabric-1.7.3-1.3.0.jar
cobbleloots-fabric-2.3.0.jar
cobblemon-battle-extras-fabric-1.13.45.jar
cobblemonpokemonbadges-fabric-0.1.1.jar
cobblemon_spawn_alerts-fabric-1.13.2.jar
cloth-config-15.0.140-fabric.jar
emberstextapi-fabric-1.21.1-3.0.0-alpha.2.jar
fabric-api-0.116.12+1.21.1.jar
fabric-language-kotlin-1.13.11+kotlin.2.3.21.jar
inmis-2.8.2-1.21.1.jar
LimitedLegends-fabric-1.9.0.jar
mega_showdown-fabric-1.8.4+1.7.3+1.21.1.jar
MythsAndLegends-fabric-1.9.0.jar
owo-lib-0.13.0-alpha.15+1.21.jar
timcore-fabric-1.7.3-1.31.0.jar
```

선택 지도 모드:

```text
xaerominimap-fabric-1.21.1-25.3.12.jar
xaeroworldmap-fabric-1.21.1-1.40.16.jar
```

`timcore-fabric-1.8.0` 계열은 Cobblemon 1.8 기준이라 이 기준 세팅과 맞지 않아 제거했습니다. `particular`도 `owo-lib` 충돌 때문에 제거했습니다. `CobblemonRider`는 Cobblemon 기본 라이딩 기능과 역할이 겹쳐 안정성 우선 기준으로 제거했습니다.

## 로컬 클라이언트 설정

| 항목 | 현재 값 |
| --- | --- |
| 로컬 전투 애니메이션 속도 | `2.0` |
| 설정 파일 | `config/cobblemon-battle-extras.json` |
| 쉐이더 | 제거 |
| Iris 설정 | `enableShaders=false` |
| shaderPack | 비어 있음 |

쉐이더는 성능 문제 때문에 현재 로컬 프로필에서 뺐습니다. 서버 접속 필수 항목이 아니므로 다른 사람에게도 선택 사항으로 안내합니다.

## 로컬 주요 키 설정

| 행동 | 키 |
| --- | --- |
| 포켓몬 꺼내기/넣기 | `R` |
| 포켓몬 요약/메뉴 | `M` |
| 파티 선택 위/아래 | `Up` / `Down` |
| 파티 UI 숨김 | `O` |
| 전투 로그 | `'` |
| 라이딩 자유 시점 | `Left Alt` |
| 인벤토리 | `E` |
| 채팅 | `T` |

라이딩은 Cobblemon 기본 상호작용 메뉴 기준으로 사용합니다. 포켓몬을 꺼낸 뒤 상호작용 메뉴에 라이딩 선택지가 있는지 확인합니다.

## 로컬 테스트 규칙

관리자가 로컬 접속 테스트를 요청하면 테스트 종료 후 Minecraft 클라이언트를 닫습니다. 다음 테스트에 영향이 없도록 남은 Minecraft/Java 프로세스도 확인합니다.
