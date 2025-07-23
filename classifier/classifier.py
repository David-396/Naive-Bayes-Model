import pandas as pd


class Classifier:
    def __init__(self, model_df, classified_data_from_model, target_class_column, index_col, class_value_precent_in_df):
        self.model_df = model_df                                                # a dataframe from the model to work with
        self.classified_data_from_model = classified_data_from_model            # the big dictionary with the all values from the dataframe
        self.target_class_column = target_class_column                          # the class column to ignore from
        self.target_vals = self.model_df[self.target_class_column].unique()     # all the unique values of the class column

        if index_col:
            self.all_columns = [col for col in self.model_df.columns if col!=self.target_class_column and col!= index_col]    # all columns in the dataframe except class, index cols if it has index
        else:
            self.all_columns = [col for col in self.model_df.columns if col != self.target_class_column]                      # all columns except class if not has index

        self.record_len_required = len(self.all_columns)                        # how much parameters each record should have to predict
        self.total_records = len(self.model_df)                                 # len of the dataframe
        self.class_value_precent_in_df = class_value_precent_in_df              # percent for each class value in the all df


    def csv_classified(self, df_to_classify):
        classifier = {}
        if self.target_class_column in df_to_classify.columns:
            df_to_classify = df_to_classify.drop(columns=[self.target_class_column])

        for i in range(df_to_classify.shape[0]):
            classifier[i] = self.record_classify(df_to_classify.iloc[i])

        return classifier



    def record_classify(self, record):
        # print(len(record) , self.record_len_required)
        if len(record) == self.record_len_required:
            record = pd.Series(record)
            classifier = {}

            for target in self.target_vals:
                # classifier[target] = self.model_df[self.model_df[self.target_class_column] == target].shape[0] / self.total_records
                classifier[target] = self.class_value_precent_in_df[target]

                for i in range(self.record_len_required):
                    classifier[target] *= self.classified_data_from_model[target][self.all_columns[i]].get(record.iloc[i], 1e-6)

            return classifier

        else:
            print(f'--- not enough values to predict, please enter {self.record_len_required} values. (entered {len(record)}) ---')
            return {"not enough values to predict":None}


    def classifier_to_obj(self):
        return {"model_df": self.model_df,
                "classified_data_from_model": self.classified_data_from_model,
                "target_class_column": self.target_class_column,
                "target_vals": self.target_vals}
