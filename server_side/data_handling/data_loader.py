import pandas as pd

class Loader:
    def __init__(self, path):
        self.path = path
        self.df = self.load_data()

    # load the csv file to dataframe
    def load_data(self):
        try:
            df = pd.read_csv(self.path)
            return df
        except FileExistsError:
            print('--- file not exist ---')
        except Exception as e:
            print(f'--- {e} ---')
