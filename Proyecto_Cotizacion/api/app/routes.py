from flask import Blueprint, request, jsonify
from api.app.services.cotizacion import Cotizacion

api = Blueprint('api', __name__)

@api.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    cotizacion = Cotizacion(data['cliente'], data['ventanas'])
    total = cotizacion.calcular_total()
    return jsonify({"total": total})
