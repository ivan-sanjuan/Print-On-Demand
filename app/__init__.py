from flask import Flask
from .generate_sku import generate_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(generate_bp)
    return app

