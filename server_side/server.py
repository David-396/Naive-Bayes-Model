import json
import requests
from data_handling.data_cleaning import CleanData
from data_handling.data_loader import Loader
from model.naive_bayes_model import NaiveBayesBuildModel
from model.classifier import Classifier
from fastapi.responses import PlainTextResponse, JSONResponse
from model.test_accuracy import TestAccuracy
from fastapi.encoders import jsonable_encoder
from server_statics.statics import split_df_by_precent, dict_to_str

class Server:
    def __init__(self, classifier_ip, classifier_port):
        self.classifier_ip = classifier_ip
        self.classifier_port = classifier_port
        self.__df = None
        self.__class_column = None
        self.__index_column = None
        self.__all_columns = None
        self.__model = None
        self.__classifier = None
        self.__model_accuracy = None
        self.__unique_values_dict = None
    @property
    def model(self):
        return self.__classifier.classifier_to_dict()

    ''' setting the dataframe '''
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

    # get the class and index columns
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

    # returning the unique values for each column
    def unique_values_for_each_column(self):

        if self.__index_column:
            columns = [col for col in self.__all_columns if col != self.__index_column and col != self.__class_column]
        else:
            columns = [col for col in self.__all_columns if col != self.__class_column]

        unique_values_dict = {col:str(list(self.__df[col].unique())) for col in columns}
        return unique_values_dict


    ''' training and testing model and sending to cls server '''
    # train the model with part of the dataframe
    def train_model_from_the_df(self, precent_of_df_for_train):
        try:
            data_for_train = split_df_by_precent(self.__df,
                                                 precent_of_df_for_train)

            self.__model = NaiveBayesBuildModel(data_for_train,
                                                self.__class_column,
                                                self.__index_column)

            self.__classifier = Classifier(self.__model.classified_data,
                                           self.__model.target_vals,
                                           self.__class_column,
                                           self.__index_column,
                                           self.__model.class_value_precent_in_df,
                                           self.__model.all_columns)

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


    # send the classifier object to the cls server
    def send_classifier_to_cls_container(self):
        try:
            print('sending classifier to cls server...')
            classifier_obj = json.dumps(self.__classifier.classifier_to_dict())
            res = requests.post(f'http://{self.classifier_ip}:{self.classifier_port}/post-classifier_server-object',
                                data=classifier_obj)

            print("classifier_server sent.")
            return {'classifier server route':f'http://{self.classifier_ip}:{self.classifier_port}/classify-record'}

        except Exception as e:
            print(f'--- error in sending to classifier_server server the classifier_server object : {e} ---')







