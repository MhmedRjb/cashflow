import time
from flask import Flask, g
from flask_cors import CORS
from flaskext.mysql import MySQL
from src.blueprint.main.authorization import authorization_bp
from src.blueprint.CF import (
    CFactiveTables_bp,
    CFstartButtons_bp,
    CFinsertfunctions_bp,
    CFReportes_bp,
    ParallelSYS_bp,FileHandler_bp,
    )
from src.components.databaseAccess import databaseAccess as dbcon
from src.config import ProductionConfig, DevelopmentConfig ,init_db ,exporter_funx

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    CORS(app)
    mysql = init_db(app)
    app.register_blueprint(authorization_bp)
    app.register_blueprint(CFactiveTables_bp)
    app.register_blueprint(CFstartButtons_bp)
    app.register_blueprint(CFinsertfunctions_bp)
    app.register_blueprint(ParallelSYS_bp)
    app.register_blueprint(CFReportes_bp)
    app.register_blueprint(FileHandler_bp)


    @app.before_request
    def before_request():
    #here is tow ways to connect to the database using flask-mysql and sqlalchemy
    # may someone optimize this part
        g.db_access = exporter_funx(
        mysql,
        app.config['MYSQL_DATABASE_USER'],
        app.config['MYSQL_DATABASE_PASSWORD'],
        app.config['MYSQL_DATABASE_HOST'],
        app.config['MYSQL_DATABASE_DB']
        )

    return app

if __name__ == '__main__':
    # from waitress import serve
    # app = create_app()
    # serve(app, host='0.0.0.0', port=5000)
    app = create_app()
    create_app().run(host='0.0.0.0', port=5000)
