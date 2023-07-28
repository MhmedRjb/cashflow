import pandas as pd
import src.data.databaseIniti as dbi




class DataProcessor:
    def __init__(self, file_path: str, expected_cols: int) -> None:
        self.file_path = file_path
        self.expected_cols = expected_cols

    def read_data(self):
        funcname = 'read_data'
        classname = self.__class__.__name__
        try:
            self.data = pd.read_excel(self.file_path)
            if not set(self.expected_cols).issubset(self.data.columns):
                raise ValueError(f'The file does not contain the expected columns: {self.expected_cols}')
        except (FileNotFoundError, ImportError) as e:
            print(f'Error in {classname}.{funcname}: {e}')

if __name__ == "__main__":
    
    file_path_goods_transection = r"D:\monymovment\Cashflows\Excel_files\SBJRNLITMRPTTAX.xls"
    expected_cols_goods_transection = ['Acc_Nm' ,'sPrc', 'sQty', 'spkid']
    from src.data.DataBaseConnection import DatabaseExporter as dbcon
    username = dbi.username
    password = dbi.password
    hostname = dbi.hostname
    database = dbi.database
    exporter = dbcon(username, password, hostname, database)


    processor_goods_transection =DataProcessor(file_path_goods_transection, expected_cols_goods_transection)
    processor_goods_transection.read_data()

    print(processor_goods_transection.data.head(10))

    