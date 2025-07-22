from typing import List, Dict
import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse

from classifier import Classifier


my_classifier = None
app = FastAPI()


@app.post('/post-classifier-object')
def post_classifier_object(classifier : Dict[str,str]):
    try:
        global my_classifier
        my_classifier = Classifier(classifier['model_df'],
                                   classifier['classified_data_from_model'],
                                   classifier['target_class_column'],
                                   classifier['target_vals'])
        return JSONResponse({'success':'classifier accepted'}, 200)

    except Exception as e:
        print(f'--- error in post the classifier object : {e} ---')
        return JSONResponse({'error':f'--- error in post the classifier object : {e} ---'}, 400)

@app.get('/csv-classify')
def csv_classify(csv : Dict[str,str]):
    try:
        if my_classifier:
            return JSONResponse(my_classifier.csv_classified(csv), 200)

    except Exception as e:
        print(f'--- error classify csv file : {e} ---')
        return JSONResponse({'error' : 'post the classifier first in "/post-classifier-object" route.'}, 400)

@app.get('/classify-record')
def classify_record(record : List[str]):
    try:
        if my_classifier:
            return JSONResponse(my_classifier.record_classify(record), 200)

    except Exception as e:
        print(f'--- error classify csv file : {e} ---')
        return JSONResponse({'error': 'post the classifier first in "/post-classifier-object" route.'}, 400)


uvicorn.run(app, host='0.0.0.0', port=5000)