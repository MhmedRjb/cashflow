from sqlalchemy import create_engine
import pandas as pd
import src.data.databaseIniti as dbi

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

    def readsql(self, sql, params=None):
        data = pd.read_sql_query(sql, self.engine, params=params)
        return data


if __name__ == "__main__":
    # Values with my MySQL connection details
    username = dbi.username
    password = dbi.password
    hostname = dbi.hostname
    database = dbi.database

    exporter = DatabaseExporter(username, password, hostname, database)
