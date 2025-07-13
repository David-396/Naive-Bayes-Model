import json
import os
import requests
import validate
from prints import print_select_target_column, print_select_data, print_select_new_df, print_select_index_column
from static import get_files_in_folder, get_max_classify_from_record


class Client:
    def __init__(self, server_link):
        self.server_link = server_link
        self.file_link = None
        self.all_columns = None
        self.unique_vals = None


    # select the wanted csv file to work with - from the .\data\ directory
    def select_file_link(self):
        if_exit = False

        while not if_exit:

                print_select_data()
                file_opt = input()
                data_files = get_files_in_folder('.\\data')
                valid_options = [str(num+1) for num in range(len(data_files))]
                while not validate.validate_input_options(valid_options, file_opt):
                    print(f'--- wrong input please enter the number of the option. ---')
                    file_opt = input()

                file = os.path.join('data', data_files[int(file_opt)-1])
                try:
                    res = requests.post(f'{self.server_link}/post-file-link-from-user', json={'file_link':file}, timeout=10)
                    self.file_link = file
                    self.all_columns = res.json()
                    # print(columns, type(columns))
                    self.get_index_and_target_columns_in_df(self.all_columns)
                    if_exit = True

                except requests.exceptions.RequestException as e:
                    print(f'--- error with the connect to the server: {e} ---')
                    retry = input('try again? (y/n): ')

                    while not validate.validate_input_options(['y','n'],retry):
                        print('--- wrong option ---')
                        retry = input()
                    if retry.lower() == 'n':
                        if_exit = True

    # for the second run - if select new dataframe
    @staticmethod
    def if_select_new_dataframe():
        print_select_new_df()
        opt = input()
        while not validate.validate_input_options(['1', '2'], opt):
            opt = input('---- enter only the number of the option ---')
        if opt == '1':
            return True
        return False

    # get the target column for the model will return answer by this column - 'class' by default
    def get_index_and_target_columns_in_df(self, all_columns:list):
        exit_loop = False
        while not exit_loop:
            index_column = self.get_index_column(self.all_columns)

            print_select_target_column(all_columns)
            input_target_column = input()

            while not validate.validate_input_options(all_columns, input_target_column) and input_target_column != '':
                print('--- wrong column ---')
                input_target_column = input()

            if input_target_column == '':
                input_target_column = all_columns[-1]
            data = {'class_column':input_target_column, 'index_column':index_column}
            # print(data)
            res = requests.post(f'{self.server_link}/post-class-index-columns', json=data)
            if not res.content:
                print('--- ERROR to post the column. please try again ---')
            else:
                self.unique_vals = res.json()
                exit_loop = True


    @staticmethod
    def get_index_column(columns):
        print_select_index_column(columns)
        default_col = 'Index' if 'Index' in columns else None
        if default_col:
            print('\npress Enter if the index class is the "Index" column.')

        exit_input = False
        input_col = ''
        while not exit_input:
            input_col = input().strip()

            if input_col == '' and default_col:
                input_col = 'Index'
                exit_input = True

            elif validate.validate_input_options(columns, input_col):
                exit_input = True

            else:
                print('--- invalid column ---')

        return input_col


    # train the model from the dataframe
    def train_model(self):
        res = requests.post(f'{self.server_link}/train-model')
        print(res.text)
        if res.status_code == 200:
            return True
        return False

    # test the model accuracy
    def test_model(self):
        print('testing model...')
        res = requests.post(f'{self.server_link}/test-model')
        print(res.text)

    # classify an input row
    def classify_data(self):
        record_vals = []
        for col in self.unique_vals.keys():
            possible_vals = self.unique_vals[col]
            print(f'enter a value for {col} column (possible values: {possible_vals}):')
            input_val = input()

            while input_val == '':
                print('--- enter a value ---')
                input_val = input()

            record_vals.append(input_val)

        res = requests.post(f'{self.server_link}/classify-record', json=record_vals)
        classifier_result = res.json()

        if res.status_code == 200:
            for k,v in classifier_result.items():
                print(f'{k} class has {v}%')
            print(f'\nso the result of the record will be: {get_max_classify_from_record(classifier_result)}')

        else:
            print(classifier_result)




    # main function
    def run(self):
        if not self.file_link:
            self.select_file_link()
        else:
            if self.if_select_new_dataframe():
                self.select_file_link()

        if self.train_model():
            self.test_model()
            self.classify_data()
