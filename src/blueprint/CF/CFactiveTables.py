from flask import Blueprint, render_template
from datetime import datetime ,timedelta
from src.data.databaseIniti import exporter
from src.components import sqlcommonds as sqlcom
from datetime import datetime ,timedelta
from flask_weasyprint import HTML
from flask import make_response, render_template


def get_current_date(days:int = 0):
    return (datetime.now() + timedelta(days)).date()

CFactiveTables_bp = Blueprint('CFactiveTables', __name__)

@CFactiveTables_bp.route('/Elfateh/main/reports/cashflow/display_dataclints_data')
def display_data():
    data = exporter.readsql(sqlcom.export_clints_data)
    return render_template('entrytable.html', data=data)


@CFactiveTables_bp.route('/Elfateh/main/reports/cashflow')
@CFactiveTables_bp.route('/Elfateh/main/reports/cashflow/display_goodstransectionte')
def display_goodstransectionte():    
    data = exporter.readsql(  sqlcom.export_cashflow_gby_Acc_NmANDtr_dt)

    current_date = get_current_date()
    return render_template('entrytable.html', data=data, current_date=current_date)

@CFactiveTables_bp.route('/Elfateh/main/reports/cashflow/display_all_goodstransectionte')
def display_all_goodstransectionte():

    data = exporter.readsql(
        sqlcom.export_cashflow_fby_afterTODAY
        )
    current_date = get_current_date()
    return render_template('entrytable.html', data=data, current_date=current_date)

@CFactiveTables_bp.route('/Elfateh/main/reports/cashflow/display_cashflowgroup__comapnyname')
def cashflowgroup__comapnyname():
    data = exporter.readsql(sqlcom.export_cashflow_gby_comapnyname)
    current_date = get_current_date()
    return render_template('entrytable.html', data=data, current_date=current_date)

@CFactiveTables_bp.route('/Elfateh/main/reports/cashflow/display_goodstransectionte_summary')
def display_goodstransectionte_summary():
    data = exporter.readsql(sqlcom.export_cashflow_report)
    current_date = get_current_date()
    return render_template('summarytable.html', data=data, current_date=current_date)


