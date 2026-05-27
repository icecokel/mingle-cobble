scoreboard players operation @s ml_login_elapsed = #server_seconds ml_login_clock
scoreboard players operation @s ml_login_elapsed -= @s ml_login_last

execute if score @s ml_login_elapsed matches 21600.. run function mingle_login_reward:give
