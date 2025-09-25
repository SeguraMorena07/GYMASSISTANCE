from app.models.user import Asistencia
from datetime import date, time

def test_asistencia_fields():
    asistencia = Asistencia(
        cliente_id=1,
        fecha=date.today(),
        hora=time(10, 30)
    )
    assert asistencia.cliente_id == 1
    assert isinstance(asistencia.fecha, date)
    assert isinstance(asistencia.hora, time)