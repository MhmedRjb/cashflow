from flask import Blueprint, render_template
from datetime import datetime ,timedelta
from databaseIniti import exporter

def get_current_date(days:int = 0):
    return (datetime.now() + timedelta(days)).date()

displaytables_bp = Blueprint('displaytables', __name__)

@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_dataclints_data')
def display_data():
    data = exporter.readsql('select * from clints_data')
    return render_template('audra.html', data=data)


@displaytables_bp.route('/Elfateh/main/reports/cashflow')
@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_goodstransectionte')
def display_goodstransectionte():    
    data = exporter.readsql(  f""" SELECT * from cashflowGroupAcc_Nm__tr_dt""")
    current_date = get_current_date()
    return render_template('audra.html', data=data, current_date=current_date)

@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_all_goodstransectionte')
def display_all_goodstransectionte():

    data = exporter.readsql(f"""SELECT *  from cashflowFilter__aftertoday""")
    current_date = get_current_date()
    return render_template('audra.html', data=data, current_date=current_date)

@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_cashflowgroup__comapnyname')
def cashflowgroup__comapnyname():
    data = exporter.readsql(f"""SELECT *  from cashflowgroup__comapnyname""")
    current_date = get_current_date()
    return render_template('audra.html', data=data, current_date=current_date)



@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_goodstransectionte_summary')
def display_goodstransectionte_summary():
    data = exporter.readsql("SELECT * FROM cashflow__summary WHERE leftUnPaid <>0")
    current_date = get_current_date()
    return render_template('miller.html', data=data, current_date=current_date)
