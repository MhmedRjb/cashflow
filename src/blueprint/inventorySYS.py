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



inventorySYS_bp=Blueprint('inventorySYS',__name__)
class inventorySYS():
    @inventorySYS_bp.route('/Elfateh/main/Inventory/')
    def inventory():
        return render_template('commingsoonreports.html')
    
    @inventorySYS_bp.route('/Elfateh/main/reports/clinets_statistics')
    def clinets_statistics():
        return render_template('commingsoonreports.html')
    
    @inventorySYS_bp.route('/Elfateh/main/reports/genral_statistics')
    def genral_statistics():
        return render_template('commingsoonreports.html')
