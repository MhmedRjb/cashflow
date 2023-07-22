from flask import request ,redirect ,Blueprint,render_template , request ,flash  ,redirect 
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed  
from wtforms import FileField, SubmitField
from wtforms.validators import  ValidationError,Optional
from werkzeug.utils import secure_filename

from datetime import datetime ,timedelta
import os
import ast

from src.data.databaseIniti import exporter
from src.components import filepaths as fpth
from src.data.databaseIniti import exporter



appfunctions_bp=Blueprint('appfunctions',__name__)

def get_current_date():
    return (datetime.now() + timedelta(days=0)).date()


class func ():
    @appfunctions_bp.route('/update_paid', methods=['POST'])
    def update_paid():
        # get the InvoiceID and Paid values from the form
        invoice_ids = request.form.getlist('invoice_id')
        paid_values = request.form.getlist('paid')
        getpaid_values = request.form.getlist('getpaid')
        real_date_values=request.form.getlist('real_date')
        previous_page = request.form['previous_page']

        for invoice_id, paid ,getpaid ,realDate in zip(invoice_ids, paid_values,getpaid_values,real_date_values):
            invoice_id_tuple = ast.literal_eval(invoice_id)
            print(realDate)
            if paid :
                print(exporter.update_data_in('main_sales_entry', {'Paid': paid}, 'InvoiceID', invoice_id_tuple))
                exporter.update_data_in('main_sales_entry', {'Paid': paid}, 'InvoiceID', invoice_id_tuple)
            if realDate == "None" and getpaid  :  
                exporter.update_data_in('main_sales_entry', {'getpaid': getpaid}, 'InvoiceID', invoice_id_tuple)
        return redirect(previous_page)


class FileHandler:

    def __init__(self, upload_folder, ALLOWED_EXTENSIONS):
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
            raise ValidationError('Invalid file type. Only .xls and .xlsx files are allowed.')


file_handler = FileHandler(r'D:\monymovment\Cashflows\static\files', {'.xls', '.xlsx'})


class UploadForm(FlaskForm):
    file = FileField('file2', validators=[FileAllowed(file_handler.ALLOWED_EXTENSIONS, 'Invalid file type. Only .xls and .xlsx files are allowed.')])
    submit = SubmitField('Upload file')


@appfunctions_bp.route('/', methods=['GET', 'POST'])
@appfunctions_bp.route('/Elfateh', methods=['GET', 'POST'])
@appfunctions_bp.route('/Elfateh/main', methods=['GET', 'POST'])
@appfunctions_bp.route('/Elfateh/main/reports', methods=['GET', 'POST'])
def home():
    form = UploadForm()
    if request.method == 'POST':
        try:
            if form.file.data:
                file_handler.save_file(form.file.data)
                flash('File uploaded successfully', 'success')
        except ValidationError as e:
            flash(str(e), 'error')

    folder_path = fpth.main_folder_path
    folder_contents = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        mtime = os.path.getmtime(item_path)
        mtime_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M')
        folder_contents.append((item, mtime_str))
    return render_template('home.html', folder_contents=folder_contents, form=form)
