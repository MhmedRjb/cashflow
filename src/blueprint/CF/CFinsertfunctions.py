from flask import request ,redirect ,Blueprint , request   ,redirect ,g
from datetime import datetime ,timedelta
import ast
from ...data import dbstring as dbi

CFinsertfunctions_bp=Blueprint('CFinsertfunctions',__name__)

def get_current_date():
    return (datetime.now() + timedelta(days=0)).date()

def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

class func ():
    @CFinsertfunctions_bp.route('/update_paid', methods=['POST'])
    def update_paid():
        # get the InvoiceID and Paid values from the form
        invoice_ids = request.form.getlist('invoice_id')
        paid_values = request.form.getlist('paid')
        getpaid_values = request.form.getlist('getpaid')
        real_date_values=request.form.getlist('real_date')
        previous_page = request.form['previous_page']
        print(previous_page)

        for invoice_id, paid ,getpaid ,realDate in zip(invoice_ids, paid_values,getpaid_values,real_date_values):
            invoice_id_tuple = ast.literal_eval(invoice_id)


            if is_valid_number(paid) :
<<<<<<< HEAD

                g.db_access2.update_data_in(dbi.MAIN_SALES_ENTRY, {dbi.paid: paid}, dbi.INVOICEID, invoice_id_tuple)

            if realDate == "None" and is_valid_number(getpaid)  :  

=======
                g.db_access2.update_data_in(dbi.MAIN_SALES_ENTRY, {dbi.paid: paid}, dbi.INVOICEID, invoice_id_tuple)
            if realDate == "None" and is_valid_number(getpaid)  :  
>>>>>>> 839bcba8f4eb2a01c7ac88cc17399af8d52de572
                g.db_access2.update_data_in(dbi.MAIN_SALES_ENTRY, {dbi.GETPAID: getpaid}, dbi.INVOICEID, invoice_id_tuple)
        return redirect(previous_page)
