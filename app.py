from Dataprocessor import DataProcessor as dprs
from DataBaseConnection import DatabaseExporter as dbcon
from flask import Flask, render_template , request ,flash
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import input_required ,ValidationError,Optional
from main import process_good_transection, processor_Clints
from werkzeug.utils import secure_filename
import os
from flask import redirect
from flask import url_for
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY']='123456789'
app.config['UPLOAD_FOLDER'] = r'D:\monymovment\Cashflows\static\files'
username = 'root'
password = '123qweasdzxcSq'
hostname = 'localhost'
database = 'easytrick'

exporter = dbcon(username, password, hostname, database)

Processor_goods_transection = process_good_transection()

processor_clints_data = processor_Clints()

class FileHandler :

    def __init__(self, upload_folder,ALLOWED_EXTENSIONS):
        self.upload_folder = upload_folder
        self.ALLOWED_EXTENSIONS = ALLOWED_EXTENSIONS
    def is_valid_file(self, file):
        if file:
            filename = file.filename
            ext = os.path.splitext(filename)[1]
            return ext in self.ALLOWED_EXTENSIONS
        return False

    def save_file(self, file):
        if self.is_valid_file(file):
            file.save(os.path.join(self.upload_folder, secure_filename(file.filename)))
        else:
            raise ValidationError('Invalid file type. Only .xls and .xlsx files are allowed.')

file_handler = FileHandler(app.config['UPLOAD_FOLDER'], ALLOWED_EXTENSIONS=['.xls', '.xlsx'])
class UploadForm(FlaskForm):
    file = FileField('SBJRNLITMRPTTAX.xls', validators=[Optional(), file_handler.is_valid_file])
    file2 = FileField('file2', validators=[Optional(), file_handler.is_valid_file])
    submit = SubmitField('Upload file')

    @app.route('/', methods=['GET', 'POST'])
    @app.route('/home', methods=['GET', 'POST'])
    def home():
        form = UploadForm()
        if request.method == 'POST':
            try:
                file_handler.save_file(form.file.data)
                file_handler.save_file(form.file2.data)
            except ValidationError as e:
                flash(str(e))

        return render_template("home.html", form=form)

    @app.route('/next_page', methods=['GET', 'POST'])
    def next_page():
        return render_template('next_page.html')
@app.route('/export_data', methods=['POST'])
def export_data():
    processor_goods_transection = process_good_transection()
    exporter.export_data(processor_goods_transection.data, 'goodstransectionte')
    return render_template('next_page.html', message='Data exported successfully!')

@app.route('/delete_data', methods=['POST'])
def delete_data():
    processor_goods_transection = process_good_transection()
    exporter.delete_data(processor_goods_transection.data, 'goodstransectionte', 'InvoiceID', 'removed_rows')
    return render_template('next_page.html', message='Data deleted successfully!')

@app.route('/export_data_frist', methods=['POST'])
def export_data_frist():
    processor_clints_data = processor_Clints()
    exporter.export_data_frist(processor_clints_data.data, 'clints_data')
    return render_template('next_page.html', message='Data exported successfully!')

@app.route('/display_dataclints_data')
def display_data():
    data = exporter.get_table_data('clints_data')
    return render_template('audra.html', data=data)


@app.route('/display_goodstransectionte')
def display_goodstransectionte():
    # create an instance of the DatabaseExporter class
    
    # retrieve the data from the goodstransectionte table
    data = exporter.get_table_data('goodstransectionte')
    
    # pass the data to the template
    return render_template('audra.html', data=data)
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

# @app.route('/update_paid', methods=['POST','GET'])
# def update_paid():
#     # create a connection to the database
#     conn = exporter.engine.connect()
    
#     # loop over the form data
#     for key, value in request.form.items():
#         if key.startswith('paid-'):
#             # extract the InvoiceID from the key
#             invoice_id = key.split('-')[1]
            
#             # check that the InvoiceID is not empty
#             if invoice_id:
#                 # update the Paid column for this InvoiceID
#                 conn.execute(f"UPDATE goodstransectionte SET Paid='{value}' WHERE InvoiceID='{invoice_id}'")
    
#     # close the connection to the database
#     conn.close()
    
#     # redirect back to the display_goodstransectionte route
#     return redirect(url_for('display_goodstransectionte'))


# @app.route('/goodstransectionte', methods=['GET', 'POST'])
# def goodstransectionte():
#     # Retrieve data from the goodstransectionte table
#     data = exporter.get_table_data('goodstransectionte')

#     # Render an HTML template to display the data
#     return render_template('display_goodstransectionte_copy.html', data=data)






if __name__ == '__main__':
    app.run(debug=True)
