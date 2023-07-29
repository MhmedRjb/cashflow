from flask import  render_template, request, redirect, url_for, flash, session ,Blueprint 
from werkzeug.security import check_password_hash
from .authorizationFunction import read_user_by_username



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
            return redirect(url_for('CFinsertfunctions.home'))

    return render_template('authorization.html')


@authorization_bp.route('/logout')
def logout():
    # Clear the session data to log the user out
    session.clear()
    return redirect(url_for('authorization.authorization'))
