from typing import Dict, List
from fastapi import FastAPI
from server import Server


app = FastAPI()
server = Server()

@app.post('/post-file-link-from-user')
def post_file_to_sever(file_info_dict : Dict[str,str]):
    # print(file_link, type(file_link))
    return server.file_link_to_clean_df(file_info_dict)

@app.post('/post-class-index-columns')
def post_class_and_index_column(columns_info_dict : Dict[str,str]):
    # print(class_column, type(class_column))
    return server.get_class_index_columns(columns_info_dict)

@app.post('/train-model')
def train_model():
    return server.train_model_from_the_df(0.7)

@app.post('/test-model')
def test_model():
    return server.test_model_from_the_df(0.3)

@app.post('/classify-record')
def classify(record : List[str]):
    return server.classify_record(record)