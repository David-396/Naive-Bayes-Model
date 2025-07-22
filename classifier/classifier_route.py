from typing import List, Dict
import uvicorn
from fastapi import FastAPI
from classifier import Classifier


my_classifier = None
app = FastAPI()


@app.post('/post-classifier-object')
def post_classifier_object(classifier):
    global my_classifier
    my_classifier = classifier
    return {'success':'classifier accepted'}

@app.get('/csv-classify')
def csv_classify(csv : Dict[str,str]):
    if my_classifier:
        return my_classifier.csv_classified(csv)
    return {'error' : 'post the classifier first in "/post-classifier-object" route.'}, 400

@app.get('/classify-record')
def classify_record(record : List[str]):
    if my_classifier:
        return my_classifier.record_classify(record)
    return {'error': 'post the classifier first in "/post-classifier-object" route.'}, 400


uvicorn.run(app, host='0.0.0.0', port=5000)