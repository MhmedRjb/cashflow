from sqlalchemy import create_engine, inspect,delete,update,Table,MetaData
import pandas as pd
import pymysql
class DatabaseExporter:
    def __init__(self, username, password, hostname, database):
        self.engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{database}')
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine)

    def export_data_frist(self, data, table_name):
        data.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def export_data(self, data, table_name):

        #create the table if not exist
        
        existing_data = pd.read_sql(f'SELECT * FROM {table_name}', self.engine)

        # identify any duplicate rows based on the primary key column
        duplicates = data['InvoiceID'].isin(existing_data['InvoiceID'])

        # remove any duplicate rows from the new data
        data = data[~duplicates]

    # insert the new data into the table
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

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cur.close()


    

    
if __name__ == "__main__":
#  values with my MySQL connection details
    username = 'root'
    password = '123qweasdzxcSq'
    hostname = 'localhost'
    database = 'easytrick'
    exporter = DatabaseExporter(username, password, hostname, database)
    print(exporter.cols_names('goodstransectionte'))
    exporter.update_data('goodstransectionte', {'Paid': 1}, "InvoiceID = 'Ba0356'")

