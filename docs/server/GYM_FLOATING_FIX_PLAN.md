# Gym Floating Fix Plan

마지막 갱신: 2026-06-03

현재 상태: 적용 완료. 결과는 `GYM_PLACEMENT_LOG.md`의 `2026-06-03 지면 기준 gym 재보정` 섹션을 우선한다.

이 문서는 CobbleBuilds gym 구조물이 허공에 떠 있는 문제를 다시 수정하기 위한 검증 계획과 작업 순서를 기록한다.

## 문제 요약

2026-06-03 1차 보정에서는 구조물 바로 아래 `Y - 1` 한 층에 `stone` 받침을 추가하고, 콘솔에서 해당 위치가 공기가 아닌지만 확인했다.

이 검증은 실패한 기준이다. 구조물 바로 아래 한 칸이 solid여도, 그 받침 자체가 실제 지면에서 수십 블록 위에 있으면 구조물은 여전히 허공에 떠 있다.

스크린샷 기준 문제 위치:

| 항목 | 값 |
| --- | --- |
| 플레이어 좌표 | 약 `-55 111 -558` |
| 기존 `rock_gym` 구조물 좌표 | `-56 175 -555` |
| 차이 | 약 `64`블록 위 |

따라서 이번 수정의 기준은 “하단 1칸 solid”가 아니라 “구조물 footprint가 실제 자연 지면과 충분히 가까운가”로 둔다.

## 수정 대상

CobbleBuilds 기본 건물이 있는 6개 gym만 이번 수정 대상이다.

| Gym ID | 구조물 |
| --- | --- |
| `rock_gym` | `cobblebuilds:rock_gym` |
| `grass_gym` | `cobblebuilds:grass_gym` |
| `water_gym` | `cobblebuilds:water_gym` |
| `electric_gym` | `cobblebuilds:electric_gym` |
| `fire_gym` | `cobblebuilds:fire_gym` |
| `poison_gym` | `cobblebuilds:poison_gym` |

`ice_gym`, `steel_gym`은 건물 구조물이 없어 이번 구조물 재배치 대상이 아니다.

## 통과 기준

구조물 제거 후 자연 지형 heightmap을 기준으로 후보지를 고른다.

| 기준 | 통과 조건 |
| --- | --- |
| footprint 크기 | `33 x 39` |
| 후보 계산 시점 | 기존 구조물과 받침 제거 후 `save-all flush` 완료 뒤 |
| 배치 높이 | 후보 footprint의 자연 지형 최고점 `maxH + 1` |
| 최대 지면 간격 | `baseY - 1 - minH <= 6` |
| 중앙 지면 간격 | `baseY - 1 - centerH <= 4` |
| 평균 지면 간격 | `baseY - 1 - avgH <= 4` 권장 |
| 콘솔 검증 | corners, center, edge sample에서 구조물 바로 아래가 solid |
| 저장 검증 | `save-all flush` 완료 |
| forceload 검증 | `forceload query` 결과 강제 로드 청크 없음 |

`max_gap > 6`이면 작은 stone 판을 만드는 것에 불과하므로 실패로 본다. 이 경우 같은 gym의 후보 X/Z를 다시 찾아야 한다.

## 작업 순서

1. `save-all flush` 후 `world/` 백업을 만든다.
2. 백업 tar와 `.sha256`을 생성하고 `sha256sum -c`로 확인한다.
3. 6개 건물형 gym의 현재 구조물, 1차 보정 받침, gym marker, NPC spawner marker를 제거한다.
4. `save-all flush`를 실행한다.
5. 관련 region 파일의 heightmap을 읽어 각 gym 주변의 평탄 후보지를 계산한다.
6. 각 gym의 후보 X/Z, `minH`, `centerH`, `avgH`, `maxH`, `baseY`, `max_gap`을 기록한다.
7. 통과 기준을 만족하는 후보에만 구조물을 다시 배치한다.
8. 구조물 아래 한 층은 `replace air` 방식으로만 얇은 foundation을 둔다.
9. gym marker와 NPC spawner marker를 구조물 중앙 근처에 다시 생성한다.
10. 콘솔에서 marker/spawner 존재, sample 하단 solid, `forceload query`, `save-all flush`를 확인한다.
11. `GYM_PLACEMENT_LOG.md`, `CHANGELOG.md`, 서버 문서 사본을 갱신한다.

## 완료 조건

- 6개 건물형 gym 모두 자연 지면 기준 gap 검증을 통과한다.
- 기존 허공 구조물과 높은 stone 판이 남지 않는다.
- 콘솔 기준 marker/spawner가 다시 조회된다.
- 서버 저장과 forceload 해제가 확인된다.
- 인게임 육안 확인은 남은 검증으로 분리하되, 콘솔 기준으로 “64블록 위에 떠 있는 상태”는 재발하지 않아야 한다.
