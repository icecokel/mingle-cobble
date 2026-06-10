# Ops Runbook

마지막 갱신: 2026-06-11

이 문서는 `icecoke-cobblemon` 서버 작업 시 사용하는 기본 명령과 점검 절차를 정리한다. 현재 플레이 기준은 173 라인이고, 161 라인은 레거시 보존 라인이다.

## 서버 라인

| 항목 | 173 현재 라인 | 161 레거시 라인 |
| --- | --- | --- |
| 서버 경로 | `/home/icenux/minecraft/icecoke-cobblemon-173-test` | `/home/icenux/minecraft/mingle-lounge` |
| screen | `icecoke-173` | `mingle-sample` |
| 포트 | `25566` | `25565` |
| MOTD | `icecoke-cobblemon-173` | `icecoke-cobblemon-161` |
| 용도 | 현재 플레이/검증 | 보존, 비교, 롤백 참고 |

173 서버 경로의 `-test`는 과거 인스턴스 이름이다. 안정성을 위해 디렉터리는 이동하지 않고, 표시명과 운영 명칭만 `icecoke-cobblemon-173`으로 사용한다.

## 접속

```bash
ssh icenux-ms7b23
cd ~/minecraft/icecoke-cobblemon-173-test
```

161 레거시 라인을 확인할 때만 아래 경로를 쓴다.

```bash
cd ~/minecraft/mingle-lounge
```

## 기본 스크립트

```bash
./start-screen.sh
./attach.sh
./stop.sh
```

현재 실행 방식은 `screen` 세션 유지다. 173 라인은 `icecoke-173`, 161 레거시는 `mingle-sample` 세션을 쓴다.

주의:

- `./stop.sh`는 서버 정지 작업이다.
- 관장 배치나 문서 동기화 중에는 사용자가 명시적으로 요청하지 않는 한 실행하지 않는다.
- 월드 복구나 서버 정지가 필요한 작업은 고위험 작업으로 보고, 백업 확인과 재기동 후 검증 전까지 완료로 말하지 않는다.

| 항목 | 값 |
| --- | --- |
| screen 세션 | `mingle-sample` |
| 서버 디렉터리 | `/home/icenux/minecraft/mingle-lounge` |
| Java | `/home/icenux/.local/java/temurin-21-jre/bin/java` |
| 서버 포트 | `25565` |
| Hermes bridge 세션 | `mc-hermes-bridge` |
| Daily reward 세션 | `mc-daily-reward` |
| 정기 월드 백업 | 아래 정기 월드 백업 섹션의 173 라인 `cron`, 매일 19:00 KST |

위 표의 bridge 항목은 161 레거시 라인의 보조 프로세스 기준이다. 정기 월드 백업은 현재 173 라인만 대상으로 한다.

## 현재 상태 확인

```bash
screen -ls
ss -ltnp | grep -E '25565|25566'
grep -nE '^(motd|server-port|server-ip|max-players|spawn-monsters|spawn-animals|spawn-npcs)=' server.properties
tail -n 80 logs/latest.log
```

173 라인 빠른 확인:

```bash
cd /home/icenux/minecraft/icecoke-cobblemon-173-test
grep -nE '^(motd|server-port|max-players)=' server.properties
screen -S icecoke-173 -p 0 -X stuff $'list\r'
tail -n 80 logs/latest.log
```

161 레거시 라인 빠른 확인:

```bash
cd /home/icenux/minecraft/mingle-lounge
grep -nE '^(motd|server-port|max-players)=' server.properties
screen -S mingle-sample -p 0 -X stuff $'list\r'
tail -n 80 logs/latest.log
```

보조 브리지 확인:

```bash
screen -ls
ps -ef | grep -E '[m]c_hermes_bridge|[m]c_daily_reward_bridge'
tail -n 80 logs/mc-hermes-bridge.log
tail -n 80 logs/mc-daily-reward.log
```

로컬 Mac에서 포트 확인:

```bash
nc -vz -G 3 192.168.219.110 25566
nc -vz -G 3 192.168.219.110 25565
```

## 서버 작업 기록

서버 파일, 설정, 모드, 데이터팩, 월드, 재시작, 접속 조건, 운영 문서를 변경했으면 `docs/server/CHANGELOG.md`에 작업 기록을 남긴다. 기본 항목은 아래와 같다.

```markdown
- 요청:
- 목표:
- 작업내용:
- 기대작용:
- 특이사항:
```

필요하면 아래 항목도 같은 기록에 붙인다.

```markdown
- 백업:
- 검증:
- 재시작:
- 클라이언트 영향:
- 확인 필요:
```

작업 전 예상과 실제 수행 결과가 다르면, 최종 기록은 실제 수행한 내용과 남은 확인 필요 사항을 기준으로 고친다.

## 콘솔 명령 입력

서버 콘솔 명령은 Minecraft 채팅 명령과 달리 앞에 `/`를 붙이지 않는다.

원격에서 한 번에 입력:

```bash
ssh icenux-ms7b23 'bash -s' <<'REMOTE'
cd "$HOME/minecraft/mingle-lounge"
screen -S mingle-sample -p 0 -X stuff $'list\r'
REMOTE
```

예시:

```bash
screen -S mingle-sample -p 0 -X stuff $'gamerule keepInventory\r'
screen -S mingle-sample -p 0 -X stuff $'give Icecokel minecraft:diamond 1\r'
screen -S mingle-sample -p 0 -X stuff $'say maintenance check\r'
```

## 현재 중요 gamerule

```mcfunction
gamerule keepInventory true
```

이 설정은 재시작 없이 즉시 적용된다. 사망 시 인벤토리, 가방, 경험치를 보호한다.

## 재시작 판단

재시작이 필요한 작업:

- 서버 jar 또는 `mods/` 변경
- 일부 config 변경
- `config/rctmod-server.toml`의 `initialLevelCap`, `maxLevelDiff`, `forceBattleMaxLevelDiff` 같은 RCTMod 진행/트레이너 레벨 설정 변경
- `server.properties` 중 서버 시작 시 읽는 설정 변경

재시작이 필요 없는 작업:

- `gamerule` 변경
- 콘솔 `give`, `say`, `list`
- 문서 복사
- `mc-daily-reward`, `mc-hermes-bridge` 같은 별도 bridge 프로세스 재기동

## 데일리 보상 브리지

데일리 보상은 플레이어 접속 로그를 감지해 서버 날짜 기준 하루 1회 랜덤 보상을 지급한다. 서버/클라이언트 모드 변경 없이 별도 `screen` 세션으로 실행한다.

기동:

```bash
cd /home/icenux/minecraft/mingle-lounge
screen -dmS mc-daily-reward bash -lc 'exec python3 tools/mc_daily_reward_bridge.py >> logs/mc-daily-reward.log 2>&1'
```

중지:

```bash
screen -S mc-daily-reward -X quit
```

dry-run:

```bash
cd /home/icenux/minecraft/mingle-lounge
python3 tools/mc_daily_reward_bridge.py --dry-run --once-player Icecokel
```

상태 파일:

```bash
/home/icenux/minecraft/mingle-lounge/data/daily-rewards-state.json
```

## 백업 원칙

- 월드 파일을 건드리기 전에는 `world/` 백업을 먼저 만든다.
- NPC나 구조물을 배치하기 전에도 최소한 좌표와 변경 목적을 기록한다.
- `.mca`, `level.dat`, `playerdata` 직접 교체는 고위험 작업으로 본다.

## 정기 월드 백업

정기 백업은 서버 사용자 crontab에서 매일 19:00 KST에 실행한다. 현재 정기 백업 대상은 173 라인의 `world/`만이며, `.sha256` 검증 파일을 함께 만든다. 161 레거시 라인은 자동 정기 백업 대상에서 제외한다.

```cron
0 19 * * * cd /home/icenux/minecraft/icecoke-cobblemon-173-test && /home/icenux/minecraft/icecoke-cobblemon-173-test/tools/mc_world_backup.sh >> /home/icenux/minecraft/icecoke-cobblemon-173-test/logs/mc-world-backup-cron.log 2>&1
```

백업 스크립트:

```bash
/home/icenux/minecraft/icecoke-cobblemon-173-test/tools/mc_world_backup.sh
```

동작:

1. 중복 실행 방지를 위해 `flock`으로 lock을 잡는다.
2. `icecoke-173` screen 세션이 있으면 `save-off` 후 `save-all flush`를 보낸다.
3. `backups/world-auto-backup-YYYYMMDD-HHMMSS.tar.gz`를 만든다.
4. tar 생성 후 `save-on`을 보내 서버 저장을 다시 켠다.
5. `sha256sum -c`로 생성된 백업을 검증한다.

수동 검증:

```bash
cd /home/icenux/minecraft/icecoke-cobblemon-173-test
crontab -l
tail -n 80 logs/mc-world-backup-cron.log
ls -lh backups/world-auto-backup-*.tar.gz | tail
sha256sum -c backups/world-auto-backup-YYYYMMDD-HHMMSS.tar.gz.sha256
```

## 문서 동기화

로컬 원본:

```bash
/Users/smlee/mingle-lounge/docs/server
```

서버 사본:

```bash
/home/icenux/minecraft/mingle-lounge/docs
```

동기화는 로컬에서 진행한다.

```bash
rsync -av --delete /Users/smlee/mingle-lounge/docs/server/ icenux-ms7b23:/home/icenux/minecraft/mingle-lounge/docs/
```
