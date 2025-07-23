import json
import uvicorn
from typing import Dict, List
from fastapi import FastAPI
from server_side.server import Server
from server_side.server_statics.statics import get_max_classify_from_record


def server_run(classifier_ip, classifier_port, host='0.0.0.0', port=8000):

    app = FastAPI()
    my_server = Server(classifier_ip, classifier_port)

    @app.get('/test-if-works')
    def test_if_works():
        return {'status':'working'}

    @app.post('/post-file-link-from-user')
    # def post_file_to_sever(file_info_dict : Dict[str,str]):
        # return my_server.file_link_to_clean_df(file_info_dict)
    def post_file_to_sever():
        return my_server.file_link_to_clean_df({'file_link':r'../Naive_Bayes/data/DATA.csv'})

    @app.post('/post-class-index-columns')
    # def post_class_and_index_column(columns_info_dict : Dict[str,object]):
    #     return my_server.get_class_index_columns(columns_info_dict)
    def post_class_and_index_column():
        return my_server.get_class_index_columns({"index_column":"id", "class_column":"Buy_Computer"})

    @app.post('/train-model')
    def train_model():
        return my_server.train_model_from_the_df(0.7)

    @app.post('/test-model')
    def test_model():
        accuracy_and_classifier_route = my_server.send_classifier_to_cls_container()
        accuracy_and_classifier_route['accuracy'] = my_server.test_model_from_the_df(0.3).body
        return accuracy_and_classifier_route



    # @app.post('/classify-record')
    # # def classify(record : List[str]):
    # #     return my_server.classify_record(record)
    # def classify():
    #     result = my_server.classify_record(["1","1","1","1"]).body.decode()
    #     result = result.replace('\\"', '"')[1:-1]
    #     result = json.loads(result)
    #     result = get_max_classify_from_record(result)
    #     return result


    uvicorn.run(app, host=host, port=port)
