class CleanData:
    def __init__(self, df):
        self.df = df

    # set a column to index column
    def set_index(self, index_column):
        self.df = self.df.set_index(index_column)

    # convert the dataframe types to string
    def df_to_str(self):
        self.df = self.df.astype(str)