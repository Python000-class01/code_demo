import requests
 
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text) # '{"cookies": {"sessioncookie": "123456789"}}'


# 会话还可以用作前后文管理器：
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')