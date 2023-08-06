from flask import Blueprint, render_template ,session,make_response,g
from src.components import sqlcommonds as sqlcom
from flask_weasyprint import HTML
from ..main.authorizationFunction import authorization_required
from .reportsDataFUNC import *





CFReportes_bp = Blueprint('CFReportes', __name__)


@CFReportes_bp.route('/Elfateh/main/print/cashflow')
@authorization_required(allowed_roles=['admin','user'])
def extractPDFofgoodstransectionte_summary():
    # Retrieve the data from the goodstransectionte table
    data = g.db_access.readsql(sqlcom.export_cashflow_report)
    column_names = ['اسم الشركة ', 'معاد الأستحقاق ', 'الإجمالي']
    reprot_type='تقرير داخلي'
    report_date=get_current_date()
    report_author = authoreName()
    report_number = fristlettersINuserANDdate()
    

    
    
    # Render the HTML template with the data
    html = render_template('pdf.html', data=data, column_names=column_names,
                            reprot_type=reprot_type,report_number=report_number,report_author=
                            report_author,report_date=report_date)

    # Generate the PDF
    pdf = HTML(string=html).write_pdf()
    # Create a response object with the PDF data
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename={report_date}_cashflowtreport.pdf'

    return response

