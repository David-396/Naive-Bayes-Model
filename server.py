import json
from typing import Dict, Any, List
import pandas as pd
from fastapi import FastAPI
import validate
from data_cleaning import CleanData
from data_loader import Loader
from naive_bayes_model import NaiveBayesBuildModel
from predictor import Predictor
from static import split_df_by_precent, dict_to_str
from fastapi.responses import PlainTextResponse, JSONResponse
from test_accuracy import TestAccuracy
from fastapi.encoders import jsonable_encoder


class Server:
    def __init__(self):
        self.df = None
        self.class_column = None
        self.index_column = None
        self.all_columns = None
        self.model = None
        self.classifier = None
        self.model_accuracy = None
        self.unique_values_dict = None

    # get the csv file link
    def file_link_to_clean_df(self, file_info):
        try:
            # print(file_link, type(file_link))
            load_data = Loader(file_info['file_link'])
            self.df = load_data.df
            self.all_columns = [col for col in self.df.columns]
            return self.all_columns

        except Exception as e:
            print(e)
            return None

    # get the class column
    def get_class_index_columns(self, columns_info):
        try:
            # print(column, type(column))
            clean_data = CleanData(self.df)
            self.index_column = columns_info['index_column']
            clean_data.df.set_index(self.index_column)
            self.class_column = columns_info['class_column']
            self.unique_values_dict = self.unique_values_for_each_column()
            # print(self.unique_values_dict)
            return JSONResponse(jsonable_encoder(self.unique_values_dict), 200)

        except Exception as e:
            print(e)
            return PlainTextResponse(None,400)

    def unique_values_for_each_column(self):
        columns = [col for col in self.all_columns if col != self.index_column and col != self.class_column]
        unique_values_dict = {col:str(list(self.df[col].unique())) for col in columns}
        return unique_values_dict






    # train the model with part of the dataframe
    def train_model_from_the_df(self, precent_of_df_for_train):
        try:
            data_for_train = split_df_by_precent(self.df, precent_of_df_for_train)
            self.model = NaiveBayesBuildModel(data_for_train, self.class_column)
            self.classifier = Predictor(self.df, self.model.classified_data, self.class_column, self.index_column)
            return PlainTextResponse('The Model Started Successfully!', 200)
        except Exception as e:
            print(e)
            return PlainTextResponse('error in training model. please try again!', 400)

    # test the model to get the success precent
    def test_model_from_the_df(self, precent_of_df_for_test):
        try:
            tester = TestAccuracy(self.classifier)
            # data_for_test = split_df_by_precent(self.df, precent_of_df_for_test, from_bottom=True)
            data_for_test = self.df.sample(frac=1, random_state=33)
            data_for_test = data_for_test.drop(columns=[self.index_column])
            self.model_accuracy = tester.test_accuracy(data_for_test)
            return PlainTextResponse(f'the accuracy of the model is {self.model_accuracy}%', status_code=200)

        except Exception as e:
            return PlainTextResponse(f'error in testing data. {e}', 400)

    def classify_record(self, record):
        result = self.classifier.record_classify(record)
        if "not enough values to predict" in result:
            return JSONResponse(result, 400)

        result = dict_to_str(result)
        print('result:' , result)
        return JSONResponse(result, 200)
