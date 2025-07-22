import requests
from server_side.data_handling.data_cleaning import CleanData
from server_side.data_handling.data_loader import Loader
from server_side.model.naive_bayes_model import NaiveBayesBuildModel
from classifier.classifier import Classifier
from fastapi.responses import PlainTextResponse, JSONResponse
from server_side.model.test_accuracy import TestAccuracy
from fastapi.encoders import jsonable_encoder
from client_side.static import split_df_by_precent, dict_to_str

class Server:
    def __init__(self, classifier_url):
        self.classifier_url = classifier_url
        self.__df = None
        self.__class_column = None
        self.__index_column = None
        self.__all_columns = None
        self.__model = None
        self.__classifier = None
        self.__model_accuracy = None
        self.__unique_values_dict = None

    # get the csv file link
    def file_link_to_clean_df(self, file_info):
        try:
            # print(file_link, type(file_link))
            load_data = Loader(file_info['file_link'])
            self.__df = load_data.df
            self.__all_columns = [col for col in self.__df.columns]
            return self.__all_columns

        except Exception as e:
            print(f'--- error in to load the data file : {e} ---')
            return None

    # get the class column
    def get_class_index_columns(self, columns_info):
        try:
            # print(columns_info, type(columns_info))
            clean_data = CleanData(self.__df)
            clean_data.df_to_str()

            if columns_info['index_column']:
                self.__index_column = columns_info['index_column']
                clean_data.df.set_index(self.__index_column)

            self.__df = clean_data.df

            self.__class_column = columns_info['class_column']
            self.__unique_values_dict = self.unique_values_for_each_column()
            # print(self.unique_values_dict)
            return JSONResponse(jsonable_encoder(self.__unique_values_dict), 200)

        except Exception as e:
            print(f'--- error to get the class and index columns : {e} ---')
            return PlainTextResponse(None,400)

    # for returning to the client, the uniques values in each column and the user will choose one each column
    def unique_values_for_each_column(self):

        if self.__index_column:
            columns = [col for col in self.__all_columns if col != self.__index_column and col != self.__class_column]
        else:
            columns = [col for col in self.__all_columns if col != self.__class_column]

        unique_values_dict = {col:str(list(self.__df[col].unique())) for col in columns}
        return unique_values_dict






    # train the model with part of the dataframe
    def train_model_from_the_df(self, precent_of_df_for_train):
        try:
            data_for_train = split_df_by_precent(self.__df, precent_of_df_for_train)
            self.__model = NaiveBayesBuildModel(data_for_train, self.__class_column)
            self.__classifier = Classifier(self.__df, self.__model.classified_data, self.__class_column, self.__index_column)
            return PlainTextResponse('The Model Started Successfully!', 200)

        except Exception as e:
            print(f'--- error in training the model : {e} ---')
            return PlainTextResponse('error in training model. please try again!', 400)

    # test the model to get the success precent
    def test_model_from_the_df(self, precent_of_df_for_test):
        try:
            tester = TestAccuracy(self.__classifier)
            # data_for_test = split_df_by_precent(self.df, precent_of_df_for_test, from_bottom=True)
            data_for_test = self.__df.sample(frac=1, random_state=33)

            if self.__index_column:
                data_for_test = data_for_test.drop(columns=[self.__index_column])
            self.__model_accuracy = tester.test_accuracy(data_for_test)
            return PlainTextResponse(f'the accuracy of the model is {self.__model_accuracy}%', 200)

        except Exception as e:
            print(f'--- error in testing the model : {e} ---')
            return PlainTextResponse(f'error in testing model : {e}', 400)


    def send_classifier_to_cls_container(self):
        try:
            res = requests.post(f'http://{self.classifier_url}/post-classifier-object',
                                data=self.__classifier.classifier_to_obj())
            print(res)
            return res

        except Exception as e:
            print(f'--- error in sending to classifier server the classifier object : {e} ---')


    def classify_record(self, record):
        try:
            result = requests.get(f'http://{self.classifier_url}/classify-record', data=record)
            if "not enough values to predict" in result.content():
                return JSONResponse(result, 400)

            result = dict_to_str(result)
            print('result:' , result)
            return JSONResponse(result, 200)

        except Exception as e:
            print(f'--- error in classifying the record : {e} ---')
            return JSONResponse({'error':f'--- error in classifying the record : {e} ---'}, 400)





