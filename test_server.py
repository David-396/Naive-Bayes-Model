import requests

routes = ['http://localhost:8001/post-file-link-from-user',
          'http://localhost:8001/post-class-index-columns',
          'http://localhost:8001/train-model',
          'http://localhost:8001/test-model']

for route in routes:
    res = requests.post(route)
    print(res.json())

res = requests.get('http://127.0.0.1:8003/classify-record', json=["senior","high","no","fair"])
print(res.json())