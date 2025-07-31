import requests

routes = ['http://localhost:8001/post-file-link-from-user',
          'http://localhost:8001/post-class-index-columns',
          'http://localhost:8001/train-model',
          'http://localhost:8001/test-model']

for route in routes:
    res = requests.post(route)
    print(res.content.decode())

data = ["youth","low","yes","fair"]
res = requests.post('http://127.0.0.1:8001/classify-record', json=data)
print(res.json())