class NaiveBayesBuildModel:
    def __init__(self, df, target_class_column, index_column):
        self.df = df                                            # the dataframe that the model will work on
        self.target_class_column = target_class_column          # the class column to ignore
        self.total_records = len(df)                            # number of all records in df
        self.class_value_precent_in_df = {}                     # how much each class value in the df in percents
        self.target_vals = list(self.df[self.target_class_column].unique())           # all the values in the class column
        self.index_column = index_column                        # the index column to ignore

        # if index_column:
        self.all_columns = [col for col in self.df.columns if col != self.target_class_column and col != index_column]      # all the columns except the index and class columns, if index
        # else:
        #     self.all_columns = [col for col in self.df.columns if col != self.target_class_column]

        self.classified_data = self.model_train_data()          # the big dictionary with the all values in the dataframe


    # training the model from the dataframe
    def model_train_data(self):
        data = {}

        for target in self.target_vals:
            self.class_value_precent_in_df[target] = self.df[self.df[self.target_class_column] == target].shape[0] / self.total_records

            target_data = self.df[self.df[self.target_class_column] == target]
            records_number = target_data.shape[0]
            data[target] = {}

            for column in self.all_columns:
                data[target][column] = {}
                uniq_vals = target_data[column].unique()

                for val in uniq_vals:
                    data[target][column][val] = (target_data[target_data[column] == val].shape[0] + 1) / (records_number + len(uniq_vals))

        return data