from flask import  redirect, url_for, flash, session ,Blueprint 
from src.data.databaseIniti import exporter
from functools import wraps
from src.components import sqlcommonds as sqlcom


def read_user_by_username(username):
    # Execute the query to find the user by the provided username
    sql = sqlcom.read_user_by_username
    data = exporter.readsql(sql, params=(username,))
    
    # If data is not empty, return the first row as a dictionary, otherwise return None
    return data.iloc[0].to_dict() if not data.empty else None


def read_user_by_id(user_id):
    # Execute the query to find the user by the provided user ID
    sql = "SELECT * FROM user WHERE id = %s"
    data = exporter.readsql(sql, params=(user_id,))
    
    # If data is not empty, return the first row as a dictionary, otherwise return None
    return data.iloc[0].to_dict() if not data.empty else None


def authorization_required(allowed_roles=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash('You need to log in first.')
                return redirect(url_for('authorization.authorization'))

            # Check if the user's role is in the allowed_roles list
            user_role = session.get('user_role')
            if allowed_roles and user_role not in allowed_roles:
                flash('You do not have permission to access this page.')
                return redirect(url_for('authorization.authorization'))

            return f(*args, **kwargs)

        return decorated_function
    return decorator



