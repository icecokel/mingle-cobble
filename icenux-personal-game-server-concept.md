# icenux 개인용 게임 서버 컨셉

마지막 갱신: 2026-06-03

이 문서는 `icenux-ms7b23` 머신을 개인용 Minecraft/Cobblemon 게임 서버로 사용할 때의 현재 컨셉과 운영 기준을 정리한다. 현재 버전의 목표는 공개 서버가 아니라 개인 플레이용 서버다.

## 한 줄 정의

`icenux-ms7b23`는 외부 공개를 전제로 하지 않는 개인용 Cobblemon 게임 서버다.

## 현재 목적

- 개인이 안정적으로 접속해 장기 플레이할 수 있는 Minecraft Java 서버를 만든다.
- Cobblemon 중심의 플레이 흐름을 유지한다.
- 새 기능보다 접속 안정성, 월드 보존, 운영 단순성을 우선한다.
- 공개 서버 운영, 커뮤니티 관리, 불특정 다수 접속은 현재 범위에 넣지 않는다.

## 서버 성격

| 항목 | 기준 |
| --- | --- |
| 용도 | 개인용 게임 서버 |
| 공개 여부 | 비공개 |
| 접속 범위 | 우선 LAN 또는 관리자가 허용한 제한된 환경 |
| 운영 방식 | CLI 기반 서버 실행 |
| 우선순위 | 안정성, 백업, 단순한 운영 |
| 확장 가능성 | 나중에 외부 연결 과제로 분리 |

현재 단계에서는 포트포워딩, 도메인 연결, 공개 접속 가이드, 다중 사용자 운영 정책을 필수 조건으로 보지 않는다.

## 기준 게임 버전

초기 기준은 기존 Mingle Lounge Cobblemon 기준이었지만, 2026-06-03 현재 `icenux-ms7b23`에는 샘플팩 `sample/포켓몬 100일 생존 1.21.zip` 기반 서버를 적용했다.

| 항목 | 기준 |
| --- | --- |
| Minecraft | `1.21.1` |
| Loader | Fabric |
| Java | Java 21 |
| 샘플 서버 Fabric Loader | `0.16.14` |
| 샘플 서버 Cobblemon | `1.6.1` |
| 샘플 서버 모드 기준 | `work/sample-server-20260531` 기준에서 보이스챗 제외, 서버 활성 모드 90개 |

`cobblemon-current-settings.md`는 기존 Mingle Lounge 기준 세팅 비교용으로 유지한다. `icenux-ms7b23`의 실제 적용 상태는 이 문서의 "현재 적용 상태"를 우선한다.

## 확인된 머신 상태

2026-06-03 SSH 확인 기준:

| 항목 | 값 |
| --- | --- |
| SSH 별칭 | `icenux-ms7b23` |
| 호스트명 | `icenux-MS-7B23` |
| 사용자 | `icenux` |
| OS | Ubuntu 26.04 LTS |
| CPU | 6 threads |
| 메모리 | 15GiB |
| 디스크 여유 | 약 404GiB |
| Java 21 | `/home/icenux/.local/java/temurin-21-jre`에 사용자 홈 설치 |
| `screen` | 설치됨 |
| `tmux` | 미설치 |
| 25565 포트 바인딩 | 가능 |
| LAN 접속성 | 임시 리스너 기준 확인됨 |
| 공인 IP 접속성 | 현재 범위 아님 |

## 현재 적용 상태

2026-06-03 기준 `icenux-ms7b23`에는 샘플 서버 구성을 적용했다.

| 항목 | 값 |
| --- | --- |
| 서버 디렉터리 | `/home/icenux/minecraft/mingle-lounge` |
| 기준 샘플 | `work/sample-server-20260531` |
| 원본 샘플 ZIP | `sample/포켓몬 100일 생존 1.21.zip` |
| Minecraft | `1.21.1` |
| Fabric Loader | `0.16.14` |
| Cobblemon | `1.6.1` |
| 활성 서버 모드 | 90개 |
| 비활성 서버 모드 | 없음 |
| 서버에서 제외한 모드 | `DistantHorizons-2.2.1-a-1.21.1-neo-fabric.jar`, `voicechat-fabric-1.21.1-2.5.30.jar` |
| Java | `/home/icenux/.local/java/temurin-21-jre/bin/java` |
| 실행 방식 | `screen` 세션 `mingle-sample` |
| 서버 이름/MOTD | `icecoke-cobblemon` |
| 서버 포트 | `25565` |
| 기본 Minecraft 적대 몬스터 | 비활성화, `spawn-monsters=false` |
| 사망 시 아이템/가방 보호 | 활성화, `keepInventory=true` |
| 사망 시 경험치 보호 | 활성화, `keepInventory=true` 기준 |
| 현재 상태 | 클라이언트 접속 준비 후 실행 중 |
| 이전 1.7.3 기준 서버 백업 | `/home/icenux/minecraft/mingle-lounge-pre-sample-20260603-122928` |

기동 검증 결과:

- `Done (3.366s)! For help, type "help"` 로그 확인
- `*:25565` 리슨 확인
- `stop` 명령 후 모든 차원 저장과 정상 종료 확인
- 2026-06-03 클라이언트 접속 준비 후 `screen` 세션 `mingle-sample`로 실행 중
- 로컬 Mac에서 `192.168.219.110:25565` TCP 접속 성공 확인
- 2026-06-03 콘솔에서 `gamerule keepInventory true` 적용 후 `Gamerule keepInventory is currently set to: true` 확인

샘플 서버는 경고 로그가 많지만, 로컬 샘플 서버 기동 기록과 동일하게 부팅을 막지는 않았다. 대표 경고는 클라이언트 전용/선택 호환 mixin 대상 없음, Farmers Delight global loot modifier 경고, 일부 NPC preset 경고다.

## 운영 원칙

1. 개인 서버이므로 공개 접속 편의보다 월드 보존을 우선한다.
2. 서버 구동은 가능한 단순하게 유지한다.
3. 현재는 샘플팩 모드 조합을 기준으로 하며, 기존 `1.7.3` 기준 모드 조합과 섞지 않는다.
4. 서버와 클라이언트의 필수 모드 차이를 만들지 않는다.
5. 월드 파일, 설정 파일, 모드 파일은 변경 전후로 백업한다.
6. 서버 주소나 접속 조건이 바뀌면 접속 문서도 함께 갱신한다.

관장 콘텐츠의 타입, 바이옴, 동적 난이도 방향은 [관장 컨셉 문서](/Users/smlee/mingle-lounge/icenux-gym-leader-concept.md)를 기준으로 별도 관리한다.

## 운영 형태

초기 운영은 다음 형태를 목표로 한다.

- `icenux` 사용자 홈 아래에 서버 디렉터리를 둔다.
- Java 21 런타임과 Fabric 서버 파일을 명확히 분리한다.
- `screen`으로 서버 콘솔 세션을 유지한다.
- 서버 시작 스크립트와 JVM 메모리 값을 문서화한다.
- 백업은 자동화 전까지 수동 백업 기준을 둔다.

시스템 서비스 등록, 자동 재시작, 원격 관리 UI는 초기 필수 범위가 아니다.

현재 사용 명령:

```bash
ssh icenux-ms7b23
cd ~/minecraft/mingle-lounge
./start-screen.sh
./attach.sh
./stop.sh
```

LAN 접속 주소는 `192.168.219.110:25565`이다. 외부 공개 접속은 현재 범위가 아니다.

## 로컬 클라이언트 프로필

이 Mac에는 Modrinth App 프로필 `icecoke-cobblemon`이 준비되어 있다.

| 항목 | 값 |
| --- | --- |
| 프로필 경로 | `/Users/smlee/Library/Application Support/ModrinthApp/profiles/icecoke-cobblemon` |
| 기준 클라이언트 | `work/sample-client-profile-20260531` |
| Minecraft | `1.21.1` |
| Fabric Loader | `0.16.14` |
| 클라이언트 활성 모드 | 101개 |
| 제거한 클라이언트 모드 | 6개, `DistantHorizons-2.2.1-a-1.21.1-neo-fabric.jar`, `hdskins-6.14.3+1.21.1.jar`, `iris-fabric-1.8.8+mc1.21.1.jar`, `replaymod-1.21-2.6.19.jar`, `sound-physics-remastered-fabric-1.21.1-1.4.12.jar`, `voicechat-fabric-1.21.1-2.5.30.jar` |
| 서버 목록 | `icecoke-cobblemon` -> `192.168.219.110:25565` |

`servers.dat`를 생성해 멀티플레이 서버 목록에 `icecoke-cobblemon`을 등록했다.

방송, 녹화, 보이스챗, 쉐이더, 선택 그래픽/사운드 연출 모드는 개인 플레이 기준에서 제거했다. `Exposure`, `Exposure Polaroid`, `More Cobblemon Move Animations`는 서버에도 포함된 공통 모드라 접속 안정성을 위해 이번 정리에서는 유지한다.

## 기존 Mingle Lounge 서버와의 관계

이 서버는 기존 Mingle Lounge 서버 환경을 즉시 대체하는 목적이 아니다. 기존 서버의 안정화된 버전, 모드 구성, 데이터팩 기준은 참고하되, `icenux-ms7b23`의 현재 컨셉은 개인용 게임 서버로 둔다.

따라서 다음 항목은 이전 또는 공개 전환을 결정하기 전까지 별도 과제로 남긴다.

- 기존 운영 월드 이전
- 기존 접속 주소 변경
- 도메인 연결
- 외부 접속 포트포워딩
- 공개 접속 가이드 작성
- 다중 사용자 운영 정책
- 장기 자동 백업과 복구 절차

## 현재 제외 범위

다음은 현재 버전의 컨셉에서 제외한다.

- 공개 서버 런칭
- 불특정 다수 접속 허용
- 서버 홍보 페이지 구성
- 관리자 웹 패널 구축
- 새 경제/상점 모드 추가
- 안정성 검증 없는 대규모 모드 변경

## 다음 과제

샘플 서버 적용 이후 남은 과제는 아래 순서로 본다.

1. 샘플 클라이언트 프로필을 준비한다.
2. LAN에서 `192.168.219.110:25565` 접속 테스트를 한다.
3. 접속 테스트 후 서버를 계속 켜 둘지, 필요할 때만 켤지 정한다.
4. 월드 백업 위치와 수동 백업 명령을 정한다.
5. 필요하면 `crontab @reboot` 또는 `systemd --user` 기반 자동 시작을 별도 과제로 검토한다.

외부 연결은 개인용 서버 구축이 안정화된 뒤 별도 과제로 판단한다.
