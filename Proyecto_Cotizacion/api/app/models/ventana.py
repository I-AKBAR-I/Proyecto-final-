from api.app import db

class Ventana(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alto = db.Column(db.Float, nullable=False)
    ancho = db.Column(db.Float, nullable=False)
    precio = db.Column(db.Float, nullable=False)
