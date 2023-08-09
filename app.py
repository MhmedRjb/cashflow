import time
from flask import Flask, g ,request
from flask_babel import Babel ,get_locale
from flask_cors import CORS
from src.blueprint.main.authorization import authorization_bp
from src.blueprint.CF import (
    CFactiveTables_bp,
    CFstartButtons_bp,
    CFinsertfunctions_bp,
    CFReportes_bp,
    ParallelSYS_bp,FileHandler_bp,
    )
from config import ProductionConfig, DevelopmentConfig ,init_db ,exporter_funx

def create_app():
    app = Flask(__name__)
    babel = Babel(app)
    app.config.from_object(ProductionConfig)
    babel.init_app(app, default_locale=app.config['BABEL_DEFAULT_LOCALE'])
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
        g.db_access = exporter_funx(
        mysql,
        app.config['MYSQL_DATABASE_USER'],
        app.config['MYSQL_DATABASE_PASSWORD'],
        app.config['MYSQL_DATABASE_HOST'],
        app.config['MYSQL_DATABASE_DB']
        )


    @app.context_processor
    def inject_get_locale():
        return dict(get_locale=get_locale)


    return app

if __name__ == '__main__':
    from waitress import serve
    app = create_app()
    serve(app, host='0.0.0.0', port=5000)
    # app = create_app()
    # create_app().run(host='0.0.0.0', port=5000)
