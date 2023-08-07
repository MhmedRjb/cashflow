from flask import  redirect, url_for, flash
from functools import wraps
from datetime import datetime
from ...components.filepaths import TXT_FILE_path
from werkzeug.security import check_password_hash
TXT_FILE = TXT_FILE_path
from datetime import timedelta
CODE = 'pbkdf2:sha256:600000$xCVdbV9G1DWnBKZv$4462e2070444c20339683c26afba3b73fc36ab42589822927e1e46bd242a0713'
TXT_FILE=TXT_FILE_path

def codeISright(CODE=CODE,TXT_FILE=TXT_FILE):
    with open(TXT_FILE, 'r') as file:
        content = file.read()
        if  check_password_hash(CODE, content.strip()):
            return True
        return  False 

def date_check_required(end_date=datetime(2023,8,6),add_days=0):
    end_date=end_date+timedelta(days=add_days)
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            current_date = datetime.now()
            if current_date <= end_date:
                return f(*args, **kwargs)
            else:
                    if not codeISright():
                        flash('انتهي مدة الثلاثين يوم برجاء ارسال45 دولار لتجديد مدى الحياة .','success')
                        return redirect(url_for('authorization.error'))

            return f(*args, **kwargs)

        return decorated_function
    return decorator



