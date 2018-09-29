import json
f = open("config.json",encoding='utf-8')
setting = json.load(f)
print(setting)
print(setting["PID_turn"])
print(setting["PID_turn"]["P"])
