from datetime import datetime ,timedelta
from ..main.authorizationFunction import read_user_by_id
from flask import session


def get_current_date(days:int = 0):
    return (datetime.now() + timedelta(days)).date()

def authoreName():
    user = read_user_by_id(session.get('user_id'))
    report_author = user['username'] if user is not None else "Unknown"
    return report_author

def fristlettersINuserANDdate():
    author_initials = ''.join([name[0] for name in authoreName().split('_')]).upper()
    report_date = get_current_date()
    formatted_date = report_date.strftime('%d%m%y')
    report_number = f'{author_initials}{formatted_date}'
    return report_number



