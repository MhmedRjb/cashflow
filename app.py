from Dataprocessor import DataProcessor as dprs
from DataBaseConnection import DatabaseExporter as dbcon
from main import process_good_transection, processor_Clints
from flask import Flask, render_template , request ,flash ,session ,redirect ,url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import input_required ,ValidationError,Optional
from werkzeug.utils import secure_filename
import os
import pandas as pd
from flask import jsonify
from datetime import datetime ,timedelta
from flask_weasyprint import HTML, render_pdf
from flask import make_response, render_template


app = Flask(__name__)
app.config['SECRET_KEY']='123456789'
app.secret_key = '123456789'
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), r'Excel_files')
username = 'root'
password = '123qweasdzxcSq'
hostname = 'localhost'
database = 'easytrick'

exporter = dbcon(username, password, hostname, database)

def get_current_date():
    return (datetime.now() + timedelta(days=1)).date()

class FileHandler :

    def __init__(self, upload_folder,ALLOWED_EXTENSIONS):
        self.upload_folder = upload_folder
        self.ALLOWED_EXTENSIONS = ALLOWED_EXTENSIONS
    def is_valid_file(self, file):
        if file:
            filename = file.filename
            ext = os.path.splitext(filename)[1]
            print(f'File extension: {ext}')
            return ext in self.ALLOWED_EXTENSIONS
        return False

    def save_file(self, file):
        if self.is_valid_file(file):
            file.save(os.path.join(self.upload_folder, secure_filename(file.filename)))
        else:
            
            raise ValidationError('Invalid file ssssssssssssstype. Only .xls and .xlsx files are allowed.')

file_handler = FileHandler(app.config['UPLOAD_FOLDER'], ALLOWED_EXTENSIONS=['.xls', '.xlsx'])
class UploadForm(FlaskForm):
    file = FileField('file2', validators=[Optional(), file_handler.is_valid_file])
    submit = SubmitField('Upload file')

    @app.route('/', methods=['GET', 'POST'])
    @app.route('/home', methods=['GET', 'POST'])
    def home():
        form = UploadForm()
        if request.method == 'POST':
            try:
                if form.file.data:
                    file_handler.save_file(form.file.data)

            except ValidationError as e:
                flash(str(e), 'error')

    
        folder_path = r'D:\monymovment\Cashflows\Excel_files'
        folder_contents = []
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            mtime = os.path.getmtime(item_path)
            mtime_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M')
            folder_contents.append((item, mtime_str))
        return render_template('home.html', folder_contents=folder_contents,form=form)

    @app.route('/next_page', methods=['GET', 'POST'])
    def next_page(message=None):
        return render_template('next_page.html',message=message)
    
class button(FlaskForm):
    @app.route('/export_data', methods=['POST','GET'])
    def export_data():
        processor_goods_transection = process_good_transection()
        exporter.export_data(processor_goods_transection.data, 'goodstransectionte')
        return redirect(url_for('home', message='Data exported successfully!'))

    @app.route('/delete_data', methods=['POST','GET'])
    def delete_data():
        processor_goods_transection = process_good_transection()
        exporter.delete_data(processor_goods_transection.data, 'goodstransectionte', 'InvoiceID', 'removed_rows')
        return redirect(url_for('home', message='Data deleted successfully!'))

    @app.route('/export_data_frist', methods=['POST','GET'])
    def export_data_frist():
        processor_clints_data = processor_Clints()
        exporter.export_data_frist(processor_clints_data.data, 'clints_data')
        return redirect(url_for('home', message='Data exported successfully!'))
    @app.route('/delete_data_last', methods=['POST','GET'])
    def delete_data_last():
        exporter.call_stored_procedure('deleteRemovedRows')
        return redirect(url_for('home', message='Data exported successfully!'))
    
class displaytables():
    @app.route('/display_dataclints_data')
    def display_data():
        data = exporter.get_table_data('clints_data')
        return render_template('audra.html', data=data)


    @app.route('/display_goodstransectionte')
    def display_goodstransectionte():    
        data = exporter.readsql( 'SELECT * FROM recent_goodstransectionte;')
        current_date = get_current_date()
        return render_template('audra.html', data=data, current_date=current_date)
    
    @app.route('/display_all_goodstransectionte')
    def display_all_goodstransectionte():
        data = exporter.readsql( 'SELECT * FROM goodstransectionte  ORDER BY dueDate ASC, Acc_Nm ASC;')
        current_date = get_current_date()

        return render_template('audra.html', data=data, current_date=current_date)
    
    @app.route('/display_goodstransectionte_summary')
    def display_goodstransectionte_summary():
        data = exporter.readsql("SELECT * FROM goodstransectionte_summary ")
        current_date = get_current_date()
        return render_template('miller.html', data=data, current_date=current_date)


class hello():
    @app.route('/pdf')
    def hello():
        # Retrieve the data from the goodstransectionte table
        data = exporter.readsql('SELECT company_name , dueDate , total_invoice from goodstransectionte_summary')
        column_names = ['اسم الشركة ', 'معاد الأستحقاق ', 'الإجمالي']
        reprot_type='تقرير داخلي'
        report_number='1'
        report_author='محمد عبدالله'
        report_date=get_current_date()

        # Render the HTML template with the data
        html = render_template('pdf.html', data=data, column_names=column_names,reprot_type=reprot_type,report_number=report_number,report_author=
                               report_author,report_date=report_date)

        # Generate the PDF
        pdf = HTML(string=html).write_pdf()

        # Create a response object with the PDF data
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=goodstransectionte_summary.pdf'

        return response


class func ():
    @app.route('/update_paid', methods=['POST'])
    def update_paid():
        # get the InvoiceID and Paid values from the form
        invoice_ids = request.form.getlist('invoice_id')
        paid_values = request.form.getlist('paid')

        # update the Paid value for each specified InvoiceID where the value is not empty
        for invoice_id, paid in zip(invoice_ids, paid_values):
            if paid:
                exporter.update_data('goodstransectionte', {'Paid': paid}, f"InvoiceID = '{invoice_id}'")

        # redirect back to the display_goodstransectionte route
        return redirect(url_for('display_goodstransectionte'))

class in_way():
    @app.route('/inventory')
    def inventory():
        return render_template('commingsoon.html')
    
    @app.route('/clinets_statistics')
    def clinets_statistics():
        return render_template('commingsoonreports.html')
    
    @app.route('/genral_statistics')
    def genral_statistics():
        return render_template('commingsoonreports.html')
    

if __name__ == '__main__':
    app.run(debug=True)
