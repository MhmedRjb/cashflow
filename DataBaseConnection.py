from sqlalchemy import create_engine, inspect,delete

import pandas as pd
class DatabaseExporter:
    def __init__(self, username, password, hostname, database):
        self.engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{database}')

    def export_data(self, data, table_name):
        data.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def get_table_names(self):
        inspector = inspect(self.engine)    
        table_names = inspector.get_table_names()
        return table_names
    
    def append_new_rows(self, table_name1, table_name2):
        # read data from database table 1 into a dataframe
        data = pd.read_sql_table(table_name1, self.engine)

        # read data from database table 2 into another dataframe
        db_data = pd.read_sql_table(table_name2, self.engine)

        # find rows in data that are not in db_data based on primary key
        new_rows = data.merge(db_data, on='pk', how='left', indicator=True)
        new_rows = new_rows[new_rows['_merge'] == 'left_only']

        # append new_rows to database table 2
        new_rows.to_sql(table_name2, self.engine, if_exists='append', index=False)
    def append_new_rows3(self, data, table_name):
        # read data from database table into another dataframe
        db_data = pd.read_sql_table(table_name, self.engine)

        # find rows in data that are not in db_data based on primary key
        new_rows = data.merge(db_data, on='pk', how='left', indicator=True)
        new_rows = new_rows[new_rows['_merge'] == 'left_only']

        # append new_rows to database table
        new_rows.to_sql(table_name, self.engine, if_exists='append', index=False)

    def remove_old_rows(self, file_path, table_name):
        # read data from excel file into a dataframe
        excel_data = pd.read_excel(file_path)

        # read data from database table into a dataframe
        db_data = pd.read_sql_table(table_name, self.engine)

        # find rows in db_data that are not in excel_data based on primary key
        old_rows = db_data.merge(excel_data, on='pk', how='right', indicator=True)
        old_rows = old_rows[old_rows['_merge'] == 'right_only']

        # get primary key values of old rows
        old_pks = old_rows['pk'].tolist()

        # delete old rows from database table
        with self.engine.connect() as conn:
            for pk in old_pks:
                conn.execute(f'DELETE FROM {table_name} WHERE pk = "{pk}"')
    def remove_old_rows2(self, file_path, table_name):
        # read data from excel file into a dataframe
        excel_data = pd.read_excel(file_path)

        # get primary keys from excel file
        pks = excel_data['pk'].tolist()

        # delete rows from database table that are not in excel file based on primary key
        with self.engine.connect() as conn:
            delete_stmt = delete(table_name).where(~table_name.c.pk.in_(pks))
            conn.execute(delete_stmt)


if __name__ == "__main__":
#  values with my MySQL connection details
    username = 'root'
    password = '123qweasdzxcSq'
    hostname = 'localhost'
    database = 'cashflow'

    exporter = DatabaseExporter(username, password, hostname, database)
