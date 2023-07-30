from flask import Blueprint
from src.data.databaseIniti import exporter
from flask import redirect ,url_for
from src.data.readexcel import readexcel as excel2sql
import src.data.databaseIniti as dbi 
from src.components import filepaths as fpth
from src.components.sqlcommonds import callupdateCashflow_excelPRoducer
CFstartButtons_bp = Blueprint('CFstartButtons', __name__,url_prefix='/Elfateh/main/reports/cashflow')

@CFstartButtons_bp.route('/export_datagood_transection', methods=['POST','GET'])
def export_goodstransectiontedata():
    expected_cols_goods_transection = ['Acc_Nm' ,'Itm_cd', 'TR_NO']
    processor_goods_transection =excel2sql(fpth.goodstransectionte_filepath, expected_cols_goods_transection)
    processor_goods_transection.read_data()
    exporter.export_data_first(processor_goods_transection.data, dbi.cashflow_excelINsql)
    return redirect(url_for('FileHandler.home', message='Data exported successfully!'))


@CFstartButtons_bp.route('/export_clints_data', methods=['POST','GET'])
def export_data_clients():
    expected_cols_goods_transection = ['acc_nm']
    processor_goods_transection =excel2sql(fpth.clientsdb_filephath, expected_cols_goods_transection)
    processor_goods_transection.read_data()
    exporter.export_data_first(processor_goods_transection.data, dbi.clients_excelINsql)
    return redirect(url_for('FileHandler.home', message='Data exported successfully!'))
    
@CFstartButtons_bp.route('/delete_dataFromDataBasegood_transection', methods=['POST','GET'])
def updatethedata():
    exporter.readsql(callupdateCashflow_excelPRoducer)
    return redirect(url_for('FileHandler.home', message='Data updated successfully!'))


