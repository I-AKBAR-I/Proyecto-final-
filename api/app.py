from flask import Flask, jsonify, request
from models import db, Appointment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/appointments_db'
db.init_app(app)

@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([a.to_dict() for a in appointments])

@app.route('/api/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    new_appointment = Appointment(**data)
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify(new_appointment.to_dict()), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5432)
