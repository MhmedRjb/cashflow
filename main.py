from Dataprocessor import DataProcessor as dprs
from DataBaseConnection import DatabaseExporter as dbcon

file_path_goods_transection = r"D:\monymovment\Cashflows\Excel_files\SBJRNLITMRPTTAX.xls"
expected_cols_goods_transection = ['Acc_Nm' ,'sPrc', 'sQty', 'spkid']
wanted_cols_goods_transection = ['tr_dt', 'TR_NO', 'LN_NO', 'tr_ds', 'Text103', 'Acc_Nm']
filter_column = 'tr_ds'
filter_values = 'بيع|مرتجع'

processor_goods_transection =dprs(file_path_goods_transection, expected_cols_goods_transection)
processor_goods_transection.read_data()
processor_goods_transection.select_columns(wanted_cols_goods_transection)
processor_goods_transection.filter_row(filter_column, filter_values)
processor_goods_transection.rename_columns({ 'Text103': 'Total_invoice'})
processor_goods_transection.ApplyDICtToCol('tr_ds',{ 'بيع آجل': 'Ba', 'شراء نقدي': 'sn', 'مرتجع آجل': 'MA'})
processor_goods_transection.creat_primary_key(['tr_ds', 'TR_NO', 'LN_NO'],  {'TR_NO': 4, 'LN_NO': 2})
processor_goods_transection.creat_primary_key(['tr_ds', 'TR_NO'], pk_column='InvoiceID'   )
wanted_cols_goods_transection = ['pk','InvoiceID','tr_dt', 'Acc_Nm','Total_invoice']
processor_goods_transection.select_columns(wanted_cols_goods_transection)
processor_goods_transection.groupby_agg(['InvoiceID'],{'Total_invoice':'sum','tr_dt':'first','Acc_Nm':'first'})

print(processor_goods_transection.data)


#work in second file
file_path_clints_data= r"D:\monymovment\Cashflows\Excel_files\SBAccMFDtlRpt.xls"
expected_cols_clints_data = ['rec_id', 'acc_cd', 'acc_nm', 'Text85', 'نص93']
wanted_cols_clints_data = ['acc_nm', 'Text85', 'نص93']
filter_column = 'acc_nm'
processor_clints_data =dprs(file_path_clints_data, expected_cols_clints_data)
processor_clints_data.read_data()
processor_clints_data.select_columns(wanted_cols_clints_data)
processor_clints_data.filter_row_null(filter_column)
processor_clints_data.rename_columns({'Text85':"tax",'نص93':"payment_method"})

print(processor_clints_data.data)


username = 'root'
password = '123qweasdzxcSq'
hostname = 'localhost'
database = 'easytrick'

exporter = dbcon(username, password, hostname, database)
# specify the data and table name

# export the data to the database
exporter.export_data(processor_goods_transection.data, 'goodstransectionte')
exporter.delete_data(processor_goods_transection.data, 'goodstransectionte', 'InvoiceID', 'removed_rows')

#print goods_transection ins the mysql 
# print(exporter.get_table_data('goodstransectiontemp'))

exporter.export_data_frist(processor_clints_data.data, 'clints_data')
# print(exporter.get_table_data('clints_data'))
#Print the table names
print(exporter.get_table_names())
