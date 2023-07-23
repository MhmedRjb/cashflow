
from src.data.DataBaseConnection import DatabaseExporter as dbcon

username =
password = password
hostname = hostname
database = database

cashflow_excelINsql='excel_table'
clients_excelINsql='excel_table_clients'
updateCashflow_excel='update_main_sales_entry'





exporter = dbcon(username, password, hostname, database)


