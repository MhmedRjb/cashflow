from flask import  render_template, request, redirect, url_for, flash, session ,Blueprint ,g
from werkzeug.security import check_password_hash
from .authorizationFunction import read_user_by_username
from ...components.filepaths import TXT_FILE_path
from .date_check_required import codeISright

authorization_bp=Blueprint('authorization',__name__)


@authorization_bp.route('/authorization', methods=['GET', 'POST'])
def authorization():
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
            session['user_role'] = user['role']
            return redirect(url_for('CFinsertfunctions.authorization'))

    return render_template('authorization.html')


@authorization_bp.route('/logout')
def logout():
    # Clear the session data to log the user out
    session.clear()
    return redirect(url_for('authorization.authorization'))



@authorization_bp.route('/comapny_name/main/error')
def error():
    return render_template('error.html')

@authorization_bp.route('/comapny_name/main/save_code', methods=['POST'])
def save_code():
    code = request.form['code']
    with open(TXT_FILE_path, 'w') as file:
        file.write(code)
    print (code)
    if codeISright():
        flash('Code saved successfully and it is right','success')
    else :
        flash('Code saved successfully but wrong', 'error')
            
    return redirect(url_for('authorization.error'))
