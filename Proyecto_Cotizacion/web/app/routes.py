from flask import Blueprint, render_template, request
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate', methods=['POST'])
def generate_pdf():
    data = {
        "cliente": {
            "nombre": request.form['nombre'],
            "email": request.form['email']
        },
        "ventanas": [
            {
                "alto": float(request.form['alto']),
                "ancho": float(request.form['ancho']),
                "precio": float(request.form['precio'])
            }
        ]
    }
    response = requests.post("http://api:5000/api/calculate", json=data)
    return response.json()
