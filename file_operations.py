import pandas as pd

class FileOperator:
    def __init__(self, data: pd.DataFrame):
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")
        self.data = data

    def save_data_to_excel(self, file_path: str = 'output.xlsx'):
        if not isinstance(file_path, str):
            raise ValueError("File path must be a string.")
        self.data.to_excel(file_path)
