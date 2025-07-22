import uvicorn
from typing import Dict, List
from fastapi import FastAPI
from server_side.server import Server




def server_run(host='0.0.0.0', port=8000):

    app = FastAPI()
    my_server = Server('localhost:5000')

    @app.get('/test-if-works')
    def test_if_works():
        return {'status':'working'}

    @app.post('/post-file-link-from-user')
    # def post_file_to_sever(file_info_dict : Dict[str,str]):
        # print(file_link, type(file_link))
        # return my_server.file_link_to_clean_df(file_info_dict)
    def post_file_to_sever():
        return my_server.file_link_to_clean_df({'file_link':r'../Naive_Bayes/data/DATA.csv'})

    @app.post('/post-class-index-columns')
    # def post_class_and_index_column(columns_info_dict : Dict[str,object]):
    #     # print(columns_info_dict, type(columns_info_dict))
    #     return my_server.get_class_index_columns(columns_info_dict)
    def post_class_and_index_column():
        return my_server.get_class_index_columns({"index_column":"id", "class_column":"Buy_Computer"})

    @app.post('/train-model')
    def train_model():
        return my_server.train_model_from_the_df(0.7)

    @app.post('/test-model')
    def test_model():
        return my_server.send_classifier_to_cls_container(), my_server.test_model_from_the_df(0.3)



    @app.post('/classify-record')
    # def classify(record : List[str]):
    #     return my_server.classify_record(record)
    def classify():
        return my_server.classify_record(["1","1","1","1"])


    uvicorn.run(app, host=host, port=port)
