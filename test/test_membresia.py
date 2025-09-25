from app.models.user import Membresia
from datetime import date

def test_membresia_fields():
    membresia = Membresia(
        cliente_id=1,
        fecha_inicio=date(2025, 9, 1),
        fecha_fin=date(2025, 10, 1),
        creditos_mensuales=10
    )
    assert membresia.cliente_id == 1
    assert membresia.creditos_mensuales == 10
    assert membresia.fecha_inicio < membresia.fecha_fin