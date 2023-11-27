import pandas as pd


class DataManager:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_parquet(self.data_path)
            return self.data
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False

    def get_char_data(self):
        return self.data.select_dtypes(include=["object"])

    def get_num_data(self):
        return self.data.select_dtypes(include=["number"])

    def get_npr_data(self):
        return self.data[["description", "type_unified"]]

    def get_clean_npr_data(self):
        return self.get_npr_data().dropna()
