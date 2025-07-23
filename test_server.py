import requests

routes = ['http://localhost:8000/post-file-link-from-user',
'http://localhost:8000/post-class-index-columns',
'http://localhost:8000/train-model',
'http://localhost:8000/test-model',
'http://localhost:8000/classify-record']

for route in routes:
    res = requests.post(route)
    print(res.content.decode())
