import requests

routes = ['http://localhost:8000/post-file-link-from-user',
'http://localhost:8000/post-class-index-columns',
'http://localhost:8000/train-model',
'http://localhost:8000/test-model',
'http://localhost:8000/classify-record']

for route in routes:
    res = requests.post(route)
    print(res.content.decode())



'''/* sending requests */'''
# @app.post('/classify-record')
    # # def classify(record : List[str]):
    # #     return my_server.classify_record(record)
    # def classify():
    #     result = my_server.classify_record(["1","1","1","1"]).body.decode()
    #     result = result.replace('\\"', '"')[1:-1]
    #     result = json.loads(result)
    #     result = get_max_classify_from_record(result)
    #     return result


# def classify_record(self, record):
#     try:
#         record = json.dumps(record)
#         result = requests.get(f'http://{self.classifier_ip}:{self.classifier_port}/classify-record', data=record)
#         return JSONResponse(result.json(), result.status_code)
#
#     except Exception as e:
#         print(f'--- error in classifying the record : {e} ---')
#         return JSONResponse({'error':f'--- error in classifying the record : {e} ---'}, 400)
