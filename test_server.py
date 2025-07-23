import requests

route = 'http://127.0.0.1:8001/classify-record'
data = ["1","1","7","8"]
res = requests.get(route, json=data)
print(res.json())
