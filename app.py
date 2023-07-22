from flask import Flask

# Import Blueprints
from src.blueprint.reportsTables import displaytables_bp
from src.blueprint.cashFlowButtons import cashFlowButtons_bp
from src.blueprint.Functions import appfunctions_bp
from src.blueprint.inventorySYS import inventorySYS_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456789'
    
    # Register Blueprints
    app.register_blueprint(displaytables_bp)
    app.register_blueprint(cashFlowButtons_bp)
    app.register_blueprint(appfunctions_bp)
    app.register_blueprint(inventorySYS_bp)

    return app

def start_server():
    create_app().run(debug=True, host="0.0.0.0")

if __name__ == '__main__':
    start_server()