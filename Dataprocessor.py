import pandas as pd
import numpy as np
import openpyxl
from error import ErrorHandler




class DataProcessor:
    def __init__(self, file_path: str, expected_cols: int) -> None:
        self.file_path = file_path
        self.expected_cols = expected_cols
        self.error_handler = ErrorHandler()


    def read_data(self):
        funcname = 'read_data'
        classname = self.__class__.__name__

        try:
            self.data = pd.read_excel(self.file_path)
            if not set(self.expected_cols).issubset(self.data.columns):
                raise ValueError(f'The file does not contain the expected columns: {self.expected_cols}')
        except (FileNotFoundError, ImportError) as e:
            self.error_handler.handle_error(e, classname, funcname)


    def ApplyDICtToCol(self, column:str,replacements:dict)->None:
        data = self.data.copy()
        data[column] = data[column].replace(replacements)
        self.data = data    
        
    def format_columns(self, columns, length):
        # format the specified columns
        for column in columns:
            self.data[column] = self.data[column].apply(lambda x: f'{x:0{length}d}')
        
    def add_primary_key(self, columns, pk_column='pk'):
        self.data[pk_column] = self.data[columns].apply(lambda row: ''.join(row.values.astype(str)), axis=1)
        
    def rename_columns(self, columns):
        self.data = self.data.rename(columns=columns)

    def select_columns(self,wanted_cols):
        self.data = self.data[wanted_cols]

    def filter_row_null(self, column):
        self.data = self.data[self.data[column].notnull()]

    def filter_row (self, column, values):
        self.data = self.data[self.data[column].str.contains(values)]

    def groupby_agg(self, groupby_col, agg_dict):
        self.data = self.data.groupby(groupby_col).agg(agg_dict).reset_index()
        
    #filter row in df if not in another df
    def filter_row_not_in(self, df1,df2,col1,col2):
        df1 = df1[~df1[col1].isin(df2[col2])]        
    

if __name__ == "__main__":
    
    file_path_goods_transection = r"D:\monymovment\Cashflows\Excel_files\SBJRNLITMRPTTAX.xls"
    expected_cols_goods_transection = ['Acc_Nm' ,'sPrc', 'sQty', 'spkid']
    wanted_cols_goods_transection = ['tr_dt', 'TR_NO', 'tr_ds', 'Text103', 'Acc_Nm']
    filter_column = 'tr_ds'
    filter_values = 'بيع|مرتجع'
    filter_column2 = 'Acc_Nm'
    filter_vlaues2 = 'الصعيدى|العابد|البدر|خزين|ايتوال|اليسر|ع-لولو|ع-بيم|مكسب|جورميه'
    from DataBaseConnection import DatabaseExporter as dbcon
    username = 'root'
    password = '123qweasdzxcSq'
    hostname = 'localhost'
    database = 'easytrick'
    exporter = dbcon(username, password, hostname, database)


    processor_goods_transection =DataProcessor(file_path_goods_transection, expected_cols_goods_transection)
    processor_goods_transection.read_data()
    processor_goods_transection.select_columns(wanted_cols_goods_transection)
    processor_goods_transection.filter_row(filter_column, filter_values)
    processor_goods_transection.filter_row(filter_column2, filter_vlaues2)

    processor_goods_transection.rename_columns({ 'Text103': 'Total_invoice'})
    processor_goods_transection.ApplyDICtToCol('tr_ds',{ 'بيع آجل': 'Ba', 'شراء نقدي': 'sn', 'مرتجع آجل': 'MA'})
    processor_goods_transection.format_columns(['TR_NO'], 4)
    processor_goods_transection.add_primary_key(['tr_ds', 'TR_NO'], 'InvoiceID')
    wanted_cols_goods_transection = ['InvoiceID','tr_dt', 'Acc_Nm','Total_invoice']
    processor_goods_transection.select_columns(wanted_cols_goods_transection)
    processor_goods_transection.groupby_agg(['InvoiceID'],{'Total_invoice':'sum','tr_dt':'first','Acc_Nm':'first'})

    print(processor_goods_transection.data.head(10))

    