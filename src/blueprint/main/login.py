from flask import Flask, render_template, request, redirect, url_for, flash, session ,Blueprint
from werkzeug.security import check_password_hash
from src.data.databaseIniti import exporter

login_bp=Blueprint('login',__name__)


def read_user_by_username(username):
    # Execute the query to find the user by the provided username
    sql = f"SELECT * FROM user WHERE username = '{username}'"
    data = exporter.readsql(sql)
    
    # If data is not empty, return the first row as a dictionary, otherwise return None
    return data.iloc[0].to_dict() if not data.empty else None

def read_user_by_id(user_id):
    # Execute the query to find the user by the provided user ID
    sql = f"SELECT * FROM user WHERE id = {user_id}"
    data = exporter.readsql(sql)
    
    # If data is not empty, return the first row as a dictionary, otherwise return None
    return data.iloc[0].to_dict() if not data.empty else None

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = read_user_by_username(username)

        if user is None:
            flash('Incorrect username.')
        elif not check_password_hash(user['password'], password):
            flash('Incorrect password.')
        else:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('CFstartfunctions.home'))

    return render_template('login.html')


from functools import wraps
from flask import session, flash, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You need to log in first.')
            return redirect(url_for('login.login'))
        return f(*args, **kwargs)
    return decorated_function
