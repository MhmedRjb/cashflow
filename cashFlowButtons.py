from flask import Blueprint
from databaseIniti import exporter
from main import process_good_transection, processor_Clints
from flask import redirect ,url_for
from Dataprocessor import DataProcessor as dprs

cashFlowButtons_bp = Blueprint('cashFlowButtons', __name__)

@cashFlowButtons_bp.route('/Elfateh/main/reports/cashflow/export_datagood_transection', methods=['POST','GET'])
def export_data():
    #export data from excel ro sql bt replaceing the whole table
    file_path_goods_transection = r"D:\monymovment\Cashflows\Excel_files\SBJRNLITMRPTTAX.xls"
    expected_cols_goods_transection = ['Acc_Nm' ,'Itm_cd', 'TR_NO']
    processor_goods_transection =dprs(file_path_goods_transection, expected_cols_goods_transection)
    processor_goods_transection.read_data()
    #export the data to sql 
    exporter.export_data_frist(processor_goods_transection.data, 'excel_table')

    
    return redirect(url_for('home', message='Data exported successfully!'))

@cashFlowButtons_bp.route('/Elfateh/main/reports/cashflow/delete_good_transection', methods=['POST','GET'])
def delete_data():
    processor_goods_transection = process_good_transection()
    exporter.delete_data(processor_goods_transection.data, 'goodstransectionte', 'InvoiceID', 'removed_rows')
    return redirect(url_for('home', message='Data deleted successfully!'))

@cashFlowButtons_bp.route('/Elfateh/main/reports/cashflow/export_clints_data', methods=['POST','GET'])
def export_data_frist():
    processor_clints_data = processor_Clints()
    exporter.export_data_frist(processor_clints_data.data, 'clints_data')
    return redirect(url_for('home', message='Data exported successfully!'))
    
@cashFlowButtons_bp.route('/Elfateh/main/reports/cashflow/delete_dataFromDataBasegood_transection', methods=['POST','GET'])
def delete_data_last():
    exporter.call_stored_procedure('update_main_sales_entry')
    return redirect(url_for('home', message='Data exported successfully!'))
