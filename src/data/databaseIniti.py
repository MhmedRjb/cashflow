
from src.data.databaseAccess import databaseAccess as dbcon


username = 'root'
password = '123qweasdzxcSq'
hostname = 'localhost'
database = 'elfateh'

cashflow_excelINsql='excel_table'
clients_excelINsql='excel_table_clients'
updateCashflow_excelPRoducer='update_main_sales_entry'

MAIN_SALES_ENTRY='main_sales_entry'
paid='Paid'
GETPAID='getpaid'
INVOICEID='InvoiceID'
REAL_DATE='real_date'


exporter = dbcon(username, password, hostname, database)



