# Gym Implementation Plan

> **Status:** 이 문서는 2026-06-03에 161 레거시 라인 기준으로 작성한 관장 배치 실행 계획 기록이다. 현재 플레이 기준은 `icecoke-cobblemon-173`이며, 173 라인에서 관장 작업을 다시 진행할 때는 [COBBLEMON_173_LINE.md](COBBLEMON_173_LINE.md), [GYM_PLACEMENT_LOG.md](GYM_PLACEMENT_LOG.md), [OPS_RUNBOOK.md](OPS_RUNBOOK.md)를 함께 확인하고 173 기준으로 재검증한다.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to execute this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `icecoke-cobblemon` 개인 서버에 8관장 탐험 콘텐츠를 안전하게 추가한다.

**Architecture:** 로컬 `docs/server/`를 원본으로 두고, 조사와 설계는 서브 에이전트가 병렬로 수행한다. 실제 월드 변경은 메인 컨트롤러가 백업, 콘솔 명령, 저장, 검증 순서로 1개 관장씩 적용한다.

**Tech Stack:** Minecraft `1.21.1`, Fabric, Cobblemon `1.6.1`, CobbleBuilds Leaders, Easy NPC, Badgebox, remote server `icenux-ms7b23`.

**Version Guard:** 현재 활성 서버는 `sample/포켓몬 100일 생존 1.21.zip` 기반이며, 서버 `mods/`에서 `Cobblemon-fabric-1.6.1+1.21.1.jar`를 확인했다. 기존 Mingle Lounge `1.7.3` 기준과 섞지 않는다.

---

## Safety Rules

- 서버 안정성과 월드 보존을 최우선으로 둔다.
- 서브 에이전트는 기본적으로 읽기 전용 조사와 문서 패치만 맡는다.
- 실제 서버 월드에 쓰는 작업은 메인 컨트롤러만 수행한다.
- 구조물/NPC/marker를 배치하기 전에는 `world/` 백업을 만든다.
- 8관장을 한 번에 배치하지 않는다. 1개 관장 배치 후 저장, 재기동 또는 재접속 검증, 문서화를 끝낸 뒤 다음 관장으로 넘어간다.
- 클라이언트 모드 조건이 바뀌는 변경은 하지 않는다.
- 새 모드 추가는 현재 범위에서 제외한다.

## Source Documents

| Document | Purpose |
| --- | --- |
| `docs/server/GYM_CONCEPT.md` | 타입, 바이옴, 구조물 지원 여부, 동적 난이도 방향 |
| `docs/server/GYM_TEAMS.md` | 관장별 초급/표준/상급 포켓몬 구성 |
| `docs/server/GYM_PLACEMENT_LOG.md` | 실제 배치 좌표, 명령, 검증 결과 |
| `docs/server/OPS_RUNBOOK.md` | SSH, screen 콘솔 입력, 백업, 점검 절차 |
| `docs/server/SERVER_RULES.md` | 운영 룰과 안전 기준 |
| `docs/server/CHANGELOG.md` | 작업 이력 |

## 작성 당시 Known State

| Item | Value |
| --- | --- |
| Server | `icenux-ms7b23` |
| Server path | `/home/icenux/minecraft/mingle-lounge` |
| Local source docs | `/Users/smlee/mingle-lounge/docs/server` |
| Remote docs copy | `/home/icenux/minecraft/mingle-lounge/docs` |
| Screen session | `mingle-sample` |
| Port | `25565` |
| Current server name | `icecoke-cobblemon` |
| Current marker test | `rock_gym` marker and Brock spawner marker at `2 68 -359` |
| Current limitation | Actual `cobblemon:npc` Brock still needs player proximity in-game verification |

## Subagent Survey Result Summary

| Area | Result | Next Action |
| --- | --- | --- |
| Candidate coordinates | 1차 후보 8개를 `GYM_PLACEMENT_LOG.md`에 통합 | 인게임 지형/공간 확인 후 최종 좌표 확정 |
| Strong candidates | `rock_gym`, `grass_gym`, `ice_gym`, `steel_gym` | 우선 육안 검증 |
| Needs route review | `water_gym`, `electric_gym` | 스폰과 너무 가깝거나 컨셉 근거가 약해 동선 재검토 |
| Needs more exploration | `fire_gym`, `poison_gym` | 사막/악지, 늪/어두운 숲/습지 추가 탐사 |
| Placement command | `place template` + direct marker summon 방식 | 구조물 footprint 확인 후 1개 관장만 적용 |
| Rollback | marker/NPC는 조건부 kill 가능, 구조물은 고위험 백업 복구만 허용 | 배치 전 백업 필수. 복구는 재기동/재검증 전 완료 아님 |
| Ice/steel NPC risk | NPC/party는 있으나 variation 내부값이 placeholder로 보임 | 인게임 외형 확인 필요 |

## Gym Lineup

| Order | Type | Gym ID | Location Concept | Building Support | Implementation Mode |
| --- | --- | --- | --- | --- | --- |
| 1 | 바위 | `rock_gym` | 산, 돌산, 절벽 | CobbleBuilds building exists | Structure + marker + NPC spawner |
| 2 | 풀 | `grass_gym` | 숲, 꽃 숲, 초원 | CobbleBuilds building exists | Structure + marker + NPC spawner |
| 3 | 물 | `water_gym` | 강, 호수, 해변 | CobbleBuilds building exists | Structure + marker + NPC spawner |
| 4 | 전기 | `electric_gym` | 평원 마을, 고지대, 탑 | CobbleBuilds building exists | Structure + marker + NPC spawner |
| 5 | 불꽃 | `fire_gym` | 사막, 악지, 용암 근처 | CobbleBuilds building exists | Structure + marker + NPC spawner |
| 6 | 독 | `poison_gym` | 늪, 어두운 숲, 습지 | CobbleBuilds building exists | Structure + marker + NPC spawner |
| 7 | 얼음 | `ice_gym` | 설산 | No building found | Manual small base + marker + NPC spawner |
| 8 | 강철 | `steel_gym` | 강을 끼고 있는 마을 | No building found | Manual village base + small signal marker + NPC spawner |

## Subagent Work Split

### Task 1: World Candidate Survey

**Owner:** explorer subagent  
**Write scope:** none unless asked to return a patch separately  
**Goal:** 현재 월드에서 관장 후보 좌표를 찾는다.

- [ ] Read `GYM_CONCEPT.md`, `GYM_PLACEMENT_LOG.md`, and `OPS_RUNBOOK.md`.
- [ ] Inspect server world metadata and available tools without modifying world files.
- [ ] Produce at least one candidate for each required concept:
  - rock: 산/돌산/절벽
  - grass: 숲/꽃 숲/초원
  - water: 강/호수/해변
  - electric: 평원 마을/고지대/탑
  - fire: 사막/악지/용암 근처
  - poison: 늪/어두운 숲/습지
  - ice: 설산
  - steel: 강을 끼고 있는 마을
- [ ] For each candidate, return coordinates, biome evidence, distance from spawn if available, and risk notes.
- [ ] Do not run commands that alter chunks, entities, gamerules, server properties, or files.

Expected output:

```markdown
## Candidate Survey

| Gym ID | Candidate XYZ | Biome/terrain evidence | Distance/routing | Risk |
| --- | --- | --- | --- | --- |
| rock_gym | ... | ... | ... | ... |
```

### Task 2: CobbleBuilds Placement Method Survey

**Owner:** explorer subagent  
**Write scope:** none unless asked to return a patch separately  
**Goal:** 구조물과 marker/NPC spawner를 안전하게 배치하는 명령 절차를 확정한다.

- [ ] Read `GYM_PLACEMENT_LOG.md` and `OPS_RUNBOOK.md`.
- [ ] Inspect CobbleBuilds jar resources on the server or local copy if available.
- [ ] Confirm structure IDs for `rock_gym`, `grass_gym`, `water_gym`, `electric_gym`, `fire_gym`, `poison_gym`.
- [ ] Confirm NPC variation IDs for all 8 gym leaders.
- [ ] Confirm the safest command pattern for:
  - structure placement
  - gym marker placement
  - NPC spawner marker placement
  - post-placement query
  - rollback query/removal
- [ ] Do not alter the world.

Expected output:

```markdown
## Placement Method Survey

### Safe command sequence

1. Backup command
2. Structure command
3. Marker command
4. Spawner command
5. Verification command
6. Rollback command

### IDs

| Gym ID | Structure ID | NPC ID | Notes |
| --- | --- | --- | --- |
```

### Task 3: Documentation Patch

**Owner:** worker subagent  
**Write scope:** `docs/server/GYM_PLACEMENT_LOG.md`, `docs/server/CHANGELOG.md` only  
**Goal:** 조사 결과를 반영할 문서 템플릿을 준비한다.

- [ ] Add a section named `## Gym Candidate Survey` to `GYM_PLACEMENT_LOG.md`.
- [ ] Add a section named `## Placement Command Template` to `GYM_PLACEMENT_LOG.md`.
- [ ] Add one changelog line saying the subagent-driven implementation plan was added.
- [ ] Do not invent coordinates. Use `확인 필요` where survey results are not integrated yet.
- [ ] Do not edit server files directly.
- [ ] Do not change `GYM_CONCEPT.md` or `GYM_TEAMS.md`.

Expected verification:

```bash
git diff --check -- docs/server/GYM_PLACEMENT_LOG.md docs/server/CHANGELOG.md
rg -n "Gym Candidate Survey|Placement Command Template|subagent" docs/server/GYM_PLACEMENT_LOG.md docs/server/CHANGELOG.md
```

### Task 4: Controller Integration

**Owner:** main controller  
**Write scope:** all docs under `docs/server/`  
**Goal:** 서브 에이전트 결과를 검토해 하나의 적용 후보 목록으로 통합한다.

- [ ] Review Task 1 candidate survey.
- [ ] Review Task 2 placement method survey.
- [ ] Review Task 3 documentation patch.
- [ ] Resolve conflicts manually.
- [ ] Update `GYM_PLACEMENT_LOG.md` with selected candidates and command templates.
- [ ] Update `CHANGELOG.md`.
- [ ] Run:

```bash
git diff --check -- docs/server
```

### Task 5: First Real Gym Application

**Owner:** main controller only  
**Write scope:** remote server world, then local docs  
**Goal:** 바위 관장 1개를 완성형으로 검증한다.

- [ ] Confirm server status:

```bash
ssh icenux-ms7b23 'cd ~/minecraft/mingle-lounge && screen -ls && ss -ltnp | grep :25565'
```

- [ ] Create a fresh `world/` backup.
- [ ] Verify backup archive and checksum.
- [ ] Apply only one gym.
- [ ] Query markers/entities after placement.
- [ ] Save world.
- [ ] Record exact commands and output summary in `GYM_PLACEMENT_LOG.md`.
- [ ] Sync local docs to server docs.
- [ ] Leave in-game client verification as `확인 필요` if the client is not opened.

### Task 6: Repeat Per Gym

**Owner:** main controller only  
**Write scope:** remote server world, then local docs  
**Goal:** 2번부터 8번 관장까지 같은 절차로 반복한다.

- [ ] Apply only one additional gym per cycle.
- [ ] Verify markers/entities.
- [ ] Record coordinates and rollback notes.
- [ ] Stop if a placement fails or if NPC spawning cannot be verified.

## Final Verification

Run these before claiming completion:

```bash
git diff --check -- docs/server
rsync -av --delete /Users/smlee/mingle-lounge/docs/server/ icenux-ms7b23:/home/icenux/minecraft/mingle-lounge/docs/
find /Users/smlee/mingle-lounge/docs/server -maxdepth 1 -type f -print0 | sort -z | xargs -0 shasum -a 256
ssh icenux-ms7b23 'cd /home/icenux/minecraft/mingle-lounge/docs && find . -maxdepth 1 -type f -print0 | sort -z | xargs -0 sha256sum'
```

Completion means:

- Local docs and server docs match.
- Every actual world change has a backup, coordinate record, and rollback note.
- Any unverified in-game NPC behavior is explicitly marked `확인 필요`.
