# class Menu:
#     def __init__(self):
#         self.df = None
#         self.classifier = None
#         self.model = None
#         self.tester = None
#         self.class_column = None
#         self.accuracy = None

    # # select the wanted csv file to work with - from the .\data\ directory
    # def select_and_clean_data(self):
    #     print_select_data()
    #     file_opt = input()
    #     data_files = get_files_in_folder('.\\data')
    #     while not validate.validate_input_options([str(num+1) for num in range(len(data_files))], file_opt):
    #         print(f'\nwrong input please enter the number of the option.\n')
    #         file_opt = input()
    #     file = f'.\\data\\{data_files[int(file_opt)-1]}'
    #
    #     self.from_data_to_clean_df(file)
    #     self.get_target_columns_in_df(self.df)

    # # get the target column for the model will return answer by this column - 'class' by default
    # def get_target_columns_in_df(self, df):
    #     columns = list(df.columns)
    #     print_select_target_column(columns)
    #     input_column = input()
    #     columns.append('')
    #     while not validate.validate_input_options([column for column in columns],input_column) :
    #         print('--- wrong column ---')
    #         input_column = input()
    #
    #     if input_column == '':
    #         self.class_column = columns[-2]
    #     else:
    #         self.class_column = input_column

    # # csv to clean dataframe
    # def from_data_to_clean_df(self, file):
    #     load_data = Loader(file)
    #     clean_data = CleanData(load_data.df)
    #     clean_data.set_index()
    #     self.df = clean_data.df



    # # for the second run - if select new dataframe
    # @staticmethod
    # def if_select_new_dataframe():
    #     print_select_new_df()
    #     opt = input()
    #     while not validate.validate_input_options(['1','2'], opt):
    #         opt = input('---- enter only the number of the option ---')
    #     if opt == '1':
    #         return True
    #     return False



    # # train the model with part of the dataframe
    # def train_model_from_the_df(self, precent_of_df_for_train):
    #     data_for_train = split_df_by_precent(self.df, precent_of_df_for_train)
    #     model = NaiveBayesBuildModel(data_for_train, self.class_column)
    #     self.model = model
    #     self.classifier = Predictor(self.df, self.model.classified_data, self.class_column)
    #     print('\nmodel started successfully\n')

    # # test how the model is accurate with part of the dataframe
    # def test_model_from_the_df(self, precent_of_df_for_test):
    #     print('\ntesting model..\n')
    #     tester = TestAccuracy(self.classifier)
    #     # data_for_test = split_df_by_precent(self.df, precent_of_df_for_test, from_bottom=True)
    #     data_for_test = self.df.sample(frac=1, random_state=33)
    #     self.accuracy = tester.test_accuracy(data_for_test)
    #     print(f'\nthe accuracy of the model is {self.accuracy}%\n')

    # # the user enters a record and the model will predict the result
    # def classify_data_by_record_input(self, record_to_classify):
    #     pass
    #
    # # the user enters a csv file and the model will predict the result
    # def classify_data_by_csv_file_input(self, csv_to_classify):
    #     pass


    # def run(self):
        # if not self.df:
        #     self.select_and_clean_data()
        # else:
        #     if self.if_select_new_dataframe():
        #         self.select_and_clean_data()

        # self.train_model_from_the_df(0.7)
        # self.test_model_from_the_df(0.3)
