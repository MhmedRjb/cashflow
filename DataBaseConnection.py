from sqlalchemy import create_engine
import pandas as pd

class DatabaseExporter:
    def __init__(self, username, password, hostname, database):
        self.engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{database}')

    def _execute_sql(self, sql):
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()

    def export_data_first(self, data, table_name):
        data.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def update_data_in(self, table_name, set_values, column_name, values):
        set_clause = ', '.join([f"{col} = '{val}'" for col, val in set_values.items()])
        values_str = ', '.join([f"'{val}'" for val in values])
        sql = f"UPDATE {table_name} SET {set_clause} WHERE {column_name} IN ({values_str})"
        self._execute_sql(sql)

    def call_stored_procedure(self, procedure_name):
        sql = f'CALL {procedure_name}()'
        self._execute_sql(sql)

    def readsql(self, sql):
        data = pd.read_sql_query(sql, self.engine)
        return data


if __name__ == "__main__":
    # Values with my MySQL connection details
    username = 'root'
    password = '123qweasdzxcSq'
    hostname = 'localhost'
    database = 'elfateh'

    exporter = DatabaseExporter(username, password, hostname, database)

    # Use the exporter instance to call different methods
    # For example:
    # data = pd.DataFrame(...)  # Your data here
    # table_name = 'your_table_name'
    # exporter.export_data_first(data, table_name)

    # set_values = {'column1': 'new_value'}
    # column_name = 'id'
    # values = [1, 2, 3]
    # exporter.update_data_in('your_table_name', set_values, column_name, values)

    # procedure_name = 'your_procedure_name'
    # exporter.call_stored_procedure(procedure_name)

    # sql = 'SELECT * FROM your_table_name'
    # result = exporter.read_sql(sql)
    # print(result)
