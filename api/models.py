from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Doctor(db.Model):
    __tablename__ = 'doctores'
    id = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(15), nullable=False)
    especialidad = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Doctor {self.nombre} - {self.especialidad}>"
