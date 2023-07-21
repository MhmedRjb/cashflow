
from DataBaseConnection import DatabaseExporter as dbcon

username = 'root'
password = '123qweasdzxcSq'
hostname = 'localhost'
database = 'elfateh'

cashflow_excelINsql='excel_table'
clients_excelINsql='excel_table_clients'
updateCashflow_excel='update_main_sales_entry'





exporter = dbcon(username, password, hostname, database)


