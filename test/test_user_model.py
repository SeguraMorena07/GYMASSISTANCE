from app.models.user import User

def test_user_model_fields():
    user = User(nombre="Santi", email="santi@gmail.com", password="1234", rol="cliente")
    assert user.nombre == "Santi"
    assert user.email == "santi@gmail.com"
    assert user.password == "1234"
    assert user.rol == "cliente"
    assert repr(user) == "<User Santi (cliente)>"