# Mingle Lounge 접속 가이드

마지막 갱신: 2026-05-24

이 문서는 새 유저가 `Mingle Lounge` Cobblemon 서버에 접속하기 위해 로컬 Minecraft 클라이언트를 세팅하는 가이드입니다.

## 1. 서버 정보

| 항목 | 값 |
| --- | --- |
| 서버 이름 | `Mingle Lounge` |
| 서버 주소 | 관리자에게 받은 주소 사용 |
| 서버 목록 설명 | `Mingle Lounge` |
| Minecraft | `1.21.1` |
| Loader | Fabric |
| Cobblemon | `1.7.3` |
| 권장 런처 | Modrinth App |
| Java | Java 21 |

서버 주소와 운영 페이지 주소는 공개 문서에 적지 않습니다. 필요한 경우 관리자에게 따로 받습니다.

## 2. 먼저 설치할 것

새 유저는 아래 두 가지가 필요합니다.

```text
Minecraft Java Edition
Modrinth App
```

Modrinth App:

```text
https://modrinth.com/app
```

Modrinth App을 설치한 뒤 Microsoft 계정으로 Minecraft에 로그인합니다.

## 3. 프로필 만들기

Modrinth App에서 새 프로필을 만듭니다.

1. Modrinth App 실행
2. `Browse` 또는 `검색`에서 `Cobblemon Official Modpack` 검색
3. `Cobblemon Official Modpack [Fabric]` 설치
4. Minecraft 버전이 `1.21.1`인지 확인
5. Loader가 Fabric인지 확인

프로필 이름은 알아보기 쉽게 아래처럼 두는 것을 권장합니다.

```text
Mingle Lounge Cobblemon
```

## 4. 필수 모드 확인

서버 접속에는 아래 모드 구성이 필요합니다. Modrinth App의 프로필 화면에서 `Content` 또는 `Mods` 목록을 열어 확인합니다.

이 저장소에는 클라이언트용 모드 파일을 아래처럼 나눠 두었습니다.

```text
client-mods/required  필수 모드 17개
client-mods/optional  선택 모드 2개
```

처음 세팅할 때는 `client-mods/required` 안의 `.jar` 파일 17개를 Modrinth 프로필의 `mods` 폴더에 모두 넣습니다. 선택 모드는 접속 성공을 확인한 뒤 필요할 때 추가합니다.

```text
Cobblemon 1.7.3
Fabric API
Cloth Config API
Cobbleloots
Cobblemon Spawn Alerts
Capture XP
Cobblemon Battle Extras
Mega Showdown
Myths and Legends
Cobblemon: Limited Legends
Inmis
Accessories
Architectury API
Embers Text API
Fabric Language Kotlin
oωo Library
Tim Core
```

파일명 기준으로는 아래 버전과 맞아야 합니다.

```text
Cobblemon-fabric-1.7.3+1.21.1.jar
LimitedLegends-fabric-1.9.0.jar
MythsAndLegends-fabric-1.9.0.jar
accessories-fabric-1.1.0-beta.53+1.21.1.jar
architectury-13.0.8-fabric.jar
capturexp-fabric-1.7.3-1.3.0.jar
cloth-config-15.0.140-fabric.jar
cobbleloots-fabric-2.3.0.jar
cobblemon-battle-extras-fabric-1.13.45.jar
cobblemon_spawn_alerts-fabric-1.13.2.jar
emberstextapi-fabric-1.21.1-3.0.0-alpha.2.jar
fabric-api-0.116.12+1.21.1.jar
fabric-language-kotlin-1.13.11+kotlin.2.3.21.jar
inmis-2.8.2-1.21.1.jar
mega_showdown-fabric-1.8.4+1.7.3+1.21.1.jar
owo-lib-0.13.0-alpha.15+1.21.jar
timcore-fabric-1.7.3-1.31.0.jar
```

위 목록 중 일부가 없으면 Modrinth App의 프로필에서 `Add content`를 눌러 같은 이름의 모드를 추가합니다.

## 5. 첫 접속 세팅에서 제외할 것

현재 서버는 안정성을 우선합니다. 아래 모드는 새 유저 기본 세팅에 넣지 않습니다.

버전이 맞지 않거나 충돌 이력이 있어 설치하지 않는 항목:

```text
CobblemonRider
particular
timcore 1.8.x 계열
Cobblemon 1.8.x 계열
```

개인 선택은 가능하지만 첫 접속 세팅에서는 제외하는 항목:

```text
Iris
Sodium
쉐이더팩
```

쉐이더는 서버 접속에 필수는 아니며 클라이언트 그래픽 선택 사항입니다. 다만 성능 문제나 렌더링 문제가 생기면 원인 분리가 어려우므로, 처음 접속할 때는 제외하고 서버 접속이 정상인 것을 먼저 확인합니다. 쉐이더를 추가한 뒤 문제가 생기면 `Iris`, `Sodium`, 쉐이더팩을 먼저 제거하고 다시 테스트합니다.

## 6. 선택 모드

지도 편의 모드는 선택입니다. 없어도 서버 접속은 됩니다.

권장 선택 모드:

```text
Xaero's Minimap
Xaero's World Map
```

저장소에 포함된 선택 모드 파일:

```text
xaerominimap-fabric-1.21.1-25.3.12.jar
xaeroworldmap-fabric-1.21.1-1.40.16.jar
```

설치할 경우 Minecraft `1.21.1`, Fabric용 파일을 사용합니다. 현재 로컬 테스트 프로필은 필수 모드 17개와 선택 모드 2개를 합쳐 총 19개 모드로 맞춰 두었습니다.

선택 모드는 서버에 설치하지 않는 클라이언트 편의 모드입니다. 접속 문제가 생기면 먼저 `client-mods/optional`에서 복사한 2개를 제거하고 필수 모드 17개만으로 다시 테스트합니다.

`Wiki Cobblemon`은 한글 검색과 검색 버튼 동작이 불안정해서 현재 로컬 테스트 프로필과 기본 안내에서 제외했습니다. 포켓몬 정보 검색은 웹 위키를 사용합니다.

## 7. 실행 설정

Modrinth App 프로필 설정에서 아래를 확인합니다.

| 항목 | 권장 값 |
| --- | --- |
| Minecraft | `1.21.1` |
| Loader | Fabric |
| Java | Java 21 |
| 메모리 | 최소 4GB, 권장 6GB 이상 |

Modrinth App 내장 Java를 쓰면 보통 Java 21이 자동으로 잡힙니다.

## 8. 서버 등록

Minecraft를 실행한 뒤 서버를 등록합니다.

1. `멀티플레이` 선택
2. `서버 추가` 선택
3. 아래 값 입력

```text
서버 이름: Mingle Lounge
서버 주소: 관리자에게 받은 주소
```

4. 저장
5. 서버 목록에서 `Mingle Lounge` 선택 후 접속

서버 목록에서 서버 아래 설명 문구는 서버 설정의 `motd=Mingle Lounge` 기준으로 표시됩니다. Minecraft가 창 제목이나 화면 일부에 표시하는 `제삼자 서버` 문구는 클라이언트 분류명이라 서버 설정으로 바꾸지 못합니다.

## 9. 처음 접속하면

처음 접속하면 스타터 보상을 받을 수 있습니다.

```text
몬스터볼 20개
슈퍼볼 5개
스테이크 30개
포켓몬 도감 1개
Baby Backpack 1개
```

서버는 기본 Minecraft 적대 몬스터가 나오지 않게 설정되어 있습니다. 좀비, 해골 걱정보다는 포켓몬 탐험과 포획에 집중하면 됩니다.

스폰 지점은 포켓몬센터가 있는 마을 근처입니다.

## 10. 기본 조작

| 행동 | 키 |
| --- | --- |
| 인벤토리 | `E` |
| 첫 번째 백팩 열기 | `I` |
| 채팅 | `T` |
| 포켓몬 꺼내기/넣기 | `R` |
| 포켓몬 메뉴 | `M` |
| 파티 선택 | `Up` / `Down` |
| 파티 UI 숨김 | `O` |
| 전투 로그 | `'` |
| 라이딩 자유 시점 | `Left Alt` |

키가 다르면 Minecraft 설정의 `조작` 메뉴에서 Cobblemon 관련 키를 검색해 확인합니다.

## 11. 백팩

서버에는 인벤토리 확장용 `Inmis`가 적용되어 있습니다. 백팩 아이템을 들고 우클릭하면 열 수 있고, 인벤토리에 백팩이 있을 때 `I` 키로 첫 번째 백팩을 열 수 있습니다.

기본 제작 흐름:

```text
Baby Backpack = 가죽 4개 + 상자 1개
Frayed Backpack = 가죽 8개 + 상자 1개
Plated Backpack = Frayed Backpack + 철 주괴 8개
Gilded Backpack = Plated Backpack + 금 주괴 8개
Bejeweled Backpack = Gilded Backpack + 다이아몬드/에메랄드
Ender Pouch = 가죽 8개 + 엔더 상자 1개
```

`Inmis`의 기본 키는 `B`지만, 현재 로컬 테스트 프로필은 핫바 7번 키와 겹치지 않게 `I`로 바꿔 두었습니다. 키가 다르면 Minecraft `Options` -> `Controls`에서 `Inmis` 항목을 검색해 바꿉니다.

백팩 안에 아이템을 넣은 상태로 모드를 제거하면 아이템 접근이 어려워질 수 있습니다. 서버에서 백팩 모드를 제거해야 하는 상황이 생기면 먼저 백팩 안의 아이템을 모두 꺼낸 뒤 진행합니다.

## 12. 전설 포켓몬 콘텐츠

서버에는 `Myths and Legends`와 `Cobblemon: Limited Legends`가 적용되어 있습니다.

| 항목 | 내용 |
| --- | --- |
| 전설 소환 방식 | 특정 키 아이템과 바이옴/아이템 조건을 만족하면 전설/환상 포켓몬 스폰 조건이 열림 |
| 소지 제한 | 플레이어 1인당 전설/환상 포켓몬 최대 1마리 |
| 레시피 확인 | 현재 구성은 조합 레시피 중심이 아니라 키 아이템 조건 중심 |

일반 플레이어는 `/give` 같은 관리자 명령을 사용할 수 없습니다. 관리자 테스트에서는 `mythsandlegends:tidal_bell`, `mythsandlegends:dr_fujis_diary`, `mythsandlegends:azure_flute` 같은 키 아이템 ID가 자동완성되는지 확인해 모드 로딩 상태를 볼 수 있습니다.

## 13. 접속이 안 될 때

먼저 아래를 확인합니다.

```text
Minecraft 버전이 1.21.1인가?
Fabric 프로필인가?
Cobblemon이 1.7.3인가?
필수 모드 17개가 빠지지 않았는가?
선택 모드 2개를 추가했다면 먼저 제거하고 다시 테스트했는가?
Cobblemon 1.8.x용 모드가 섞이지 않았는가?
쉐이더나 그래픽 모드를 추가하지 않았는가?
서버 주소를 관리자에게 받은 값 그대로 입력했는가?
```

자주 나는 문제:

| 증상 | 확인할 것 |
| --- | --- |
| `Incompatible mod set` | 모드 버전 불일치, 특히 `timcore`와 `Cobblemon` 버전 확인 |
| 접속 직후 튕김 | 서버 필수 모드 누락 여부 확인 |
| 화면이 너무 무거움 | 쉐이더, Iris, Sodium 제거 |
| 서버가 안 보임 | 서버 주소와 서버 상태 확인 |

문제가 계속되면 에러 화면의 문구와 `latest.log`를 관리자에게 전달합니다.
