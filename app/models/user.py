from app import db

class User(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f"<User {self.nombre} ({self.rol})>"

class Membresia(db.Model):
    __tablename__ = "membresias"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), unique=True)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    creditos_mensuales = db.Column(db.Integer, nullable=False)

    cliente = db.relationship("User", backref=db.backref("membresia", uselist=False))
    
class Asistencia(db.Model):
    __tablename__ = "asistencias"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)

    cliente = db.relationship("User", backref="asistencias")