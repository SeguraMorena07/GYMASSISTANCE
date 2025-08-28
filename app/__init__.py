# app/__init__.py
import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    # Config básica (podés moverla a app/config luego)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret")

    # Registrar Blueprints (rutas)
    from .resources.home import home_bp
    app.register_blueprint(home_bp)

    return app
