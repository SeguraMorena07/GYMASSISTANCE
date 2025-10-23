# app/resources/home.py

from flask import Blueprint, jsonify
from app.services.asistencia_services import registrar_asistencia

home_bp = Blueprint("home", __name__)

@home_bp.route("/", methods=["GET"])
def index():
    return "Bienvendio a GYMASSISTANCE!"

@home_bp.route("/registrar_asistencia/<int:cliente_id>", methods=["GET"])
def registrar(cliente_id):
    resultado = registrar_asistencia(cliente_id)
    return jsonify({"mensaje": resultado})

@home_bp.route("/ping-db", methods=["GET"])
def ping_db():
    try:
        db.session.execute("SELECT 1")
        return {"status": "Conectado a la base de datos"}
    except Exception as e:
        return {"status": "Error", "detalle": str(e)}
