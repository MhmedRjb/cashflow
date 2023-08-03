import time
from flask import Flask, g
from flask_cors import CORS
from flaskext.mysql import MySQL
from src.blueprint.main.authorization import authorization_bp
from src.blueprint.CF import (
    CFactiveTables_bp, CFstartButtons_bp,
    CFinsertfunctions_bp, CFReportes_bp,
    ParallelSYS_bp, FileHandler_bp,
)
from src.data.databaseAccess import databaseAccess2 as dbcon2
from src.data.databaseAccess import databaseAccess as dbcon
from src.config import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)
    CORS(app)
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = '123qweasdzxcSq'
    app.config['MYSQL_DATABASE_DB'] = 'elfateh'
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    mysql.init_app(app)

    app.register_blueprint(authorization_bp)
    app.register_blueprint(CFactiveTables_bp)
    app.register_blueprint(CFstartButtons_bp)
    app.register_blueprint(CFinsertfunctions_bp)
    app.register_blueprint(ParallelSYS_bp)
    app.register_blueprint(CFReportes_bp)
    app.register_blueprint(FileHandler_bp)

    exporter2 = None
    exporter =dbcon(app.config['MYSQL_DATABASE_USER'],app.config['MYSQL_DATABASE_PASSWORD'],app.config['MYSQL_DATABASE_HOST'],app.config['MYSQL_DATABASE_DB'])

    while not exporter2:
        try:
            exporter2 = dbcon2(mysql)
            exporter =dbcon(app.config['MYSQL_DATABASE_USER'],app.config['MYSQL_DATABASE_PASSWORD'],app.config['MYSQL_DATABASE_HOST'],app.config['MYSQL_DATABASE_DB'])


        except Exception as e:
            print(f"Error connecting to MySQL: {e}")
            time.sleep(2)

    @app.before_request
    def before_request2():
        g.db_access2 = exporter2
        g.db_access = exporter

    return app

if __name__ == '__main__':
    app = create_app()
    create_app().run(host='0.0.0.0', port=5000)
