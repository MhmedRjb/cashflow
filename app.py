from Dataprocessor import DataProcessor as dprs
from DataBaseConnection import DatabaseExporter as dbcon
from main import process_good_transection, processor_Clints
from flask import Flask, render_template , request ,flash
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import input_required ,ValidationError,Optional
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY']='123456789'
app.config['UPLOAD_FOLDER'] = r'D:\monymovment\Cashflows\static\files'

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
    @app.route('/process_good_transection')
    def index():
        processor_goods_transection = process_good_transection()
        data = processor_goods_transection.data
        # do something with the processed data
        return render_template('index.html', data=data)

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

@app.route('/process_good_transection')
def process_good_transection_route():
    processor_goods_transection = process_good_transection()
    data = processor_goods_transection.data
    # do something with the processed data
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
