import pandas as pd


class Classifier:
    def __init__(self, classified_data_from_model, target_vals, target_class_column, index_col, class_value_precent_in_df, all_columns):
        self.classified_data_from_model = classified_data_from_model            # the big dictionary with the all values from the dataframe
        self.target_class_column = target_class_column                          # the class column to ignore from
        self.index_col = index_col
        self.target_vals = target_vals                                          # all the unique values of the class column
        self.all_columns = all_columns                                          # all columns in the dataframe except class, index cols
        self.record_len_required = len(self.all_columns)                        # how much parameters each record should have to predict
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
                classifier[target] = self.class_value_precent_in_df[target]

                for i in range(self.record_len_required):
                    classifier[target] *= self.classified_data_from_model[target][self.all_columns[i]].get(record.iloc[i], 1e-6)

            return classifier

        else:
            print(f'--- not enough values to predict, please enter {self.record_len_required} values. (entered {len(record)}) ---')
            return {"not enough values to predict":None}


    def classifier_to_dict(self):
        return {"classified_data_from_model":self.classified_data_from_model,
                "target_class_column":self.target_class_column,
                "index_col":self.index_col,
                "target_vals":self.target_vals,
                "all_columns":self.all_columns,
                "record_len_required":self.record_len_required,
                "class_value_precent_in_df":self.class_value_precent_in_df}