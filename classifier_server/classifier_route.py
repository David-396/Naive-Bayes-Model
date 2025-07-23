import json
from typing import List, Dict
import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse
from classifier import Classifier


my_classifier = None
app = FastAPI()


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


@app.get('/csv-classify')
def csv_classify(csv : Dict[str,str]):
    try:
        if my_classifier:
            return JSONResponse(my_classifier.csv_classified(csv), 200)

    except Exception as e:
        print(f'--- error classify csv file : {e} ---')
        return JSONResponse({'error' : 'post the classifier_server first in "/post-classifier_server-object" route.'}, 400)


@app.get('/classify-record')
def classify_record(record : List[str]):
    try:
        if my_classifier:
            result = my_classifier.record_classify(record)
            return JSONResponse(json.dumps(result), 200)

    except Exception as e:
        print(f'--- error classify csv file : {e} ---')
        return JSONResponse({'error': 'post the classifier_server first in "/post-classifier_server-object" route.'}, 400)


uvicorn.run(app, host='127.0.0.1', port=8001)