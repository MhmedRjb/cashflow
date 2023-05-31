from sqlalchemy import create_engine, inspect,delete,update,Table,MetaData
import pandas as pd
import pymysql
class DatabaseExporter:
    def __init__(self, username, password, hostname, database):
        self.engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{database}')
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine,views=True)

    def export_data_frist(self, data, table_name):
        data.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def export_data(self, data, table_name):

        #create the table if not exist
        
        existing_data = pd.read_sql(f'SELECT * FROM {table_name}', self.engine)

        # identify any duplicate rows based on the primary key column
        duplicates = data['InvoiceID'].isin(existing_data['InvoiceID'])

        # remove any duplicate rows from the new data
        data = data[~duplicates]

        data.to_sql(table_name, self.engine, if_exists='append', index=False)
        
    #TODO: add a function to delete ROWS from MYSQL data if  not exist in df 
    def delete_data(self, data, table_name, primary_key, temp_table_name):
        # query the existing data in the table
        existing_data = pd.read_sql(f'SELECT * FROM {table_name}', self.engine)

        # identify any rows that have been removed from the Excel file
        removed_rows = existing_data[~existing_data[primary_key].isin(data[primary_key])]

        # insert the primary keys of the removed rows into a temporary table
        removed_rows[[primary_key]].to_sql(temp_table_name, self.engine, if_exists='replace', index=False)

    def get_table_names(self):
        inspector = inspect(self.engine)    
        table_names = inspector.get_table_names()
        return table_names
    #print all table data
    def get_table_data(self,table_name):        
        data = pd.read_sql_table(table_name, self.engine)
        return data
    #print table col names
    def cols_names(self,table_name):
        inspector = inspect(self.engine)
        col_names = inspector.get_columns(table_name)
        return col_names
    #update data in col 

    def update_data(self, table_name, set_values, where_condition):

        # Create a connection to the database
        conn = self.engine.raw_connection()
        cur = conn.cursor()

        # Construct the UPDATE statement
        set_clause = ', '.join([f"{col} = {val}" for col, val in set_values.items()])
        stmt = f"UPDATE {table_name} SET {set_clause} WHERE {where_condition}"

        # Execute the statement
        cur.execute(stmt)
        conn.commit()
        cur.close()
    
    #show the last N row in table ORDER BY col
    def show_rows(self, table_name, n, order_by, first=True):
        """
        Display the first or last n rows of a table when ordered by a specified column.

        Args:
            table_name (str): The name of the table to query.
            n (int): The number of rows to display.
            order_by (str): The column name to use for ordering.
            first (bool): Whether to display the first(True) or last(False) N rows. Defaults to True.

        Returns:
            pd.DataFrame: A DataFrame containing the query results.
        """
        if first:
            data = pd.read_sql(f'SELECT * FROM {table_name} ORDER BY {order_by} ASC LIMIT {n}', self.engine)
        else:
            data = pd.read_sql(f'SELECT * FROM (SELECT * FROM {table_name} ORDER BY {order_by} DESC LIMIT {n}) sub ORDER BY {order_by} ASC', self.engine)
        return data
    #show tables with tow condition
    # def show_tables_by_condition(self, table_name, condition1, condition2):
    #     data = pd.read_sql(f'SELECT * FROM {table_name} WHERE {condition1} AND {condition2}', self.engine)
    #     return data
    
    def get_column_data(self, table_name, column_name, condition=None):
    # construct the SELECT statement
        stmt = f'SELECT {column_name} FROM {table_name}'
        if condition:
            stmt += f' WHERE {condition}'

        # execute the SELECT statement and fetch the results
        conn = self.engine.connect()
        results = conn.execute(stmt).fetchall()

        # extract the column values from the results
        column_data = [row[0] for row in results]

        # return the column data
        return column_data
    
    #call a stored procedure 
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


    #show tables with tow conditiond
    def show_tables_by_condition(self, table_name, condition1, condition2):
        # construct the SELECT statement
        stmt = f'SELECT * FROM {table_name} WHERE {condition1} OR {condition2}'
        # execute the SELECT statement and store the results in a DataFrame
        data = pd.read_sql_query(stmt, self.engine)
        return data
    
    def readsql(self, sql):
        data = pd.read_sql_query(sql, self.engine)
        return data
        #filter row in df if not in mysql table 

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
    database = 'easytrick'
    exporter = DatabaseExporter(username, password, hostname, database)
    # print(exporter.cols_names('goodstransectionte'))
    # exporter.update_data('goodstransectionte', {'Paid': 1}, "InvoiceID = 'Ba0356'")
    #show the last 10 row in table ORDER BY Any col
    # exporter.call_stored_procedure('deleteRemovedRows')
    #show table where tr_dt> today  OR paid =0
    print(exporter.readsql('SELECT * FROM display_goodstransectionte_summary'))
