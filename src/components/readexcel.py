import pandas as pd
class readexcel:
    def __init__(self, file_path: str, expected_cols: int) -> None:
        self.file_path = file_path
        self.expected_cols = expected_cols
        

    def read_data(self):
        try:
            self.data = pd.read_excel(self.file_path)
            print(self.data)
            if not set(self.expected_cols).issubset(self.data.columns):
                raise ValueError(f'The file does not contain the expected columns: {self.expected_cols}')
        except (FileNotFoundError, ImportError) as e:
            print(f'Error in readexcel.read_data {e}')
