# icecoke-cobblemon 관장 포켓몬 구성

마지막 갱신: 2026-06-03

이 문서는 `icecoke-cobblemon` 개인 서버의 8관장 포켓몬 팀 초안을 정리한다. 실제 NPC 배치 전 기획 문서이며, 팀은 Cobblemon `1.6.1` 서버 jar에서 종 파일 존재를 확인한 포켓몬 위주로 구성한다.

## 구성 기준

| 항목 | 기준 |
| --- | --- |
| 난이도 방식 | 배지 수 기반 단계식 난이도 |
| 단계 | 초급, 표준, 상급 |
| 초급 | 배지 0-1개 기준, 3마리 |
| 표준 | 배지 2-5개 기준, 4마리 |
| 상급 | 배지 6개 이상 또는 재도전 기준, 5마리 |
| 기술 구성 | 실제 Easy NPC/Cobblebuilds 적용 직전 ID 검증 |
| 아이템 | 초기 배치에서는 없음, 상급 재도전에서만 검토 |

팀은 타입 정체성이 분명하고, 개인 서버에서 과하게 막히지 않는 것을 우선한다. 상급 팀은 완전 경쟁전 구성이 아니라 재도전용 체감 난이도 상승 정도로 본다.

## 난이도 공통 규칙

| 단계 | 레벨 범위 | 팀 크기 | 설계 의도 |
| --- | --- | --- | --- |
| 초급 | Lv. 10-18 | 3마리 | 타입 맛보기, 초반 진행 방해 최소화 |
| 표준 | Lv. 28-42 | 4마리 | 관장다운 상성 압박과 에이스 운영 |
| 상급 | Lv. 55-68 | 5마리 | 재도전/후반 목표, 최종 진화체 중심 |

레벨은 관장 순서 고정이 아니라 플레이어 진행도에 맞춰 고르는 기준이다. 예를 들어 바위 관장을 늦게 만나면 초급 바위 팀이 아니라 표준 또는 상급 바위 팀을 사용한다.

## 1. 바위 관장

컨셉: 광산, 절벽, 단단한 방어. 첫 관장 후보지만 상급에서는 물리 압박을 준다.

| 단계 | 팀 |
| --- | --- |
| 초급 | Geodude Lv. 11, Rockruff Lv. 12, Onix Lv. 14 |
| 표준 | Graveler Lv. 30, Nosepass Lv. 31, Rhyhorn Lv. 32, Lycanroc Lv. 34 |
| 상급 | Golem Lv. 58, Rhydon Lv. 59, Nosepass Lv. 60, Onix Lv. 61, Lycanroc Lv. 63 |

운영 방향:

- 초급은 방어가 높지만 약점이 뚜렷하게 보이게 둔다.
- 표준부터 바위/땅 조합으로 전기, 불꽃 타입을 견제한다.
- 상급 에이스는 Lycanroc으로 둔다.

## 2. 풀 관장

컨셉: 숲, 정원, 회복과 상태이상. 초반 친화적이지만 상급은 회복전으로 길어진다.

| 단계 | 팀 |
| --- | --- |
| 초급 | Oddish Lv. 12, Budew Lv. 13, Bulbasaur Lv. 15 |
| 표준 | Gloom Lv. 29, Roselia Lv. 31, Lombre Lv. 32, Ivysaur Lv. 34 |
| 상급 | Vileplume Lv. 57, Roserade Lv. 59, Ludicolo Lv. 60, Venusaur Lv. 62, Gloom Lv. 58 |

운영 방향:

- 초급은 독/풀 상태이상 맛보기로 둔다.
- 표준은 물가 바이옴과 연결되도록 Lombre를 넣는다.
- 상급 에이스는 Venusaur, 보조 에이스는 Roserade로 둔다.

## 3. 물 관장

컨셉: 강, 호수, 낚시터. 초급은 접근성이 좋고, 상급은 Gyarados와 Starmie로 속도감을 준다.

| 단계 | 팀 |
| --- | --- |
| 초급 | Magikarp Lv. 12, Psyduck Lv. 14, Squirtle Lv. 16 |
| 표준 | Golduck Lv. 31, Wartortle Lv. 32, Staryu Lv. 33, Gyarados Lv. 36 |
| 상급 | Blastoise Lv. 59, Golduck Lv. 58, Starmie Lv. 60, Ludicolo Lv. 61, Gyarados Lv. 64 |

운영 방향:

- 초급 Magikarp는 쉬운 시작과 낚시터 분위기용이다.
- 표준부터 Gyarados를 에이스로 세워 난이도를 올린다.
- 상급은 Starmie 속도와 Gyarados 압박을 같이 사용한다.

## 4. 전기 관장

컨셉: 발전소, 탑, 속도전. 초급은 마비, 표준 이후는 강철 보조 타입으로 방어를 섞는다.

| 단계 | 팀 |
| --- | --- |
| 초급 | Mareep Lv. 14, Pikachu Lv. 15, Magnemite Lv. 17 |
| 표준 | Flaaffy Lv. 32, Pikachu Lv. 33, Magneton Lv. 35, Raichu Lv. 37 |
| 상급 | Ampharos Lv. 58, Raichu Lv. 60, Magneton Lv. 61, Magnezone Lv. 63, Pikachu Lv. 57 |

운영 방향:

- 초급은 마비와 전기 타입 상성을 배우는 단계다.
- 표준은 Magneton으로 단순 전기 타입보다 단단하게 만든다.
- 상급 에이스는 Ampharos 또는 Magnezone으로 둔다.

## 5. 불꽃 관장

컨셉: 사막, 대장간, 붉은 협곡. 빠른 화력과 화상 압박.

| 단계 | 팀 |
| --- | --- |
| 초급 | Vulpix Lv. 15, Houndour Lv. 16, Ponyta Lv. 18 |
| 표준 | Ninetales Lv. 34, Growlithe Lv. 33, Houndoom Lv. 36, Rapidash Lv. 38 |
| 상급 | Ninetales Lv. 59, Arcanine Lv. 62, Houndoom Lv. 61, Rapidash Lv. 60, Magmortar Lv. 64 |

운영 방향:

- 초급은 속도는 있지만 내구가 낮게 둔다.
- 표준부터 Houndoom으로 에스퍼/고스트 견제를 추가한다.
- 상급 에이스는 Magmortar, 분위기 에이스는 Arcanine으로 둔다.

## 6. 독 관장

컨셉: 늪, 폐허, 독성 연구소. 상태이상과 지속 압박.

| 단계 | 팀 |
| --- | --- |
| 초급 | Grimer Lv. 15, Koffing Lv. 16, Croagunk Lv. 18 |
| 표준 | Muk Lv. 35, Weezing Lv. 36, Haunter Lv. 37, Toxicroak Lv. 39 |
| 상급 | Muk Lv. 60, Weezing Lv. 61, Gengar Lv. 63, Toxicroak Lv. 62, Vileplume Lv. 59 |

운영 방향:

- 초급은 독 상태이상과 타입 상성 학습용이다.
- 표준부터 Haunter로 독/고스트 분위기를 강화한다.
- 상급 에이스는 Gengar, 물리 압박은 Toxicroak이 맡는다.

## 7. 얼음 관장

컨셉: 설산, 얼음 동굴, 장거리 탐험. 느리지만 단단하고 후반 위협이 큰 팀.

| 단계 | 팀 |
| --- | --- |
| 초급 | Spheal Lv. 16, Snorunt Lv. 17, Swinub Lv. 18 |
| 표준 | Sealeo Lv. 36, Glalie Lv. 38, Piloswine Lv. 39, Bergmite Lv. 37 |
| 상급 | Walrein Lv. 61, Glalie Lv. 60, Mamoswine Lv. 64, Avalugg Lv. 63, Sealeo Lv. 58 |

운영 방향:

- 초급은 설산 입문용으로 과하게 세지 않게 둔다.
- 표준은 얼음 약점을 알기 쉽게 노출한다.
- 상급 에이스는 Mamoswine, 방어형 축은 Avalugg로 둔다.

## 8. 강철 관장

컨셉: 광산 도시, 철 요새, 마지막 관문. 방어가 높고 약점 공략을 요구한다.

| 단계 | 팀 |
| --- | --- |
| 초급 | Aron Lv. 16, Magnemite Lv. 17, Mawile Lv. 19 |
| 표준 | Lairon Lv. 38, Magneton Lv. 39, Skarmory Lv. 40, Metang Lv. 42 |
| 상급 | Aggron Lv. 63, Skarmory Lv. 62, Magnezone Lv. 64, Metagross Lv. 66, Mawile Lv. 61 |

운영 방향:

- 초급은 강철 타입의 단단함을 보여 주되, 불꽃/격투/땅 약점을 열어 둔다.
- 표준부터 Skarmory로 물리 내성을 체감하게 한다.
- 상급 에이스는 Metagross, 요새형 에이스는 Aggron으로 둔다.

## 배지 수 기반 선택표

| 플레이어 진행도 | 추천 팀 단계 |
| --- | --- |
| 배지 0-1개 | 초급 |
| 배지 2-5개 | 표준 |
| 배지 6개 이상 | 상급 |
| 재도전 | 상급 |

초기 구현에서는 관장별로 한 단계만 배치해도 된다. 동적 난이도를 실제로 적용하려면 같은 관장 컨셉의 NPC 프리셋을 초급/표준/상급으로 나누고, 배지 수에 따라 상대할 프리셋을 선택하는 방식이 안전하다.

## 구현 전 검증 항목

1. 각 포켓몬 종 ID가 서버에서 `/spawnpokemon` 또는 NPC 팀 설정에서 인식되는지 확인한다.
2. `Magnezone`, `Golem`처럼 진화체 이름이 NPC 설정에서 정상 처리되는지 확인한다.
3. 기술 ID는 실제 Easy NPC/Cobblebuilds 설정 방식에 맞춰 별도 검증한다.
4. 상급 팀은 먼저 관리자 테스트 전투로 난이도를 확인한다.
5. 적용은 1번 바위 관장 초급 팀부터 시작한다.
