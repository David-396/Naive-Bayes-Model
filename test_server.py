import requests

# route to port 8003 on localhost - route to cls server on port 8001 (8003:8001)
route = 'http://127.0.0.1:8003/classify-record'
data = ["1","1","7","8"]
res = requests.get(route, json=data)
print(res.json())
