# Daily Reward

마지막 갱신: 2026-06-08

이 문서는 `icecoke-cobblemon-161` 레거시 라인의 데일리 보상 운영 기준을 정리한다. 현재 플레이 기준인 `icecoke-cobblemon-173`으로의 이관은 별도 작업이며, 아직 173 라인에서 완료된 것으로 보지 않는다.

## 기준

| 항목 | 값 |
| --- | --- |
| 지급 기점 | 플레이어 접속 로그 |
| 시간 기준 | 서버 OS 시간, `Asia/Seoul` 날짜 |
| 지급 제한 | 플레이어별 하루 1회 |
| 지급 지연 | 접속 로그 감지 후 3초 |
| 이미 수령한 날 | 별도 안내 없이 통과 |
| 실행 세션 | `mc-daily-reward` |
| 상태 파일 | `/home/icenux/minecraft/mingle-lounge/data/daily-rewards-state.json` |
| 서버 재시작 | 불필요 |
| 클라이언트 변경 | 없음 |
| 새 모드 추가 | 없음 |

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

보상이 지급되면 플레이어에게 `[Daily] 오늘 데일리 보상: ...` 메시지를 보낸다. 이미 같은 날짜에 받은 경우에는 재접속해도 메시지를 보내지 않는다.

## 운영 명령

상태 확인:

```bash
ssh icenux-ms7b23 'screen -ls; ps -ef | grep -E "[m]c_daily_reward_bridge|[j]ava @user_jvm_args"'
```

dry-run:

```bash
ssh icenux-ms7b23 'cd /home/icenux/minecraft/mingle-lounge && python3 tools/mc_daily_reward_bridge.py --dry-run --once-player Icecokel'
```

기동:

```bash
ssh icenux-ms7b23 'cd /home/icenux/minecraft/mingle-lounge && screen -dmS mc-daily-reward bash -lc "exec python3 tools/mc_daily_reward_bridge.py >> logs/mc-daily-reward.log 2>&1"'
```

중지:

```bash
ssh icenux-ms7b23 'screen -S mc-daily-reward -X quit'
```

로그 확인:

```bash
ssh icenux-ms7b23 'cd /home/icenux/minecraft/mingle-lounge && tail -n 80 logs/mc-daily-reward.log'
```

상태 파일 확인:

```bash
ssh icenux-ms7b23 'cd /home/icenux/minecraft/mingle-lounge && python3 -m json.tool data/daily-rewards-state.json'
```

## 검증 기준

1. `mc-daily-reward` screen 세션이 실행 중이다.
2. 플레이어가 접속하면 하루 첫 접속에만 보상이 지급된다.
3. 같은 날짜 재접속에서는 추가 보상이 지급되지 않는다.
4. `data/daily-rewards-state.json`에 `last_claim_date`가 기록된다.
5. 서버 재시작 없이 bridge 재기동만으로 기능을 켜고 끌 수 있다.

## 롤백

브리지 중단:

```bash
ssh icenux-ms7b23 'screen -S mc-daily-reward -X quit'
```

상태 파일 백업 후 제거:

```bash
ssh icenux-ms7b23 'cd /home/icenux/minecraft/mingle-lounge && mkdir -p backups && cp data/daily-rewards-state.json backups/daily-rewards-state-$(date +%Y%m%d-%H%M%S).json && rm data/daily-rewards-state.json'
```
