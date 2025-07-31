import requests

# route to port 8003 on localhost - to cls server on port 8001 within the container (8003:8001)
route = 'http://127.0.0.1:8003/classify-record'

# test 1
data_for_data = ["1","1","no","fair"]
data_for_phishing = [
    "1", "0", "1", "1", "1", "-1", "0", "1", "-1", "1",
    "1", "-1", "1", "0", "1", "1", "1", "-1", "0", "1",
    "-1", "1", "1", "-1", "-1", "0", "-1", "1", "0", "1"
]

res = requests.get(route, json=data_for_data)
# res = requests.get(route, json=data_for_phishing)
print(res.json())

# test 2
data_for_phishing2 = [
    "1", "0", "1", "1", "1", "-1", "-1", "-1", "-1", "1",
    "1", "-1", "1", "0", "-1", "-1", "-1", "-1", "0", "1",
    "1", "1", "1", "1", "-1", "1", "-1", "1", "0", "-1"
]
data_for_data2 =  ["senior","high","yes","fair"]

res = requests.get(route, json=data_for_data2)
# res = requests.get(route, json=data_for_phishing2)
print(res.json())
