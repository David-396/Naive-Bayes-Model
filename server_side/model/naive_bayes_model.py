class NaiveBayesBuildModel:
    def __init__(self, df, target_class_column):
        self.df = df                                            # the dataframe that the model will work on
        self.target_class_column = target_class_column          # the class column to ignore
        self.classified_data = self.model_train_data()          # the big dictionary with the all values in the dataframe
        self.class_value_precent_in_df = {}


    def model_train_data(self):
        data = {}
        target_vals = self.df[self.target_class_column].unique()
        self.class_value_precent_in_df = self.df[self.target_class_column].value_counts(normalize=True).to_dict()
        print(self.class_value_precent_in_df)

        for target in target_vals:
            target_data = self.df[self.df[self.target_class_column] == target]
            records_number = target_data.shape[0]
            data[target] = {}
            all_columns = list(self.df.columns)
            all_columns.remove(self.target_class_column)

            for column in all_columns:
                data[target][column] = {}
                uniq_vals = target_data[column].unique()

                for val in uniq_vals:
                    data[target][column][val] = (target_data[target_data[column] == val].shape[0] + 1) / (records_number + len(uniq_vals))

        return data