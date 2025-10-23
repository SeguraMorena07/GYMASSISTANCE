from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.settings import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Importar modelos
    from app.models.user import User, Membresia, Asistencia

    # Crear tablas automáticamente (solo en desarrollo)
    try:
        with app.app_context():
            db.create_all()
            print("✅ Tablas creadas correctamente")
    except Exception as e:
        print("❌ Error al crear las tablas:", e)

    # Registrar blueprints
    from app.resources.home import home_bp
    app.register_blueprint(home_bp)

    return app