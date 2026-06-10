# Daily Reward Implementation Plan

> **Status:** 이 문서는 2026-06-03에 161 레거시 라인 기준으로 작성하고 실행한 데일리 보상 구현 계획 기록이다. 현재 플레이 기준은 `icecoke-cobblemon-173`이며, 데일리 보상은 아직 173 라인으로 이관 완료된 것으로 보지 않는다. 현재 운영 상태는 [DAILY_REWARD.md](DAILY_REWARD.md)와 [SERVER_CONCEPT.md](SERVER_CONCEPT.md)를 우선한다.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `icecoke-cobblemon` 개인 서버에 서버 실제 날짜 기준 하루 1회 랜덤 데일리 보상을 추가한다.

**Architecture:** 새 서버/클라이언트 모드는 추가하지 않는다. Hermes bridge와 같은 방식으로 별도 Python 프로세스가 `logs/latest.log`의 플레이어 접속 로그를 감지하고, 수령 가능 여부를 서버 로컬 날짜 기준으로 판단한 뒤 Minecraft 콘솔에 `give`, `tellraw` 명령을 보낸다. 기존 `mingle-login-reward` 데이터팩의 랜덤 보상 테이블은 보상 구성 기준으로만 재사용하고, 서버 가동시간 기준 6시간 카운터 방식은 사용하지 않는다.

**Tech Stack:** Minecraft `1.21.1`, Fabric `0.16.14`, Cobblemon `1.6.1`, Python 3 표준 라이브러리, `screen` 세션 `mingle-sample`, remote server `icenux-ms7b23`.

---

## 배경

이전 Mingle Lounge 서버에는 `datapacks/mingle-login-reward`가 있었다. 해당 데이터팩은 서버가 켜져 있던 시간 기준으로 6시간마다 보상을 지급했다.

기존 랜덤 보상 테이블:

| 확률 | 보상 |
| --- | --- |
| 40% | 추가 없음 |
| 25% | `cobblemon:great_ball` 3개 |
| 15% | `cobblemon:exp_candy_xs` 2개 |
| 10% | `cobblemon:exp_candy_xs` 5개 |
| 5% | `cobblemon:revival_herb` 1개 |
| 3% | `cobblemon:ultra_ball` 1개 |
| 2% | `cobblemon:revive` 1개 |

이번 작업에서는 위 랜덤 테이블을 그대로 쓰되, 지급 주기를 `6시간 서버 가동시간`이 아니라 `서버 OS 날짜 기준 하루 1회`로 바꾼다.

## 결정 사항

| 항목 | 결정 |
| --- | --- |
| 수령 방식 | 플레이어 접속 이벤트 감지 후 자동 지급 |
| 시간 기준 | 서버 OS 시간, `Asia/Seoul` 날짜 |
| 지급 제한 | 플레이어별 하루 1회 |
| 확정 보상 | 없음. 사용자가 지정한 랜덤 테이블만 지급 |
| 랜덤 처리 | Python `random.choices`로 weight 기반 선택 |
| 상태 저장 | 서버 루트의 `data/daily-rewards-state.json` |
| 콘솔 입력 | `screen -S mingle-sample -p 0 -X stuff '<command>\r'` |
| 지급 지연 | 접속 로그 감지 후 3초 대기 |
| 이미 수령한 날 | 메시지 없이 조용히 통과 |
| 서버 재시작 | 불필요. 별도 bridge screen 기동으로 적용 |
| 클라이언트 변경 | 없음 |
| 새 모드 추가 | 없음 |

## 제외 범위

- 순수 datapack 기반 실제 날짜 계산.
- 클라이언트 전용 UI 버튼.
- 경제 모드, 상점 모드, 신규 보상 모드 추가.
- 플레이어가 직접 입력하는 수령 방식. 초기는 접속 이벤트를 기준으로 자동 지급한다.
- 이미 받은 날의 반복 안내 메시지. 재접속 때마다 채팅을 어지럽히지 않는다.
- 누락일 보상 적립. 하루를 놓치면 다음 날 1회만 받을 수 있다.

## 파일 구조

| 파일 | 책임 |
| --- | --- |
| `tools/mc_daily_reward_bridge.py` | 접속 로그 감지, 날짜 판정, 랜덤 보상 선택, 콘솔 명령 전송 |
| `tests/test_mc_daily_reward_bridge.py` | 날짜 판정, 상태 저장, 랜덤 선택, 접속 로그 파싱 단위 테스트 |
| `docs/server/DAILY_REWARD.md` | 운영 문서: 사용법, 보상 테이블, 기동/정지/검증 방법 |
| `docs/server/OPS_RUNBOOK.md` | daily reward bridge screen 확인/재기동 명령 추가 |
| `docs/server/MODS_AND_CLIENT.md` | 클라이언트 변경 없음, 새 모드 없음 기록 |
| `docs/server/CHANGELOG.md` | 데일리 보상 작업 기록 |
| 서버 `data/daily-rewards-state.json` | 플레이어별 마지막 수령 날짜 저장. Git에 커밋하지 않음 |

## 상태 파일 형식

`data/daily-rewards-state.json`:

```json
{
  "version": 1,
  "timezone": "Asia/Seoul",
  "players": {
    "Icecokel": {
      "last_claim_date": "2026-06-03",
      "last_claim_at": "2026-06-03T20:30:00+09:00",
      "last_reward": "cobblemon:great_ball 3"
    }
  }
}
```

플레이어 이름은 Minecraft 이름 규칙인 `[A-Za-z0-9_]{1,16}`만 허용한다. UUID 기반 저장은 추후 확장으로 남긴다.

## 보상 명령

| 선택 결과 | 콘솔 명령 | 플레이어 안내 |
| --- | --- | --- |
| 추가 없음 | 없음 | `오늘 데일리 보상: 추가 보상 없음` |
| `great_ball` 3개 | `give <player> cobblemon:great_ball 3` | `오늘 데일리 보상: 슈퍼볼 3개` |
| `exp_candy_xs` 2개 | `give <player> cobblemon:exp_candy_xs 2` | `오늘 데일리 보상: 경험치 사탕 XS 2개` |
| `exp_candy_xs` 5개 | `give <player> cobblemon:exp_candy_xs 5` | `오늘 데일리 보상: 경험치 사탕 XS 5개` |
| `revival_herb` 1개 | `give <player> cobblemon:revival_herb 1` | `오늘 데일리 보상: 부활초 1개` |
| `ultra_ball` 1개 | `give <player> cobblemon:ultra_ball 1` | `오늘 데일리 보상: 하이퍼볼 1개` |
| `revive` 1개 | `give <player> cobblemon:revive 1` | `오늘 데일리 보상: 기력의 조각 1개` |

이미 수령한 경우에는 아무 메시지도 보내지 않는다. 운영자가 수령 상태를 확인해야 할 때는 상태 파일을 직접 조회한다.

접속 직후 플레이어 엔티티가 완전히 준비되지 않았을 수 있으므로, 접속 로그 감지 후 3초 뒤 보상 명령을 보낸다.

## 작업 순서

### Task 1: 단위 테스트 작성

**Files:**
- Create: `tests/test_mc_daily_reward_bridge.py`
- Read: `tools/mc_hermes_bridge.py`

- [ ] **Step 1: 테스트 파일을 만든다**

```python
import random
import unittest
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.mc_daily_reward_bridge import (
    DAILY_REWARDS,
    can_claim,
    choose_reward,
    load_state,
    parse_join,
    record_claim,
    save_state,
)


class DailyRewardBridgeTest(unittest.TestCase):
    def test_parse_join_accepts_player_join_log(self):
        line = "[20:00:00] [Server thread/INFO]: Icecokel joined the game"
        self.assertEqual(parse_join(line), "Icecokel")

    def test_parse_join_ignores_non_join_log(self):
        line = "[20:00:00] [Server thread/INFO]: <Icecokel> hello"
        self.assertIsNone(parse_join(line))


    def test_can_claim_when_player_has_no_record(self):
        state = {"version": 1, "timezone": "Asia/Seoul", "players": {}}
        self.assertTrue(can_claim(state, "Icecokel", "2026-06-03"))


    def test_can_not_claim_twice_on_same_date(self):
        state = {
            "version": 1,
            "timezone": "Asia/Seoul",
            "players": {
                "Icecokel": {
                    "last_claim_date": "2026-06-03",
                    "last_claim_at": "2026-06-03T20:00:00+09:00",
                    "last_reward": "cobblemon:great_ball 3",
                }
            },
        }
        self.assertFalse(can_claim(state, "Icecokel", "2026-06-03"))
        self.assertTrue(can_claim(state, "Icecokel", "2026-06-04"))


    def test_record_claim_updates_state(self):
        state = {"version": 1, "timezone": "Asia/Seoul", "players": {}}
        now = datetime.fromisoformat("2026-06-03T20:00:00+09:00")
        record_claim(state, "Icecokel", "2026-06-03", now, "cobblemon:ultra_ball 1")
        self.assertEqual(state["players"]["Icecokel"]["last_claim_date"], "2026-06-03")
        self.assertEqual(state["players"]["Icecokel"]["last_reward"], "cobblemon:ultra_ball 1")


    def test_state_round_trip(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "daily-rewards-state.json"
            state = {"version": 1, "timezone": "Asia/Seoul", "players": {"Icecokel": {"last_claim_date": "2026-06-03"}}}
            save_state(path, state)
            self.assertEqual(load_state(path)["players"]["Icecokel"]["last_claim_date"], "2026-06-03")


    def test_choose_reward_uses_defined_table(self):
        rng = random.Random(7)
        reward = choose_reward(rng)
        self.assertIn(reward, DAILY_REWARDS)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: 실패를 확인한다**

Run:

```bash
python3 -m unittest tests/test_mc_daily_reward_bridge.py
```

Expected:

```text
ModuleNotFoundError: No module named 'tools.mc_daily_reward_bridge'
```

### Task 2: 데일리 보상 브리지 구현

**Files:**
- Create: `tools/mc_daily_reward_bridge.py`
- Test: `tests/test_mc_daily_reward_bridge.py`

- [ ] **Step 1: `tools/mc_daily_reward_bridge.py`를 만든다**

필수 구현 요소:

```python
DAILY_REWARDS = [
    {"label": "추가 보상 없음", "weight": 40, "item": None, "count": 0, "summary": "none"},
    {"label": "슈퍼볼 3개", "weight": 25, "item": "cobblemon:great_ball", "count": 3, "summary": "cobblemon:great_ball 3"},
    {"label": "경험치 사탕 XS 2개", "weight": 15, "item": "cobblemon:exp_candy_xs", "count": 2, "summary": "cobblemon:exp_candy_xs 2"},
    {"label": "경험치 사탕 XS 5개", "weight": 10, "item": "cobblemon:exp_candy_xs", "count": 5, "summary": "cobblemon:exp_candy_xs 5"},
    {"label": "부활초 1개", "weight": 5, "item": "cobblemon:revival_herb", "count": 1, "summary": "cobblemon:revival_herb 1"},
    {"label": "하이퍼볼 1개", "weight": 3, "item": "cobblemon:ultra_ball", "count": 1, "summary": "cobblemon:ultra_ball 1"},
    {"label": "기력의 조각 1개", "weight": 2, "item": "cobblemon:revive", "count": 1, "summary": "cobblemon:revive 1"},
]
```

필수 함수:

```python
def parse_join(line: str) -> str | None: ...
def load_state(path: Path) -> dict: ...
def save_state(path: Path, state: dict) -> None: ...
def today_kst(now: datetime | None = None) -> tuple[str, datetime]: ...
def can_claim(state: dict, player: str, today: str) -> bool: ...
def record_claim(state: dict, player: str, today: str, now: datetime, reward_summary: str) -> None: ...
def choose_reward(rng: random.Random) -> dict: ...
def send_command(screen_session: str, command: str, dry_run: bool = False) -> None: ...
def grant_daily_if_available(player: str, args: argparse.Namespace, rng: random.Random) -> str | None: ...
def schedule_grant(player: str, args: argparse.Namespace, rng: random.Random) -> None: ...
```

CLI 옵션:

```text
--server-dir /home/icenux/minecraft/mingle-lounge
--screen-session mingle-sample
--state-path data/daily-rewards-state.json
--timezone Asia/Seoul
--join-delay 3
--dry-run
--once-player Icecokel
```

- [ ] **Step 2: 테스트를 실행한다**

Run:

```bash
python3 -m unittest tests/test_mc_daily_reward_bridge.py
```

Expected:

```text
OK
```

- [ ] **Step 3: dry-run으로 콘솔 명령을 확인한다**

Run:

```bash
python3 tools/mc_daily_reward_bridge.py --dry-run --once-player Icecokel
```

Expected:

```text
give Icecokel ...
tellraw Icecokel ...
```

랜덤 결과가 `추가 보상 없음`이면 `give` 없이 `tellraw`만 출력된다.

### Task 3: 서버 업로드와 독립 기동

**Files:**
- Upload: `tools/mc_daily_reward_bridge.py`
- Create on server: `/home/icenux/minecraft/mingle-lounge/data/daily-rewards-state.json` on first run
- No client files

- [ ] **Step 1: 서버에 스크립트를 업로드한다**

Run:

```bash
rsync -av tools/mc_daily_reward_bridge.py icenux-ms7b23:/home/icenux/minecraft/mingle-lounge/tools/
```

Expected:

```text
mc_daily_reward_bridge.py
sent ...
```

- [ ] **Step 2: 서버에서 dry-run을 실행한다**

Run:

```bash
ssh icenux-ms7b23 'cd /home/icenux/minecraft/mingle-lounge && python3 tools/mc_daily_reward_bridge.py --dry-run --once-player Icecokel'
```

Expected:

```text
tellraw Icecokel ...
```

- [ ] **Step 3: 별도 screen으로 기동한다**

Run:

```bash
ssh icenux-ms7b23 'cd /home/icenux/minecraft/mingle-lounge && screen -dmS mc-daily-reward bash -lc "exec python3 tools/mc_daily_reward_bridge.py >> logs/mc-daily-reward.log 2>&1"'
```

Expected:

```bash
ssh icenux-ms7b23 'screen -ls | grep mc-daily-reward'
```

`mc-daily-reward` 세션이 보여야 한다.

### Task 4: 접속 이벤트 검증

**Files:**
- Read: `/home/icenux/minecraft/mingle-lounge/logs/latest.log`
- Read: `/home/icenux/minecraft/mingle-lounge/logs/mc-daily-reward.log`

- [ ] **Step 1: 서버 콘솔 상태를 확인한다**

Run:

```bash
ssh icenux-ms7b23 'screen -ls; ss -ltnp | grep :25565'
```

Expected:

```text
mingle-sample
mc-daily-reward
LISTEN ... :25565
```

- [ ] **Step 2: 인게임에 접속한다**

Expected:

```text
[Daily] 오늘 데일리 보상: ...
```

- [ ] **Step 3: 같은 날 재접속한다**

Expected:

```text
새 데일리 보상 메시지가 다시 나오지 않는다.
```

- [ ] **Step 4: 상태 파일을 확인한다**

Run:

```bash
ssh icenux-ms7b23 'cd /home/icenux/minecraft/mingle-lounge && python3 -m json.tool data/daily-rewards-state.json'
```

Expected:

```json
{
  "version": 1,
  "timezone": "Asia/Seoul",
  "players": {
    "Icecokel": {
      "last_claim_date": "2026-06-03"
    }
  }
}
```

### Task 5: 문서 갱신

**Files:**
- Create: `docs/server/DAILY_REWARD.md`
- Modify: `docs/server/README.md`
- Modify: `docs/server/OPS_RUNBOOK.md`
- Modify: `docs/server/MODS_AND_CLIENT.md`
- Modify: `docs/server/CHANGELOG.md`

- [ ] **Step 1: 운영 문서를 작성한다**

`docs/server/DAILY_REWARD.md`에 아래 내용을 포함한다.

```markdown
# Daily Reward

마지막 갱신: 2026-06-03

서버에 접속하면 서버 실제 날짜 기준 하루 1회 랜덤 데일리 보상을 자동으로 받는다.

## 기준

- 시간대: `Asia/Seoul`
- 저장 파일: `/home/icenux/minecraft/mingle-lounge/data/daily-rewards-state.json`
- 실행 세션: `mc-daily-reward`
- 지급 기점: 플레이어 접속 로그
- 지급 지연: 접속 후 3초
- 이미 수령한 날: 별도 안내 없이 통과
- 서버 재시작: 불필요
- 클라이언트 변경: 없음

## 보상

| 확률 | 보상 |
| --- | --- |
| 40% | 추가 없음 |
| 25% | `cobblemon:great_ball` 3개 |
| 15% | `cobblemon:exp_candy_xs` 2개 |
| 10% | `cobblemon:exp_candy_xs` 5개 |
| 5% | `cobblemon:revival_herb` 1개 |
| 3% | `cobblemon:ultra_ball` 1개 |
| 2% | `cobblemon:revive` 1개 |
```

- [ ] **Step 2: 문서 목록에 `DAILY_REWARD.md`를 추가한다**

`docs/server/README.md` 문서 목록에 추가:

```markdown
| [DAILY_REWARD.md](DAILY_REWARD.md) | 서버 날짜 기준 하루 1회 랜덤 데일리 보상 |
```

- [ ] **Step 3: 서버 문서를 동기화한다**

Run:

```bash
rsync -av --delete /Users/smlee/mingle-lounge/docs/server/ icenux-ms7b23:/home/icenux/minecraft/mingle-lounge/docs/
```

Expected:

```text
DAILY_REWARD.md
DAILY_REWARD_IMPLEMENTATION_PLAN.md
```

### Task 6: 최종 검증

**Files:**
- Read: server logs
- Read: docs hashes

- [ ] **Step 1: 테스트 전체를 다시 실행한다**

Run:

```bash
python3 -m unittest tests/test_mc_daily_reward_bridge.py
```

Expected:

```text
OK
```

- [ ] **Step 2: 서버 프로세스를 확인한다**

Run:

```bash
ssh icenux-ms7b23 'screen -ls; ss -ltnp | grep :25565; ps -ef | grep -E "[m]c_daily_reward_bridge|[j]ava @user_jvm_args"'
```

Expected:

```text
mingle-sample
mc-daily-reward
LISTEN ... :25565
python3 tools/mc_daily_reward_bridge.py
java @user_jvm_args.local.txt -jar fabric-server.jar nogui
```

- [ ] **Step 3: 로컬/서버 문서 해시를 비교한다**

Run:

```bash
find docs/server -maxdepth 1 -type f | sort | xargs sha256sum
ssh icenux-ms7b23 'cd /home/icenux/minecraft/mingle-lounge && find docs -maxdepth 1 -type f | sort | xargs sha256sum'
```

Expected: 같은 파일명의 해시가 모두 일치한다.

## 롤백 계획

브리지 중단:

```bash
ssh icenux-ms7b23 'screen -S mc-daily-reward -X quit'
```

상태 파일 백업 후 제거:

```bash
ssh icenux-ms7b23 'cd /home/icenux/minecraft/mingle-lounge && cp data/daily-rewards-state.json backups/daily-rewards-state-$(date +%Y%m%d-%H%M%S).json && rm data/daily-rewards-state.json'
```

문서 롤백은 Git diff를 확인한 뒤 해당 문서 변경만 되돌린다. 서버 월드 파일은 건드리지 않으므로 월드 백업 복구는 필요 없다.

## 리스크와 대응

| 리스크 | 대응 |
| --- | --- |
| 플레이어 이름 변경 시 새 유저로 취급 | 개인 서버 초기 범위에서는 허용. 필요 시 UUID 기반으로 확장 |
| 인벤토리 가득 참 | `give`는 바닥 드랍될 수 있음. 문서에 안내 |
| bridge 프로세스 종료 | `screen -ls`와 `logs/mc-daily-reward.log`로 확인 후 재기동 |
| 서버 날짜/타임존 오설정 | `date`와 Python `zoneinfo` 결과 확인 |
| 접속 직후 give 실패 | 접속 로그 감지 후 3초 지연 지급 |
| 같은 날 재접속 때 채팅 반복 | 이미 수령한 경우 메시지 없이 통과 |

## 완료 기준

- `python3 -m unittest tests/test_mc_daily_reward_bridge.py` 통과.
- 서버에서 `mc-daily-reward` screen 세션 실행 확인.
- 인게임 첫 접속 시 1회 수령 성공 확인.
- 같은 날짜 재접속 시 추가 지급 없음 확인.
- `data/daily-rewards-state.json`에 마지막 수령 날짜 기록 확인.
- 로컬 `docs/server`와 서버 `/home/icenux/minecraft/mingle-lounge/docs` 동기화 확인.
