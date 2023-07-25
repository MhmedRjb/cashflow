from flask import Flask
from src.blueprint.main.login import login_bp

from src.blueprint.CF.CFactiveTables import CFactiveTables_bp
from src.blueprint.CF.CFstartButtons import CFstartButtons_bp
from src.blueprint.CF.CFstartfunctions import CFstartfunctions_bp
from src.blueprint.CF.CFReportes import CFReportes_bp

from src.blueprint.ParallelSYS import ParallelSYS_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456789'
    app.register_blueprint(login_bp)
    app.register_blueprint(CFactiveTables_bp)
    app.register_blueprint(CFstartButtons_bp)
    app.register_blueprint(CFstartfunctions_bp)
    app.register_blueprint(ParallelSYS_bp)
    app.register_blueprint(CFReportes_bp)

    return app

def start_server():
    create_app().run(debug=True, host="0.0.0.0")

if __name__ == '__main__':
    start_server()