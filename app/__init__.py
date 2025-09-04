from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.settings import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Importar modelos para que las migraciones los detecten
    from app import models  

    # Registrar blueprints
    from .resources.home import home_bp
    app.register_blueprint(home_bp)

    return app
