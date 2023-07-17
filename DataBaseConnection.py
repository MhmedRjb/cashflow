from sqlalchemy import create_engine, inspect,delete,update,Table,MetaData
import pandas as pd
import pymysql
from sqlalchemy import update, text
import ast

class DatabaseExporter:
    def __init__(self, username, password, hostname, database):
        self.engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{database}')
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine,views=True)

    def export_data_frist(self, data, table_name):
        data.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def export_data(self, data, table_name):

        
        existing_data = pd.read_sql(f'SELECT * FROM {table_name}', self.engine)

        duplicates = data['InvoiceID'].isin(existing_data['InvoiceID'])

        data = data[~duplicates]

        data['Acc_Nm'] = data['Acc_Nm'].str.encode('utf8').str.decode('utf8', 'ignore')

        data.to_sql(table_name, self.engine, if_exists='append', index=False)
        
    #TODO: add a function to delete ROWS from MYSQL data if  not exist in df 
    def delete_data(self, data, table_name, primary_key, temp_table_name):
        # query the existing data in the table
        existing_data = pd.read_sql(f'SELECT * FROM {table_name}', self.engine)

        # identify any rows that have been removed from the Excel file
        removed_rows = existing_data[~existing_data[primary_key].isin(data[primary_key])]

        # insert the primary keys of the removed rows into a temporary table
        removed_rows[[primary_key]].to_sql(temp_table_name, self.engine, if_exists='replace', index=False)

    #update date using in inted of wherer
    def update_data_in(self, table_name, set_values, column_name, values):
        # Create a connection to the database
        conn = self.engine.raw_connection()
        cur = conn.cursor()

        # Construct the UPDATE statement
        set_clause = ', '.join([f"{col} = {val}" for col, val in set_values.items()])
        values_str = ', '.join([f"'{val}'" for val in values])
        stmt = f"UPDATE {table_name} SET {set_clause} WHERE {column_name} IN ({values_str})"
        # Execute the statement
        cur.execute(stmt)
        conn.commit()
        cur.close()



    def call_stored_procedure(self, procedure_name):
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        # construct the CALL statement
        stmt = f'CALL {procedure_name}()'
        print(stmt)
        # execute the CALL statement
        cur.execute(stmt)
        conn.commit()
        cur.close()


    
    def readsql(self, sql):
        data = pd.read_sql_query(sql, self.engine)
        return data

    def filter_row_not_in(self, table_name, col_name):
        existing_data = pd.read_sql(f'SELECT * FROM {table_name}', self.engine)
        # identify any duplicate rows based on the primary key column
        duplicates = data['InvoiceID'].isin(existing_data['InvoiceID'])
        # remove any duplicate rows from the new data
        data = data[~duplicates]

        


    

    
if __name__ == "__main__":
#  values with my MySQL connection details
    username = 'root'
    password = '123qweasdzxcSq'
    hostname = 'localhost'
    database = 'elfateh'
    exporter = DatabaseExporter(username, password, hostname, database)
    data.to_sql(table_name, self.engine, if_exists='replace', index=False)
