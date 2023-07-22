from flask import Blueprint
from src.data.databaseIniti import exporter
from flask import redirect ,url_for
from src.data.Dataprocessor import DataProcessor as dprs
import src.data.databaseIniti as dbi 
from src.components import filepaths as fpth

cashFlowButtons_bp = Blueprint('cashFlowButtons', __name__)

@cashFlowButtons_bp.route('/Elfateh/main/reports/cashflow/export_datagood_transection', methods=['POST','GET'])
def export_data():
    file_path_goods_transection = fpth.goodstransectionte_filepath
    expected_cols_goods_transection = ['Acc_Nm' ,'Itm_cd', 'TR_NO']
    processor_goods_transection =dprs(file_path_goods_transection, expected_cols_goods_transection)
    processor_goods_transection.read_data()
    exporter.export_data_first(processor_goods_transection.data, dbi.cashflow_excelINsql)

    
    return redirect(url_for('home', message='Data exported successfully!'))
@cashFlowButtons_bp.route('/Elfateh/main/reports/cashflow/export_clints_data', methods=['POST','GET'])
def export_data_frist():
    file_path_goods_transection = fpth.clientsdb_filephath
    expected_cols_goods_transection = ['acc_nm']
    processor_goods_transection =dprs(file_path_goods_transection, expected_cols_goods_transection)
    processor_goods_transection.read_data()
    #export the data to sql 
    exporter.export_data_first(processor_goods_transection.data, dbi.clients_excelINsql)
    return redirect(url_for('home', message='Data exported successfully!'))
    
@cashFlowButtons_bp.route('/Elfateh/main/reports/cashflow/delete_dataFromDataBasegood_transection', methods=['POST','GET'])
def updatethedata():
    exporter.call_stored_procedure(dbi.updateCashflow_excel)
    return redirect(url_for('home', message='Data updated successfully!'))
