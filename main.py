from Dataprocessor import DataProcessor as dprs
from DataBaseConnection import DatabaseExporter as dbcon


exporter = dbcon('root', '123qweasdzxcSq', 'localhost', 'easytrick')

def process_good_transection():
    file_path_goods_transection = r"D:\monymovment\Cashflows\Excel_files\SBJRNLITMRPTTAX.xls"
    expected_cols_goods_transection = ['Acc_Nm' ,'sPrc', 'sQty', 'spkid']
    wanted_cols_goods_transection = ['tr_dt', 'TR_NO', 'tr_ds', 'Text103', 'Acc_Nm']
    filter_column_goods_tran = 'tr_ds'
    filter_values = 'بيع|مرتجع'
    processor_goods_transection =dprs(file_path_goods_transection, expected_cols_goods_transection)
    processor_goods_transection.read_data()
    processor_goods_transection.select_columns(wanted_cols_goods_transection)
    processor_goods_transection.filter_row(filter_column_goods_tran, filter_values)
    processor_goods_transection.rename_columns({ 'Text103': 'Total_invoice'})
    processor_goods_transection.ApplyDICtToCol('tr_ds',{ 'بيع آجل': 'Ba', 'شراء نقدي': 'sn', 'مرتجع آجل': 'MA'})
    processor_goods_transection.format_columns(['TR_NO'], 4)
    processor_goods_transection.add_primary_key(['tr_ds', 'TR_NO'], 'InvoiceID')
    wanted_cols_goods_transection = ['InvoiceID','tr_dt', 'Acc_Nm','Total_invoice']
    processor_goods_transection.select_columns(wanted_cols_goods_transection)
    processor_goods_transection.groupby_agg(['InvoiceID'],{'Total_invoice':'sum','tr_dt':'first','Acc_Nm':'first'})
    return processor_goods_transection
Processor_goods_transection = process_good_transection()
def processor_Clints():
    file_path_clints_data= r"D:\monymovment\Cashflows\Excel_files\SBAccMFDtlRpt.xls"
    processor_Clints = dprs(file_path_clints_data, ['rec_id', 'acc_cd', 'acc_nm', 'Text85', 'نص93'])
    processor_Clints.read_data()
    processor_Clints.select_columns(['acc_nm', 'Text85', 'نص93'])
    processor_Clints.filter_row_null('acc_nm')
    processor_Clints.rename_columns({'Text85':"tax",'نص93':"payment_method"})
    return processor_Clints

processor_clints_data = processor_Clints()


exporter.export_data(Processor_goods_transection.data, 'goodstransectionte')
exporter.delete_data(Processor_goods_transection.data, 'goodstransectionte', 'InvoiceID', 'removed_rows')
exporter.export_data_frist(processor_clints_data.data, 'clints_data')

#print goodstransectionte using get_table_data
