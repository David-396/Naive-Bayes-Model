import uvicorn
from fastapi import FastAPI
from server import Server


def server_run(main_server_ip, main_server_port):

    app = FastAPI()

    @app.get('/get-model')
    def get_model():
        server = Server()

        # load the dataframe from the link and clean it
        print('loading and cleaning the dataframe')
        file_path = "./data/DATA.csv"
        server.file_link_to_clean_df({'file_link': file_path})

        # get the index and class columns to order the dataframe
        print('ordering the dataframe...')
        class_index_columns = {"index_column": "id", "class_column": "Buy_Computer"}
        server.get_class_index_columns(class_index_columns)

        # training the model
        print('training...')
        server.train_model_from_the_df(0.7)

        # testing the model
        print('testing...')
        server.test_model_from_the_df(0.3)

        # sending the classifier model to the cls server
        model = server.get_classifier
        return model


    uvicorn.run(app, host=main_server_ip, port=main_server_port)

