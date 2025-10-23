# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Inicializar Flask
app = Flask(__name__)

# Configuración de la base de datos desde variable de entorno
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Importar modelos para que SQLAlchemy los registre
from app.models.user import User, Membresia, Asistencia

# Registrar blueprints
from app.resources.home import home_bp
app.register_blueprint(home_bp)

# Crear tablas si no existen (solo para desarrollo)
@app.before_first_request
def crear_tablas():
    db.create_all()

# Punto de entrada
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)