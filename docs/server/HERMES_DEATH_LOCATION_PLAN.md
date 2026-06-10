# Hermes Death Location Plan

마지막 갱신: 2026-06-08

> **Status:** 이 문서는 161 레거시 라인의 Hermes bridge 확장 계획이다. 현재 플레이 기준인 `icecoke-cobblemon-173`에는 Hermes bridge가 아직 이관 완료된 것으로 보지 않으며, 사망 위치 기록 기능도 구현 전이다.

이 문서는 Hermes bridge가 플레이어 사망 위치를 관리자형 답변으로 제공하기 위한 작업 계획을 정리한다. 현재 서버 기본 로그는 사망 원인은 남기지만 사망 좌표를 직접 남기지 않으므로, 구현 전까지는 이 기능을 완료 상태로 보지 않는다.

## 목적

플레이어가 게임 채팅에서 "최근에 어디서 죽었어?", "내 사망 위치 알려줘"처럼 물었을 때 Hermes가 최근 사망 기록과 좌표를 짧게 답하도록 한다.

예상 답변:

```text
최근 사망은 20:19:48, Iron Golem에게 죽은 기록입니다. 마지막 위치 기록 기준 좌표는 -61, 66, -348 근처입니다.
```

## 현재 확인한 한계

서버 로그에는 사망 이벤트가 다음처럼 남는다.

```text
[20:19:48] [Server thread/INFO]: Icecokel was slain by Iron Golem
```

이 기록만으로는 정확한 좌표를 알 수 없다. 접속 로그에는 좌표가 있지만, 사망 시점 좌표와 항상 같다고 볼 수 없다.

```text
[20:16:46] [Server thread/INFO]: Icecokel[/192.168.219.111:58946] logged in with entity id 47 at (-60.96017549649747, 66.0, -348.168370890622)
```

따라서 사망 좌표 답변은 별도 위치 기록을 남긴 뒤 사망 이벤트와 연결해야 한다.

## 안전 기준

- 새 서버 모드를 추가하지 않는다.
- 클라이언트 접속 조건을 바꾸지 않는다.
- 월드 파일, playerdata, region 파일을 수정하지 않는다.
- 서버 전체 재시작 없이 `mc-hermes-bridge` 재기동으로 적용하는 것을 목표로 한다.
- 답변 엔진은 문서, 메모, 사망 기록을 읽기만 한다.
- 서버 변경 명령 실행 기능은 이 계획 범위에 포함하지 않는다.

## 추천 구조

```text
logs/latest.log
  -> tools/mc_hermes_bridge.py
  -> 플레이어 위치 스냅샷 갱신
  -> 사망 로그 감지
  -> data/hermes-deaths.jsonl 기록
  -> Hermes 질문 컨텍스트에 최근 사망 기록 포함
  -> tellraw 응답
```

## 기록 파일

사망 기록 파일:

```text
/home/icenux/minecraft/mingle-lounge/data/hermes-deaths.jsonl
```

예상 JSONL 레코드:

```json
{"at":"2026-06-03T21:20:10+09:00","player":"Icecokel","cause":"was slain by Iron Golem","x":-60.9,"y":66.0,"z":-348.1,"position_source":"last_snapshot"}
```

좌표가 없으면 좌표 필드는 비우고 출처를 `unknown`으로 남긴다.

```json
{"at":"2026-06-03T21:20:10+09:00","player":"Icecokel","cause":"died","position_source":"unknown"}
```

## 작업 계획

1. 현재 Hermes bridge 구조를 확인한다.
   - `tools/mc_hermes_bridge.py`의 `parse_chat`, `follow_log`, `answer_question` 흐름을 기준으로 한다.
   - 기존 메모 저장과 질문 응답 동작은 유지한다.

2. 테스트를 먼저 추가한다.
   - `tests/test_mc_hermes_bridge.py`에 사망 로그 파싱 테스트를 추가한다.
   - 위치 스냅샷 저장/조회 테스트를 추가한다.
   - 사망 이벤트 발생 시 마지막 위치가 death record로 남는 테스트를 추가한다.

3. 사망 로그 파서를 추가한다.
   - `Icecokel died`
   - `Icecokel was slain by Iron Golem`
   - `Icecokel was shot by Skeleton`
   - 그 외 Minecraft 기본 사망 메시지는 확인된 패턴부터 작게 추가한다.

4. 위치 스냅샷 구조를 추가한다.
   - 우선 접속 로그의 `logged in ... at (x, y, z)` 좌표를 파싱해 플레이어별 마지막 위치로 저장한다.
   - 정확도를 높이는 주기적 위치 조회는 별도 옵션으로 둔다.

5. 사망 기록 저장을 추가한다.
   - 사망 로그가 감지되면 현재 플레이어의 마지막 위치 스냅샷과 사망 원인을 `data/hermes-deaths.jsonl`에 append한다.
   - 좌표가 없으면 `position_source`를 `unknown`으로 저장한다.

6. Hermes 질문 컨텍스트를 확장한다.
   - "어디서 죽었어", "사망 위치", "죽은 곳" 같은 질문이면 최근 사망 기록을 프롬프트에 포함한다.
   - 답변에서 정확 좌표와 추정 좌표를 구분하도록 한다.

7. 운영 문서를 갱신한다.
   - `docs/server/HERMES_BRIDGE.md`에 사망 위치 기록 방식과 파일 위치를 추가한다.
   - 이 계획 문서의 완료 여부는 구현과 인게임 확인 뒤에만 변경한다.

8. 검증한다.
   - 로컬 테스트: `python3 -m unittest tests/test_mc_hermes_bridge.py`
   - 서버 dry-run: `python3 tools/mc_hermes_bridge.py --dry-run --engine hermes --once-player Icecokel --once-question '최근에 어디서 죽었어?'`
   - 적용 후 `mc-hermes-bridge`만 재기동한다.
   - 실제 인게임 사망 1회 뒤 질문 응답을 확인한다.

## 운영 상태

현재 상태: 계획 문서화만 완료.

아직 구현되지 않은 항목:

- 사망 로그 파싱
- 위치 스냅샷 저장
- `data/hermes-deaths.jsonl` 기록
- Hermes 사망 위치 질문 컨텍스트
- 인게임 end-to-end 검증
