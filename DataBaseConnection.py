from sqlalchemy import create_engine, inspect

class DatabaseExporter:
    def __init__(self, username, password, hostname, database):
        self.engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{database}')

    def export_data(self, data, table_name):
        data.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def get_table_names(self):
        inspector = inspect(self.engine)
        table_names = inspector.get_table_names()
        return table_names



#  values with my MySQL connection details
username = 'root'
password = '123qweasdzxcSq'
hostname = 'localhost'
database = 'cashflow'

exporter = DatabaseExporter(username, password, hostname, database)
table_names = exporter.get_table_names()
print(table_names)
