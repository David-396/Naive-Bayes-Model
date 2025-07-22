class CleanData:
    def __init__(self, df):
        self.df = df

    def set_index(self, index_column):
        self.df = self.df.set_index(index_column)

    def df_to_str(self):
        self.df = self.df.astype(str)