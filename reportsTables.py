from flask import Blueprint, render_template
from datetime import datetime ,timedelta
from databaseIniti import exporter

def get_current_date():
    return (datetime.now() + timedelta(days=1)).date()

displaytables_bp = Blueprint('displaytables', __name__)

@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_dataclints_data')
def display_data():
    data = exporter.get_table_data('clints_data')
    return render_template('audra.html', data=data)
@displaytables_bp.route('/Elfateh/main/reports/cashflow')
@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_goodstransectionte')
def display_goodstransectionte():    
    data = exporter.readsql( 'SELECT * FROM recent_goodstransectionte;')
    current_date = get_current_date()
    return render_template('audra.html', data=data, current_date=current_date)

@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_all_goodstransectionte')
def display_all_goodstransectionte():
    data = exporter.readsql( 'SELECT * FROM goodstransectionte  ORDER BY dueDate ASC, Acc_Nm ASC;')
    current_date = get_current_date()
    return render_template('audra.html', data=data, current_date=current_date)

@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_goodstransectionte_summary')
def display_goodstransectionte_summary():
    data = exporter.readsql("SELECT * FROM goodstransectionte_summary ")
    current_date = get_current_date()
    return render_template('miller.html', data=data, current_date=current_date)
