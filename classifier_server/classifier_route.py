import json
from typing import List, Dict
import requests
import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse
from classifier import Classifier


MAIN_SERVER_IP = 'localhost'
MAIN_SERVER_PORT = 8000

my_classifier = None
app = FastAPI()


# the only route for the user - give a list to classify and return the result
@app.get('/classify-record')
def classify_record(record : List[str]):
    try:
        if not my_classifier:
            get_model_from_main_server(main_server_ip=MAIN_SERVER_IP, main_server_port=MAIN_SERVER_PORT)

        result = my_classifier.record_classify(record)
        return JSONResponse(json.dumps(result), 200)

    except Exception as e:
        print(f'--- error classify the record : {e} ---')
        return JSONResponse({'error': 'error in the record classifying. please try again later.'}, 400)


# if there is not a classifier object - make a get request to get the classifier
def get_model_from_main_server(main_server_ip, main_server_port):
    classifier_from_server = requests.get(f"http://{main_server_ip}:{main_server_port}/get-model").json()

    global my_classifier

    my_classifier = Classifier(classifier_from_server['classified_data_from_model'],
                                classifier_from_server['target_vals'],
                                classifier_from_server['target_class_column'],
                                classifier_from_server['index_col'],
                                classifier_from_server['class_value_precent_in_df'],
                                classifier_from_server['all_columns'])


uvicorn.run(app, host='127.0.0.1', port=8001)
