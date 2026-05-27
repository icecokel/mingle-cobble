give @s cobblemon:poke_ball 5
loot give @s loot mingle_login_reward:bonus

scoreboard players operation @s ml_login_last = #server_seconds ml_login_clock
tellraw @s {"text":"6시간 접속 보상: 몬스터볼 5개와 랜덤 추가 보상을 확인하세요.","color":"green"}
