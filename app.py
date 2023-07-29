from flask import Flask
from flask_cors import CORS  # Import the CORS extension

from src.blueprint.main.authorization import authorization_bp

from src.blueprint.CF.CFactiveTables import CFactiveTables_bp
from src.blueprint.CF.CFstartButtons import CFstartButtons_bp
from src.blueprint.CF.CFinsertfunctions import CFinsertfunctions_bp
from src.blueprint.CF.CFReportes import CFReportes_bp
from src.blueprint.CF.ParallelSYS import ParallelSYS_bp
from src.blueprint.CF.FileHandler import FileHandler_bp

def create_app():
    app = Flask(__name__,static_folder='static',template_folder='templates')
    app.config['SECRET_KEY'] = '123456789'
    app.register_blueprint(authorization_bp)
    app.register_blueprint(CFactiveTables_bp)
    app.register_blueprint(CFstartButtons_bp)
    app.register_blueprint(CFinsertfunctions_bp)
    app.register_blueprint(ParallelSYS_bp)
    app.register_blueprint(CFReportes_bp)
    app.register_blueprint(FileHandler_bp)

    return app

def start_server():
    create_app().run(debug=True, port=8000)

if __name__ == '__main__':
    start_server()