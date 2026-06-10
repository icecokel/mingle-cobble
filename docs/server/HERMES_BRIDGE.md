# Hermes Bridge

마지막 갱신: 2026-06-08

이 문서는 `icecoke-cobblemon-161` 레거시 라인에서 Minecraft 채팅 질문을 받아 서버 문서, 설치 모드 메타데이터, 플레이어 메모, 일반 Minecraft/Cobblemon 지식 기준 답변을 돌려주는 브리지의 운영 방법을 정리한다. 현재 플레이 기준인 `icecoke-cobblemon-173`으로의 이관은 별도 작업이며, 아직 173 라인에서 완료된 것으로 보지 않는다.

## 목적

게임 중 서버 설정, 관장 후보, 운영 룰, 적용 모드, 기본 Minecraft/Cobblemon 플레이 방법을 물어보면 Hermes/Codex가 `/home/icenux/minecraft/mingle-lounge/docs` 문서, 루트 플레이어 가이드, `mods/` jar 메타데이터, 최근 메모를 읽고 짧게 답한다. 161 레거시 서버는 개인 서버 기준이라 플레이어 채팅 전체를 Hermes 질문으로 처리한다.

예시:

```text
죽으면 가방이랑 경험치 보호돼?
강철 관장 후보 좌표 어디야?
서버 이름 뭐야?
메모: 강철 관장은 강변 마을 컨셉 유지
메모해줘 데일리 보상은 접속 기준
기억해줘 관장 보상은 아직 인게임 검증 전
```

## 구조

```text
Minecraft chat
  -> logs/latest.log 감시
  -> tools/mc_hermes_bridge.py
  -> 메모 요청이면 data/hermes-memos.jsonl 저장
  -> mods/*.jar의 fabric.mod.json / quilt.mod.json / META-INF/mods.toml 요약
  -> Hermes chat, OpenAI Codex OAuth provider
  -> docs/ 문서, 플레이어 가이드, 최근 메모, 일반 Minecraft 지식 참고
  -> screen 콘솔 tellraw 응답
```

## 안전 기준

- 개인 서버 기준으로 브리지는 플레이어 채팅 전체를 처리한다.
- `메모:`, `메모해줘`, `기억해줘`로 시작하는 채팅은 답변 요청이 아니라 메모 저장 요청으로 처리한다.
- 답변 엔진은 문서와 모드 jar 메타데이터를 읽기만 한다.
- 일반 Minecraft, Fabric, Cobblemon, 설치 모드 지식을 사용할 수 있지만, 현재 161 레거시 서버 문서와 설치 모드 메타데이터를 최우선 근거로 본다.
- 일반 지식이 Minecraft `1.21.1`, Fabric, Cobblemon `1.6.1`, 설치 모드 버전과 다를 수 있으면 확인 필요로 답한다.
- 서버 설정 변경, 문서 수정, 월드 변경, 명령 실행을 답변 엔진에 허용하지 않는다.
- bridge 자체는 사용자가 명시한 메모만 `/home/icenux/minecraft/mingle-lounge/data/hermes-memos.jsonl`에 저장한다.
- OAuth, auth, token, secret, key 파일 내용은 절대 답변하지 않는다.
- 초기 운영은 수동 실행으로만 한다. systemd 상시 서비스 등록은 별도 검증 후 진행한다.

## 파일 위치

| 항목 | 경로 |
| --- | --- |
| 로컬 원본 | `/Users/smlee/mingle-lounge/tools/mc_hermes_bridge.py` |
| 서버 사본 | `/home/icenux/minecraft/mingle-lounge/tools/mc_hermes_bridge.py` |
| 서버 문서 | `/home/icenux/minecraft/mingle-lounge/docs` |
| 서버 로그 | `/home/icenux/minecraft/mingle-lounge/logs/latest.log` |
| 서버 모드 | `/home/icenux/minecraft/mingle-lounge/mods` |
| 메모 파일 | `/home/icenux/minecraft/mingle-lounge/data/hermes-memos.jsonl` |
| screen 세션 | `mingle-sample` |

## 답변 컨텍스트

Hermes bridge는 질문마다 아래 컨텍스트를 프롬프트에 넣는다.

| 컨텍스트 | 설명 |
| --- | --- |
| 서버 문서 | `/home/icenux/minecraft/mingle-lounge/docs` 아래 운영 문서 |
| 플레이어 가이드 | `cobblemon-newbie-guide.md`, `cobblemon-mod-usage-guide.md`, `cobblemon-client-setup-guide.md` |
| 설치 모드 메타데이터 | `mods/*.jar` 안의 `fabric.mod.json`, `quilt.mod.json`, `META-INF/mods.toml`에서 id/name/version/description 추출 |
| 최근 메모 | `data/hermes-memos.jsonl` 최근 12개 |
| 일반 지식 | Minecraft, Fabric, Cobblemon, 설치 모드에 대한 일반 지식. 서버 버전과 다를 수 있으면 확인 필요로 답변 |

모드 jar는 실행하지 않고 zip 파일로 열어 메타데이터만 읽는다. 메타데이터가 없는 jar는 파일명만 컨텍스트에 넣는다.

## 수동 테스트

서버에서 실제 채팅을 감시하지 않고 질문 1개만 테스트한다.

```bash
cd /home/icenux/minecraft/mingle-lounge
python3 tools/mc_hermes_bridge.py \
  --dry-run \
  --engine hermes \
  --once-player Icecokel \
  --once-question '서버 이름 뭐야?'
```

`--dry-run`이면 실제 Minecraft 채팅으로 보내지 않고 `tellraw` 명령만 출력한다.

## 수동 실행

```bash
cd /home/icenux/minecraft/mingle-lounge
python3 tools/mc_hermes_bridge.py --engine auto
```

현재 서버에서는 별도 screen 세션으로 실행한다.

```bash
screen -dmS mc-hermes-bridge bash -lc 'cd /home/icenux/minecraft/mingle-lounge && exec python3 tools/mc_hermes_bridge.py --engine auto >> logs/mc-hermes-bridge.log 2>&1'
```

재기동:

```bash
screen -S mc-hermes-bridge -X quit
screen -dmS mc-hermes-bridge bash -lc 'cd /home/icenux/minecraft/mingle-lounge && exec python3 tools/mc_hermes_bridge.py --engine auto >> logs/mc-hermes-bridge.log 2>&1'
```

상태 확인:

```bash
screen -ls | grep mc-hermes-bridge
ps aux | grep 'tools/mc_hermes_bridge.py'
tail -n 80 logs/mc-hermes-bridge.log
```

기본값:

| 항목 | 값 |
| --- | --- |
| Prefix | 없음. 모든 플레이어 채팅 처리 |
| Engine | `auto` |
| Hermes timeout | 90초 |
| Player cooldown | 10초 |
| Max question | 500자 |
| Max answer | 420자 |
| Memo limit | 최근 12개 |
| Mods dir | `mods` |
| Mod limit | 최대 140개 |

`auto` 엔진은 Hermes 호출을 먼저 시도하고 실패하면 `codex exec --sandbox read-only`로 fallback한다.

## 장애 대응

서버 재시작 뒤 Hermes가 반응하지 않으면 bridge가 이전 `latest.log` 파일을 보고 있는지 확인한다.

```bash
pid=$(ps -ef | awk '/python3 tools\/mc_hermes_bridge.py --engine auto/ && !/awk/ {print $2; exit}')
for fd in /proc/$pid/fd/*; do readlink "$fd"; done | grep latest.log
```

정상 상태는 `/home/icenux/minecraft/mingle-lounge/logs/latest.log`를 가리킨다. `deleted`가 붙은 과거 로그를 보고 있으면 `mc-hermes-bridge`만 재기동한다. 현재 bridge 스크립트는 `latest.log` 교체와 truncate를 감지해 자동으로 다시 열도록 되어 있다.

## 현재 확인 상태

- Hermes 상태에서 `Provider: OpenAI Codex`와 OpenAI Codex OAuth 로그인 상태를 확인했다.
- `hermes chat --quiet --query` 단발 질문 응답을 확인했다.
- `codex exec --sandbox read-only` fallback 응답을 확인했다.
- `python3 tools/mc_hermes_bridge.py --dry-run --engine hermes --once-question`으로 `tellraw` 출력 생성을 확인했다.
- `mc-hermes-bridge` screen 세션으로 브리지를 기동했다.
- 서버 재시작 후 이전 삭제 로그를 따라가던 문제를 수정했고, 새 bridge 프로세스가 현재 `logs/latest.log`를 여는 것을 확인했다.
- Prefix 없이 모든 플레이어 채팅을 처리하도록 변경했다.
- 플레이어 요청 메모를 `data/hermes-memos.jsonl`에 저장하고, 최근 메모를 답변 프롬프트에 포함하도록 변경했다.
- 질문마다 설치 모드 jar 메타데이터 요약을 프롬프트에 포함하도록 변경했다.
- 서버 문서가 부족할 때 일반 Minecraft/Fabric/Cobblemon/설치 모드 지식을 사용할 수 있게 변경했다.
- 실제 플레이어가 인게임 채팅으로 질문해 받는 end-to-end 테스트는 재확인 필요다.

## 운영 보류

- systemd 사용자 서비스 등록
- 서버 시작 스크립트에 브리지 자동 실행 추가
- 장기 질문 이력 저장
- 서버 설정 변경 명령 실행
- 월드 변경 자동화
