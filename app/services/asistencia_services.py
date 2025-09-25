from datetime import datetime
from app import db
from app.models import Asistencia, Membresia, User

def registrar_asistencia(cliente_id):
    cliente = User.query.get(cliente_id)
    if cliente.rol != "cliente":
        return "Solo los clientes pueden registrar asistencia"

    membresia = cliente.membresia
    if not membresia or membresia.creditos_mensuales <= 0:
        return "No tiene créditos disponibles"

    nueva_asistencia = Asistencia(
        cliente_id=cliente_id,
        fecha=datetime.today().date(),
        hora=datetime.now().time()
    )

    membresia.creditos_mensuales -= 1
    db.session.add(nueva_asistencia)
    db.session.commit()

    return "Asistencia registrada correctamente"

#Test no realizado