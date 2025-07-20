from flask import Flask
from .display_options import display_options_bp
from .generate_sku import sku_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(display_options_bp)
    app.register_blueprint(sku_bp)
    return app

