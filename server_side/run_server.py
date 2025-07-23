import json
import uvicorn
from typing import Dict, List
from fastapi import FastAPI
from server import Server
from server_statics.statics import get_max_classify_from_record



def server_run(classifier_ip, classifier_port, host='0.0.0.0', port=8000):

    app = FastAPI()
    my_server = Server(classifier_ip, classifier_port)

    ''' simple check if the server working '''
    @app.get('/test-if-works')
    def test_if_works():
        return {'status':'working'}

    ''' get the file path from the user '''
    @app.post('/post-file-link-from-user')
    # def post_file_to_sever(file_info_dict : Dict[str,str]):
        # return my_server.file_link_to_clean_df(file_info_dict)
    def post_file_to_sever():
        return my_server.file_link_to_clean_df({'file_link':r'./data/DATA.csv'})

    ''' get the index and class column from user '''
    @app.post('/post-class-index-columns')
    # def post_class_and_index_column(columns_info_dict : Dict[str,object]):
    #     return my_server.get_class_index_columns(columns_info_dict)
    def post_class_and_index_column():
        return my_server.get_class_index_columns({"index_column":"id", "class_column":"Buy_Computer"})

    ''' train the model from the dataframe '''
    @app.post('/train-model')
    def train_model():
        return my_server.train_model_from_the_df(0.7)

    ''' testing the model and sending to the classifier server the classifier object '''
    @app.post('/test-model')
    def test_model():
        accuracy_and_classifier_route = my_server.send_classifier_to_cls_container()
        accuracy_and_classifier_route['accuracy'] = my_server.test_model_from_the_df(0.3).body
        return accuracy_and_classifier_route

    uvicorn.run(app, host=host, port=port)

