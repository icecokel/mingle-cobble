scoreboard players add @a ml_login_seen 0

execute as @a[scores={ml_login_seen=0}] run function mingle_login_reward:init_player
execute as @a[scores={ml_login_seen=1..}] run function mingle_login_reward:check_player

schedule function mingle_login_reward:check 5s replace
