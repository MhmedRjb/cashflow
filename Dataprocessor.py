import pandas as pd
import numpy as np
import openpyxl

class DataProcessor:
    def __init__(self, file_path, expected_cols):
        self.file_path = file_path
        self.expected_cols = expected_cols

    def read_data(self):
        try:
            self.data = pd.read_excel(self.file_path)
            if not set(self.expected_cols).issubset(self.data.columns):
                raise ValueError(f'The file does not contain the expected columns: {self.expected_cols}')
        except FileNotFoundError:
            print(f'Error: The file {self.file_path} was not found')
        except ImportError as e:
            print(f'Error: {e}')
        except Exception as e:
            print(f'Error: {e}')          
    def select_columns(self,wanted_cols):
        self.data = self.data[wanted_cols]

    def filter_row_null(self, column):
        self.data = self.data[self.data[column].notnull()]

    def filter_row (self, column, values):
        self.data = self.data[self.data[column].str.contains(values)]

    def clean_data(self):
        try:
            self.select_columns()
        except Exception as e:
            print(f'Error: {e}')

    def save_tables(self, output_file, tables, sheet_names):
        with pd.ExcelWriter(output_file) as writer:
            for table, sheet_name in zip(tables, sheet_names):
                table.to_excel(writer, index=False, sheet_name=sheet_name)
    def rename_columns(self, columns):
        self.data = self.data.rename(columns=columns)


if __name__ == "__main__":
    file_path_goods_transection = r"D:\monymovment\Cashflows\Excel_files\SBJRNLITMRPTTAX.xls"
    expected_cols_goods_transection = ['Acc_Nm', 'sCst', 'Text103', 'Text120', 'Text101', 'sPrc', 'sQty', 'spkid']
    wanted_cols_goods_transection = ['tr_dt', 'TR_NO', 'LN_NO', 'tr_ds', 'Text103', 'Acc_Nm']
    filter_column = 'tr_ds'
    filter_values = 'بيع|مرتجع'

    processor_goods_transection =DataProcessor(file_path_goods_transection, expected_cols_goods_transection)
    processor_goods_transection.read_data()
    processor_goods_transection.select_columns(wanted_cols_goods_transection)
    processor_goods_transection.filter_row(filter_column, filter_values)
    processor_goods_transection.rename_columns({ 'Text103': 'Total_invoice'})
    print(processor_goods_transection.data)

    file_path_clints_data= r"D:\monymovment\Cashflows\Excel_files\SBAccMFDtlRpt.xls"
    expected_cols_clints_data = ['rec_id', 'acc_cd', 'acc_nm', 'Text85', 'نص93']
    wanted_cols_clints_data = ['acc_nm', 'Text85', 'نص93']
    filter_column = 'acc_nm'

    processor_clints_data =DataProcessor(file_path_clints_data, expected_cols_clints_data)
    processor_clints_data.read_data()
    processor_clints_data.select_columns(wanted_cols_clints_data)
    processor_clints_data.filter_row_null(filter_column)
    print(processor_clints_data.data)

    processor_goods_transection.save_tables('output.xlsx', [processor_goods_transection.data, processor_clints_data.data], ['Sheet1', 'Sheet2'])




    

