#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PACK_DIR="$ROOT_DIR/datapacks/mingle-login-reward"
PACK_ZIP="$ROOT_DIR/datapacks/mingle-login-reward.zip"

test -f "$PACK_DIR/pack.mcmeta"
test -f "$PACK_DIR/data/minecraft/tags/function/load.json"
test -f "$PACK_DIR/data/mingle_login_reward/function/load.mcfunction"
test -f "$PACK_DIR/data/mingle_login_reward/function/clock.mcfunction"
test -f "$PACK_DIR/data/mingle_login_reward/function/check.mcfunction"
test -f "$PACK_DIR/data/mingle_login_reward/function/init_player.mcfunction"
test -f "$PACK_DIR/data/mingle_login_reward/function/check_player.mcfunction"
test -f "$PACK_DIR/data/mingle_login_reward/function/give.mcfunction"
test -f "$PACK_DIR/data/mingle_login_reward/loot_table/bonus.json"
test -f "$PACK_ZIP"

OLD_DAILY_REWARD="$(find "$ROOT_DIR/datapacks" -maxdepth 2 \( -name 'daily-reward' -o -name 'daily-reward.zip' \) -print -quit)"
if [[ -n "$OLD_DAILY_REWARD" ]]; then
  echo "old daily-reward datapack name still exists" >&2
  exit 1
fi

grep -q 'mingle_login_reward:load' "$PACK_DIR/data/minecraft/tags/function/load.json"
grep -q 'schedule function mingle_login_reward:clock 1s replace' "$PACK_DIR/data/mingle_login_reward/function/load.mcfunction"
grep -q 'schedule function mingle_login_reward:check 5s replace' "$PACK_DIR/data/mingle_login_reward/function/load.mcfunction"
grep -q 'scoreboard players add #server_seconds ml_login_clock 1' "$PACK_DIR/data/mingle_login_reward/function/clock.mcfunction"
grep -q 'matches 21600..' "$PACK_DIR/data/mingle_login_reward/function/check_player.mcfunction"
grep -q 'loot give @s loot mingle_login_reward:bonus' "$PACK_DIR/data/mingle_login_reward/function/give.mcfunction"

jq -e '.pack.pack_format == 48' "$PACK_DIR/pack.mcmeta" >/dev/null
jq -e '[.pools[0].entries[].weight] | add == 100' "$PACK_DIR/data/mingle_login_reward/loot_table/bonus.json" >/dev/null
jq -e '
  .pools[0].entries
  | any(.type == "minecraft:empty" and .weight == 40)
    and any(.name == "cobblemon:great_ball" and .weight == 25 and .functions[0].count == 3)
    and any(.name == "cobblemon:exp_candy_xs" and .weight == 15 and .functions[0].count == 2)
    and any(.name == "cobblemon:exp_candy_xs" and .weight == 10 and .functions[0].count == 5)
    and any(.name == "cobblemon:revival_herb" and .weight == 5)
    and any(.name == "cobblemon:ultra_ball" and .weight == 3)
    and any(.name == "cobblemon:revive" and .weight == 2)
' "$PACK_DIR/data/mingle_login_reward/loot_table/bonus.json" >/dev/null

unzip -t "$PACK_ZIP" >/dev/null
ZIP_LIST="$(unzip -Z1 "$PACK_ZIP")"
grep -q '^pack.mcmeta$' <<< "$ZIP_LIST"
grep -q '^data/mingle_login_reward/function/check_player.mcfunction$' <<< "$ZIP_LIST"
