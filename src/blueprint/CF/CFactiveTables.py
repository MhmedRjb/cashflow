from flask import Blueprint, render_template ,jsonify ,g
from src.components import sqlcommonds as sqlcom
from src.blueprint.CF.reportsDataFUNC import get_current_date
import json
from ..main.date_check_required import date_check_required
from datetime import datetime


CFactiveTables_bp = Blueprint('CFactiveTables', __name__,url_prefix='/Elfateh/main/reports/cashflow')

@CFactiveTables_bp.route('/display_dataclints_data')
@date_check_required()
def display_data():
    data = g.db_access.readsql(sqlcom.export_clints_data)
    data_json = data.to_dict(orient='records')
    return data_json



@CFactiveTables_bp.route('')
@CFactiveTables_bp.route('/display_goodstransectionte')
@date_check_required(add_days=15)
def display_goodstransectionte():
    data = g.db_access.readsql(sqlcom.export_cashflow_gby_Acc_NmANDtr_dt)
    current_date = get_current_date()
    data_json = data.to_dict(orient='records')

    # Pass the data and current_date to the HTML template
    return render_template('entrytable.html', data=data_json, current_date=current_date)





@CFactiveTables_bp.route('/display_all_goodstransectionte')
@date_check_required()
@date_check_required()
def display_all_goodstransectionte():

    data =  g.db_access.readsql(sqlcom.export_cashflow_fby_afterTODAY)
    current_date = get_current_date()
    data_json = data.to_dict(orient='records')

    return render_template('entrytable.html', data=data_json, current_date=current_date)


@CFactiveTables_bp.route('/display_cashflowgroup__comapnyname')
@date_check_required(add_days=15)
def cashflowgroup__comapnyname():
    data = g.db_access.readsql(sqlcom.export_cashflow_gby_comapnyname)
    current_date = get_current_date()
    data_json = data.to_dict(orient='records')

    return render_template('entrytable.html', data=data_json, current_date=current_date)

@CFactiveTables_bp.route('/display_goodstransectionte_summary')
@date_check_required()
def display_goodstransectionte_summary():

    data = g.db_access.readsql(sqlcom.export_cashflow_report)

    current_date = get_current_date()


    return render_template('summarytable.html', data=data, current_date=current_date)


