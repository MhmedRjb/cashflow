from Dataprocessor import DataProcessor as dprs
from DataBaseConnection import DatabaseExporter as dbcon
from flask import Flask, render_template , request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import input_required ,ValidationError,Optional
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY']='123456789'
app.config['UPLOAD_FOLDER'] = r'D:\monymovment\Cashflows\static\files'
def validate_file_extension(form, field):
    if field.data:
        filename = field.data.filename
        ext = os.path.splitext(filename)[1]
        if ext not in ['.xls', '.xlsx']:
            raise ValidationError('ملفات أكسل فقط xls, xlsx')

class UploadForm(FlaskForm):
    file = FileField('SBJRNLITMRPTTAX.xls', validators=[Optional(), validate_file_extension])
    file2 = FileField('file2', validators=[Optional(), validate_file_extension])
    submit = SubmitField('Upload file')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadForm()
    if request.method == 'POST':
        file = form.file.data
        file2 = form.file2.data
        if file:
            filename = file.filename
            ext = os.path.splitext(filename)[1]
            if ext in ['.xls', '.xlsx']:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        if file2:
            filename = file2.filename
            ext = os.path.splitext(filename)[1]
            if ext in ['.xls', '.xlsx']:
                file2.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file2.filename)))

    return render_template("home.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
