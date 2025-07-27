import json
from typing import List, Dict
import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse
from classifier import Classifier


CLASSIFIER_IP = 'cls_server_container__v2.0'
CLASSIFIER_PORT = 8001

MAIN_SERVER_IP = 'main_server_container__v2.0'
MAIN_SERVER_PORT = 8000

my_classifier = None
app = FastAPI()


# getting the classifier object and save it
@app.post('/post-classifier_server-object')
def post_classifier_object(classifier : Dict[str,object]):
    try:
        global my_classifier
        my_classifier = Classifier(classifier['classified_data_from_model'],
                                   classifier['target_vals'],
                                   classifier['target_class_column'],
                                   classifier['index_col'],
                                   classifier['class_value_precent_in_df'],
                                   classifier['all_columns'])

        return JSONResponse({'success':'classifier_server accepted'}, 200)

    except Exception as e:
        print(f'--- error in post the classifier_server object : {e} ---')
        return JSONResponse({'error':f'--- error in post the classifier_server object : {e} ---'}, 400)

# classify a csv
@app.get('/csv-classify')
def csv_classify(csv : Dict[str,str]):
    try:
        if my_classifier:
            return JSONResponse(my_classifier.csv_classified(csv), 200)

    except Exception as e:
        print(f'--- error classify csv file : {e} ---')
        return JSONResponse({'error' : 'post the classifier_server first in "/post-classifier_server-object" route.'}, 400)

# classify a record input
@app.get('/classify-record')
def classify_record(record : List[str]):
    try:
        if my_classifier:

            result = my_classifier.record_classify(record)
            return JSONResponse(json.dumps(result), 200)

    except Exception as e:
        print(f'--- error classify the record : {e} ---')
        return JSONResponse({'error': 'error in the record classifying. please try again later.'}, 400)



uvicorn.run(app, host=CLASSIFIER_IP, port=CLASSIFIER_PORT)





