class CleanData:
    def __init__(self, df):
        self.df = df

    # set an index column to index
    def set_index(self, index_column):
        self.df = self.df.set_index(index_column)

    # converting the dataframe to string
    def df_to_str(self):
        self.df = self.df.astype(str)