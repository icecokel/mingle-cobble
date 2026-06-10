# Cobblemon 173 Local Profile

마지막 갱신: 2026-06-08

이 문서는 이 Mac의 현재 173 로컬 Modrinth 프로필 `icecoke-cobblemon-173`과 173 서버 라인 접속 조건을 기록한다. 기존 `icecoke-cobblemon` 1.6.1 프로필은 161 레거시 라인용으로 보존한다.

## 목표

1. 현재 플레이용 173 프로필 `icecoke-cobblemon-173`을 기준으로 둔다.
2. 기존 `icecoke-cobblemon` 1.6.1 로컬 프로필을 161 레거시 라인용으로 보존한다.
3. 173 라인 `192.168.219.110:25566` 접속 조건을 문서화한다.
4. 클라이언트/서버 모드 불일치, 리소스팩 문제, 인게임 기능 오류를 분리해서 기록한다.

## 전제

| 항목 | 값 |
| --- | --- |
| 161 레거시 클라이언트 프로필 | `/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon` |
| 1.7.3 원본 기준 프로필 | `/Users/smlee/Library/Application Support/ModrinthApp/profiles/Cobblemon Official Modpack [Fabric]` |
| 173 프로필명 | `icecoke-cobblemon-173` |
| 173 프로필 경로 | `/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon-173` |
| 173 라인 | `192.168.219.110:25566` |
| 173 라인 screen | `icecoke-173` |
| 173 라인 Cobblemon | `1.7.3+1.21.1` |
| 173 라인 Fabric Loader | `0.17.3` |

## 금지 사항

- 기존 `icecoke-cobblemon` 1.6.1 프로필의 `mods/`, `options.txt`, `resourcepacks/`, `servers.dat`를 173 작업 중 직접 수정하지 않는다.
- 1.7.3 173 프로필로 161 레거시 서버 `192.168.219.110:25565`에 접속하지 않는다.
- 1.6.1 운영 프로필로 173 라인 `192.168.219.110:25566`에 접속하지 않는다.
- 173 라인에서 확인된 문제가 161 레거시 라인에도 반영됐다고 단정하지 않는다.

## 프로필 구성 전략

권장 시작점은 `Cobblemon Official Modpack [Fabric]` 프로필 복사본이다. 이 프로필은 이미 `Cobblemon 1.7.3`, `Mega Showdown 1.7.3` 계열, `Cobblemon Spawn Alerts 1.13.2`를 포함한다.

173 라인은 공식 1.7.3 프로필의 20개 모드에 운영 월드 로딩용 모드와 현재 적용한 gameplay 모드를 더한 상태다. 초기 로컬 클라이언트 검증은 두 단계로 나눠 진행했다.

1. **최소 접속 테스트**: 공식 1.7.3 프로필 복사본으로 실행한다. 접속 실패 시 서버가 요구하는 missing mod를 로그에서 확인한다.
2. **서버 parity 테스트**: 접속 실패 또는 월드 렌더링 오류가 있으면 서버 173 라인에 추가한 월드젠/블록 모드를 클라이언트 173 프로필에도 추가한다.

서버 173 라인에 추가된 월드젠/블록 의존 모드:

```text
Terralith_1.21.x_v2.5.8.jar
TerraBlender-fabric-1.21.1-4.1.0.8.jar
lithostitched-fabric-1.21.1-1.4.8.jar
Oh-The-Trees-Youll-Grow-fabric-1.21.1-5.0.14.jar
Woodlands_Extra-Universal-1.21.1-v1.3.3.jar
Woodlands_Vanilla-Universal-1.21.1-v1.2.2.jar
LegendaryMonuments-5.1.jar
chipped-fabric-1.21.1-4.0.2.jar
resourcefullib-fabric-1.21-3.0.12.jar
athena-fabric-1.21-4.0.1.jar
CobbleFurnies-fabric-0.5.jar
geckolib-fabric-1.21.1-4.7.6.jar
trinkets-3.10.0.jar
```

`cobblemon-unimplementeditems-1.6-fabric-1.1.0.jar`는 metadata 기준 `cobblemon <=1.7.0`이므로 1.7.3 클라이언트에 넣지 않는다.

## 테스트 절차

### 1. 서버 사전 확인

```bash
ssh icenux-ms7b23 'screen -ls; ss -ltnp | grep 25566'
nc -vz -G 3 192.168.219.110 25566
```

통과 기준:

- `icecoke-173` screen이 있다.
- `25566` 포트가 Java 프로세스로 listen 중이다.
- 로컬 Mac에서 TCP 접속이 성공한다.

### 2. 173 프로필 생성

1. Modrinth App에서 `Cobblemon Official Modpack [Fabric]` 프로필을 복제한다.
2. 복제한 프로필 이름을 `icecoke-cobblemon-173`로 둔다.
3. 서버 목록에 `icecoke-cobblemon-173 -> 192.168.219.110:25566`만 추가한다.
4. 언어는 `ko_kr`로 둔다.

CLI로 검증할 파일:

```text
/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon-173/options.txt
/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon-173/mods/
```

### 3. 클라이언트 실행 전 정적 검사

확인 항목:

- Fabric Loader가 `0.17.3` 이상인지 확인한다.
- `Cobblemon-fabric-1.7.3+1.21.1.jar`가 있는지 확인한다.
- `Cobblemon-fabric-1.6.1+1.21.1.jar`가 섞여 있지 않은지 확인한다.
- `cobblemon_spawn_alerts-fabric-1.13.2.jar`가 있으면 1.7.3용으로 본다.
- `cobblemon_spawn_alerts-fabric-1.6.1.jar`가 섞여 있으면 실패로 본다.

### 4. 클라이언트 기동 테스트

Modrinth App에서 `icecoke-cobblemon-173`를 실행한다.

통과 기준:

- 메인 메뉴까지 진입한다.
- 클라이언트가 crash report를 만들지 않는다.
- `latest.log`에 `Incompatible mods found`, `Mod resolution failed`, `Mixin apply failed`가 없다.

실패 시 분류:

| 증상 | 판단 |
| --- | --- |
| Mod resolution failed | 모드 버전/의존성 불일치 |
| Mixin apply failed | 클라이언트 전용 모드 충돌 가능성 |
| Missing required mod | 서버 또는 클라이언트 필수 모드 불일치 |
| Resource reload failed | 리소스팩/언어팩 충돌 가능성 |

### 5. 서버 접속 테스트

`192.168.219.110:25566`에 접속한다.

통과 기준:

- 서버 목록에서 ping이 표시된다.
- 접속 후 월드 로딩이 완료된다.
- 플레이어가 월드에 스폰된다.
- 서버 로그에 `joined the game`과 `left the game`이 정상 기록된다.

실패 시 확인:

```bash
tail -n 120 "/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon-173/logs/latest.log"
ssh icenux-ms7b23 'tail -n 120 /home/icenux/minecraft/icecoke-cobblemon-173-test/logs/latest.log'
```

### 6. 인게임 기능 체크

접속 성공 후 아래를 짧게 확인한다.

| 항목 | 확인 방법 | 통과 기준 |
| --- | --- | --- |
| 플레이어 데이터 | 접속 직후 인벤토리/위치 확인 | crash 없이 로딩 |
| 포켓몬 파티 | Cobblemon 파티 UI 확인 | 파티 표시 또는 빈 상태가 정상 표시 |
| PC | 가까운 PC 또는 명령/아이템으로 확인 | UI 열림 |
| 야생 포켓몬 | 주변 탐색 또는 서버 명령으로 확인 | 모델/텍스처 깨짐 없음 |
| 포획 | 낮은 위험 포켓몬 1회 포획 | 배틀/포획 루프 정상 |
| 배틀 | 야생 또는 테스트 대상과 전투 | 턴 진행 정상 |
| 지도 | Xaero 미니맵/월드맵 열기 | crash 없음 |
| 스폰 알림 | 서버 로그/인게임 알림 관찰 | crash 없음, 메시지 표시 |

### 7. 관장/배지 회귀 체크

관장 기능은 운영 핵심이므로 별도 체크한다.

1. 기존 gym marker 근처로 이동한다.
2. NPC가 생성되는지 확인한다.
3. 관장 또는 일반 트레이너와 상호작용한다.
4. 전투가 시작되는지 확인한다.
5. 승리 후 배지/재도전 상태가 기록되는지 확인한다.

주의:

- 1.7.3 173 라인에는 `easy_npc`, `cobblebuilds-leaders`, `badgebox` 운영 조합이 완전히 반영된 상태가 아니다.
- `pokenpc` 명령은 현재 173 라인 콘솔 help에서 unknown으로 확인됐다.
- 관장 기능은 접속 테스트 통과 후 별도 migration 과제로 다룬다.

## 성공 판정

### 1차 성공

- 클라이언트가 기동한다.
- 서버 목록에서 `192.168.219.110:25566` ping이 된다.
- 173 라인에 접속해 월드에 들어간다.
- 5분 이상 crash 없이 이동 가능하다.

### 2차 성공

- 포켓몬 표시, 전투, 포획, PC가 정상이다.
- 지도와 스폰 알림이 crash 없이 동작한다.
- 서버 로그에 새 fatal error가 없다.

### 173 라인 잔여 검토

아래는 173 라인을 장기 운영 기준으로 더 굳히기 전에 확인한다.

- 관장/배지 시스템의 대체 또는 호환성 확인
- `LegendaryMonuments` loot table 오류 처리
- `unimplemented_items` 잔여 아이템 처리
- 1.7.3 클라이언트 프로필 고정
- 운영 월드 백업/롤백 계획 작성

## 2026-06-07 실행 결과

### 수행 범위

- 기존 운영 프로필 `icecoke-cobblemon`은 수정하지 않았다.
- 새 로컬 173 프로필 `/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon-173`를 만들었다.
- 173 라인 항목 `icecoke-cobblemon-173 -> 192.168.219.110:25566`을 추가했다.
- `options.txt` 언어 설정은 `ko_kr`로 유지했다.
- Modrinth App DB는 수정 전 `app.db.backup-icecoke-173-*`로 백업했다.

### 1차 최소 접속 테스트

공식 `Cobblemon Official Modpack [Fabric]` 복사본의 20개 모드만으로 클라이언트 기동은 성공했다. 서버 자동 접속도 시도됐지만, 서버 월드에 있는 블록/데이터 컴포넌트가 클라이언트 registry에 없어 접속 직후 disconnect됐다.

대표 증상:

```text
Registry entry (cobblefurnies:*) is missing from local registry (minecraft:block)
Registry entry (legendarymonuments:*) is missing from local registry (minecraft:block)
Registry entry (geckolib:stack_animatable_id) is missing from local registry (minecraft:data_component_type)
Registry entry (trinkets:attribute_modifiers) is missing from local registry (minecraft:data_component_type)
```

판정: 최소 공식 프로필만으로는 현재 173 라인 접속 불가.

### 2차 서버 parity 테스트

173 프로필에 서버 173 라인과 같은 월드젠/블록 의존 모드 13개를 추가해 총 33개 모드로 맞췄다.

추가한 모드:

```text
Terralith_1.21.x_v2.5.8.jar
TerraBlender-fabric-1.21.1-4.1.0.8.jar
lithostitched-fabric-1.21.1-1.4.8.jar
Oh-The-Trees-Youll-Grow-fabric-1.21.1-5.0.14.jar
Woodlands_Extra-Universal-1.21.1-v1.3.3.jar
Woodlands_Vanilla-Universal-1.21.1-v1.2.2.jar
LegendaryMonuments-5.1.jar
chipped-fabric-1.21.1-4.0.2.jar
resourcefullib-fabric-1.21-3.0.12.jar
athena-fabric-1.21-4.0.1.jar
CobbleFurnies-fabric-0.5.jar
geckolib-fabric-1.21.1-4.7.6.jar
trinkets-3.10.0.jar
```

검증 결과:

```text
클라이언트 프로필: icecoke-cobblemon-173
클라이언트 모드 수: 33
서버 접속 결과: 성공
접속 서버: 192.168.219.110:25566
서버 로그: Icecokel joined the game
접속 유지: 약 1분 동안 즉시 disconnect 없음
테스트 종료: 클라이언트 종료 후 서버 list 기준 0/2명
```

서버 로그 확인:

```text
Icecokel logged in with entity id 46 at (-35.25142008002707, 71.0, -250.31910350666342)
Icecokel joined the game
Icecokel left the game
There are 0 of a max of 2 players online:
```

판정: 1.7.3 테스트 클라이언트는 서버 parity 33개 모드 구성에서 173 라인 접속까지 성공했다.

### 남은 확인

- 인게임 이동, 포켓몬 파티 UI, PC, 전투, 포획은 아직 미검증이다.
- 관장/배지/레벨캡 기능은 아직 미검증이다.
- `LegendaryMonuments` loot table 오류와 Cobblemon spawn preset 경고는 서버 로그 이슈로 남아 있다.
- 운영 서버 1.7.3 전환 여부는 위 인게임 기능 검증 전에는 결정하지 않는다.

## 2026-06-07 추가 인게임 검증 결과

### 통과

```text
테스트 일시: 2026-06-07 16:40~16:47 KST
클라이언트 프로필: icecoke-cobblemon-173
클라이언트 모드 수: 33
서버 접속 결과: 성공
접속 유지: 16:40:29 joined, 16:46:26 list 기준 온라인, 5분 이상 유지
테스트 종료: 16:47:11 disconnect, 16:47:14 list 기준 0/2명
```

확인한 항목:

| 항목 | 결과 | 근거 |
| --- | --- | --- |
| 월드 진입 | 통과 | 클라이언트 화면에서 월드 렌더링 확인 |
| 접속 유지 | 통과 | 서버 `list` 기준 5분 이상 `Icecokel` 온라인 |
| 플레이어 데이터 | 부분 통과 | 위치 `[-35.2514, 71.0, -250.3191]`, 기존 파티 표시 확인 |
| 포켓몬 파티 UI | 통과 | `M` 키로 Cobblemon 파티/상세 UI 열림 |
| PC UI | 통과 | `execute as Icecokel run pc`로 박스 UI 열림 |
| 주변 포켓몬 모델 | 통과 | `Skiddo` 엔티티 조회 및 화면 렌더링 확인 |
| 미니맵 | 부분 통과 | 우측 상단 미니맵 표시 확인 |

주의:

- 주변 포켓몬 확인 중 `execute at Icecokel run tp @e[type=cobblemon:pokemon,limit=1,sort=nearest] ~ ~ ~` 명령이 실행되어 173 라인 월드의 `Skiddo` 1마리가 플레이어 위치로 이동했다. 운영 서버에는 영향이 없다.
- `M` 키는 Xaero World Map이 아니라 Cobblemon 파티 UI로 동작했다. 월드맵 전체 화면 UI는 이번 자동 검증에서 확인하지 못했다.

### 확인 필요

| 항목 | 이유 |
| --- | --- |
| 관장/배지 | gym 위치 이동, NPC 생성, 상호작용, 승리 판정이 필요함 |
| 스폰 알림 | 테스트 중 알림 발생 조건을 만들지 못함 |
| 월드맵 전체 화면 | 키 바인딩 충돌로 `M`이 Cobblemon UI를 열어 별도 키 확인 필요 |

### 사용자 확인으로 추가 통과

2026-06-07 사용자가 173 라인에서 아래 항목을 직접 성공 확인했다.

| 항목 | 결과 | 근거 |
| --- | --- | --- |
| 전투 | 통과 | 사용자 인게임 확인 |
| 포획 | 통과 | 사용자 인게임 확인 |

### 로그에서 남은 이슈

클라이언트 로그:

- `No data fixer registered for ...`가 다수 출력된다. 이번 테스트에서는 fatal crash로 이어지지 않았다.
- `cobblemon:textures/particle/.../LICENSE` invalid path 경고가 다수 출력된다. 리소스팩 경고로 보이며 이번 테스트에서는 접속 유지에 영향 없음.
- `xaerominimap:lang/ko_kr.json`, `cobblemon:lang/ko_kr.json` language file parse 경고가 있다. 한국어 일부 문구가 누락/영어 표시될 수 있다.
- `cobblemon:relic_coin_pouch` missing texture 경고가 있다.
- 일부 `cobblemon:animation.*` soundEvent 경고가 있다.

서버 로그:

- 운영 월드에서 173 라인에 없는 `farmersdelight:*`, `cobblecuisine:*` 블록/레시피 참조가 recoverable error로 남아 있다.
- 현재는 기본값으로 대체되며 접속 유지에는 실패하지 않았지만, 운영 이전 전에는 world/data cleanup 또는 모드 parity 결정을 해야 한다.

## 결과 기록 양식

```text
테스트 일시:
클라이언트 프로필:
클라이언트 모드 수:
서버 접속 결과:
접속 시간:
확인한 기능:
클라이언트 latest.log 주요 오류:
서버 latest.log 주요 오류:
판정:
다음 조치:
```
