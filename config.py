from flaskext.mysql import MySQL
import time
from src.components.databaseAccess import databaseAccess as dbcon
class Config(object):

    LANGUAGES = {
        'en': 'English',
        'fr': 'Français',
        'ar': 'العربية'
        # Add more languages as needed
    }

    # Default language
    BABEL_DEFAULT_LOCALE = 'ar'

    SECRET_KEY = '123456789'
    DEBUG = True
    # MySQL configuration
class DevelopmentConfig(Config):
    BABEL_DEFAULT_LOCALE = 'en'
    pass
class ProductionConfig(Config):
    DEBUG = False

...
def init_db(app):
   mysql = MySQL()
   app.config['MYSQL_DATABASE_USER'] = 'root'
   app.config['MYSQL_DATABASE_PASSWORD'] = '123qweasdzxcSq'
   app.config['MYSQL_DATABASE_DB'] = 'test'
   app.config['MYSQL_DATABASE_HOST'] = 'localhost'
   mysql.init_app(app)

   return mysql

def exporter_funx( mysql,user,password,host,db):
    exporter =None
    while not exporter:
        try:
            exporter = dbcon(
                mysql,
                user,
                password,
                host,
                db
                )

        except Exception as e:
            print(f"Error connecting to MySQL: {e}")
            time.sleep(2)
    return exporter
