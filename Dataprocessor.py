import pandas as pd
import numpy as np
import openpyxl
import random
import string
class DataProcessor:
    def __init__(self, file_path, expected_cols):
        self.file_path = file_path
        self.expected_cols = expected_cols
        self.old_df_length = 0

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
    def update_data(self):
        # read the new data from the Excel file
        data = pd.read_excel(self.file_path)

        # filter the data to only include new rows
        data = data.iloc[self.old_df_length:]

        # update the old DataFrame with the new data
        self.data = pd.concat([self.data, data], ignore_index=True)

        # update the old DataFrame length
        self.old_df_length = len(self.data)
     #creat primary key from by concat three columns

     
    def replaceVluesInCols(self, columns):
        replacements = { 'بيع آجل': 'Ba', 'شراء نقدي': 'sn', 'مرتجع آجل': 'MA'}
        
        data = self.data.copy()
        
        data['tr_ds'] = data['tr_ds'].replace(replacements)
        self.data = data    


    def creat_primary_key(self, columns, format_columns=None):
        # create a copy of the data
        data = self.data.copy()
        
        # format the specified columns
        if format_columns:
            for column, length in format_columns.items():
                data[column] = data[column].apply(lambda x: f'{x:0{length}d}')
        
        # create the primary key
        data['pk'] = data[columns].apply(lambda row: ''.join(row.values.astype(str)), axis=1)
        
        # update the data with the new primary key
        self.data = data

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


    def add_random_column(self, column_name):
        # create a copy of the data
        data = self.data.copy()

        # generate a list of random strings with the same length as the data
        random_strings = [''.join(random.choices(string.ascii_lowercase, k=2) + random.choices(string.digits, k=4)) for _ in range(len(data))]

        # add the random strings as a new column to the data
        data[column_name] = random_strings

        # update the data with the new column
        self.data = data



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
    processor_goods_transection.replaceVluesInCols(['tr_ds', 'TR_NO', 'LN_NO'])
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


# import pandas as pd
# from sqlalchemy import create_engine

# # create a connection to the database
# engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{database}')

# # read data from excel file into a dataframe
# excel_data = pd.read_excel(file_path)

# # read data from database table into a dataframe
# db_data = pd.read_sql_table(table_name, engine)

# # find rows in excel_data that are not in db_data based on primary key
# new_rows = excel_data.merge(db_data, on='pk', how='left', indicator=True)
# new_rows = new_rows[new_rows['_merge'] == 'left_only']

# # append new_rows to database table
# new_rows.to_sql(table_name, engine, if_exists='append', index=False)


    

