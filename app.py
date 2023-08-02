from flask import Flask ,g
from flask_cors import CORS
#IMport flask mysql
from flaskext.mysql import MySQL

from src.blueprint.main.authorization import authorization_bp

from src.blueprint.CF.CFactiveTables import CFactiveTables_bp
from src.blueprint.CF.CFstartButtons import CFstartButtons_bp
from src.blueprint.CF.CFinsertfunctions import CFinsertfunctions_bp
from src.blueprint.CF.CFReportes import CFReportes_bp
from src.blueprint.CF.ParallelSYS import ParallelSYS_bp
from src.blueprint.CF.FileHandler import FileHandler_bp
# from src.data.databaseAccess import databaseAccess as dbcon 
from src.data.databaseAccess import databaseAccess2 as dbcon2

from src.config import DevelopmentConfig,ProductionConfig 
 



def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    CORS(app)
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = '123qweasdzxcSq'
    app.config['MYSQL_DATABASE_DB'] = 'elfateh'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    app.register_blueprint(authorization_bp)
    app.register_blueprint(CFactiveTables_bp)
    app.register_blueprint(CFstartButtons_bp)
    app.register_blueprint(CFinsertfunctions_bp)
    app.register_blueprint(ParallelSYS_bp)
    app.register_blueprint(CFReportes_bp)
    app.register_blueprint(FileHandler_bp)


    # exporter = dbcon(app.config['DB_USERNAME'], app.config['DB_PASSWORD'], app.config['DB_HOSTNAME'], app.config['DB_DATABASE'])
    exporter2 = dbcon2(mysql)
   
   
    @app.before_request
    def before_request2():
        g.db_access2 = exporter2
        # g.db_access = exporter

    return app




if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
