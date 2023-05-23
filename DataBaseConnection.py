from sqlalchemy import create_engine, inspect,delete
import pandas as pd
class DatabaseExporter:
    def __init__(self, username, password, hostname, database):
        self.engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{database}')

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
    #mysql dump backup the data base arcticker only not data --nodata
    def backup_database(self,backup_name):
        self.engine.execute(f'DUMP DATABASE ElfatehCashFlow TO {backup_name}.sql')

    

    
if __name__ == "__main__":
#  values with my MySQL connection details
    username = 'root'
    password = '123qweasdzxcSq'
    hostname = 'localhost'
    database = 'ElfatehCashFlow'

    exporter = DatabaseExporter(username, password, hostname, database)
    exporter.backup_database('backup')
