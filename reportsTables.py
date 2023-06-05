from flask import Blueprint, render_template
from datetime import datetime ,timedelta
from databaseIniti import exporter

def get_current_date():
    return (datetime.now() + timedelta(days=0)).date()

displaytables_bp = Blueprint('displaytables', __name__)

@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_dataclints_data')
def display_data():
    data = exporter.get_table_data('clints_data')
    return render_template('audra.html', data=data)


@displaytables_bp.route('/Elfateh/main/reports/cashflow')
@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_goodstransectionte')
def display_goodstransectionte():    
    data = exporter.readsql(  """ SELECT CONCAT('(', GROUP_CONCAT(DISTINCT CONCAT('''', InvoiceID, '''')), ',', ')') AS InvoiceID , SUM(CASE WHEN InvoiceID LIKE 'Ba%%' THEN Total_invoice ELSE -Total_invoice END) AS Total_invoice, tr_dt, Acc_Nm, dueDate, realDate, (CASE WHEN SUM(Paid) = COUNT(*) THEN 1 ELSE NULL END) AS Paid, SUM(CASE WHEN InvoiceID LIKE 'Ba%%' THEN getpaid ELSE -getpaid END) AS getpaid, SUM(CASE WHEN InvoiceID LIKE 'Ba%%' THEN total_invoice_aftertax ELSE -total_invoice_aftertax END) AS total_invoice_aftertax, SUM(CASE WHEN InvoiceID LIKE 'Ba%%' THEN leftUnPaid ELSE -leftUnPaid END) AS leftUnPaid FROM goodstransectionte GROUP BY Acc_Nm, tr_dt ORDER by     Paid desc ,dueDate """)
    current_date = get_current_date()
    return render_template('audra.html', data=data, current_date=current_date)


@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_all_goodstransectionte')
def display_all_goodstransectionte():
    data = exporter.readsql( "SELECT * FROM goodstransectionte ORDER BY dueDate ASC ,(CASE WHEN Paid = 'NaN' THEN 0 ELSE Paid END) DESC ;")
    data = exporter.readsql(  """ SELECT CONCAT('(', '''', InvoiceID, '''', ',', ')') AS InvoiceID ,  Total_invoice, tr_dt, Acc_Nm, dueDate, realDate, Paid, getpaid,total_invoice_aftertax, leftUnPaid FROM goodstransectionte ORDER by     Paid desc ,dueDate """)
    current_date = get_current_date()
    return render_template('audra.html', data=data, current_date=current_date)



@displaytables_bp.route('/Elfateh/main/reports/cashflow/display_goodstransectionte_summary')
def display_goodstransectionte_summary():
    data = exporter.readsql("SELECT * FROM cashflowsummary WHERE leftUnPaid <>0")
    current_date = get_current_date()
    return render_template('miller.html', data=data, current_date=current_date)
