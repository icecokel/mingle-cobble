scoreboard objectives add ml_login_clock dummy "Login Reward Clock"
scoreboard objectives add ml_login_seen dummy "Login Reward Seen"
scoreboard objectives add ml_login_last dummy "Login Reward Last"
scoreboard objectives add ml_login_elapsed dummy "Login Reward Elapsed"

scoreboard players add #server_seconds ml_login_clock 0

schedule function mingle_login_reward:clock 1s replace
schedule function mingle_login_reward:check 5s replace
