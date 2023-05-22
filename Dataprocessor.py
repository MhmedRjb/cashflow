import pandas as pd
import numpy as np
import openpyxl
import random
import string
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

    def ApplyDICtToCol(self, column,replacements):
        
        data = self.data.copy()
        data[column] = data[column].replace(replacements)
        self.data = data    
 
    def creat_primary_key(self, columns, format_columns=None,pk_column='pk'):
        # create a copy of the data
        data = self.data.copy()
        
        # format the specified columns
        if format_columns:
            for column, length in format_columns.items():
                data[column] = data[column].apply(lambda x: f'{x:0{length}d}')
        
        # create the primary key
        data[pk_column] = data[columns].apply(lambda row: ''.join(row.values.astype(str)), axis=1)
        # update the data with the new primary key
        self.data = data
    def rename_columns(self, columns):
        self.data = self.data.rename(columns=columns)

    def select_columns(self,wanted_cols):
        self.data = self.data[wanted_cols]

    def filter_row_null(self, column):
        self.data = self.data[self.data[column].notnull()]

    def filter_row (self, column, values):
        self.data = self.data[self.data[column].str.contains(values)]

    #def for group by col and sum col and left other col
    # def groupby_sum(self, groupby_col, sum_col, keep_cols):
    #     self.data = self.data.groupby(groupby_col).agg({**{col: 'first' for col in keep_cols}, **{sum_col: 'sum'}}).reset_index()
    def groupby_agg(self, groupby_col, agg_dict):
        self.data = self.data.groupby(groupby_col).agg(agg_dict).reset_index()

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
    processor_goods_transection.ApplyDICtToCol(['tr_ds', 'TR_NO', 'LN_NO'])
    processor_goods_transection.creat_primary_key(['tr_ds', 'TR_NO', 'LN_NO'],  {'TR_NO': 4, 'LN_NO': 2})
    processor_goods_transection.add_random_column('random')
    print(processor_goods_transection.data)
    hadder=processor_goods_transection
    print(hadder.data)

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
