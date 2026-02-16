from flask import Flask, request, jsonify

app = Flask(__name__)

# =====================================================
# In-memory storage
# =====================================================
doctors = {}
patients = {}
appointments = {}

doctor_id_seq = 500
patient_id_seq = 100
appointment_id_seq = 9000
used_phones = set()

# =====================================================
# Authentication (Bearer Token)
# =====================================================
def auth_required():
    token = request.headers.get("Authorization")
    return token and token.startswith("Bearer ")

# =====================================================
# ROOT (Browser friendly)
# =====================================================
@app.route("/", methods=["GET"])
def root():
    return "Healthcare Appointment Management API", 200

# =====================================================
# Health Check
# =====================================================
@app.route("/v1", methods=["GET"])
def health_check():
    return "Healthcare API is running", 200

# =====================================================
# 1️⃣ Doctor Creation
# =====================================================
@app.route("/v1/doctors", methods=["POST"])
def create_doctor():
    global doctor_id_seq

    if not auth_required():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data or "name" not in data or "specialization" not in data:
        return jsonify({"error": "Invalid request"}), 400

    doctor_id_seq += 1
    doctors[doctor_id_seq] = {
        "doctor_id": doctor_id_seq,
        "name": data["name"],
        "specialization": data["specialization"],
        "experience": data.get("experience", 0)
    }

    return jsonify(doctors[doctor_id_seq]), 201

# =====================================================
# 2️⃣ Patient Registration
# =====================================================
@app.route("/v1/patients", methods=["POST"])
def register_patient():
    global patient_id_seq

    if not auth_required():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()

    if data.get("age", 0) < 0 or not data.get("email"):
        return jsonify({"error": "Validation error"}), 400

    if data.get("phone") in used_phones:
        return jsonify({"error": "Duplicate phone number"}), 409

    used_phones.add(data["phone"])
    patient_id_seq += 1

    patients[patient_id_seq] = {
        "patient_id": patient_id_seq,
        "name": data["name"],
        "age": data["age"],
        "email": data["email"],
        "phone": data["phone"]
    }

    return jsonify(patients[patient_id_seq]), 201

# =====================================================
# 3️⃣ Book Appointment
# =====================================================
@app.route("/v1/appointments", methods=["POST"])
def book_appointment():
    global appointment_id_seq

    if not auth_required():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()

    for appt in appointments.values():
        if (
            appt["doctor_id"] == data["doctor_id"]
            and appt["date"] == data["date"]
            and appt["time"] == data["time"]
            and appt["status"] == "BOOKED"
        ):
            return jsonify({"error": "Slot already booked"}), 409

    appointment_id_seq += 1
    appointments[appointment_id_seq] = {
        "appointment_id": appointment_id_seq,
        "patient_id": data["patient_id"],
        "doctor_id": data["doctor_id"],
        "date": data["date"],
        "time": data["time"],
        "status": "BOOKED"
    }

    return jsonify(appointments[appointment_id_seq]), 201

# =====================================================
# 4️⃣ View Appointment
# =====================================================
@app.route("/v1/appointments/<int:appt_id>", methods=["GET"])
def view_appointment(appt_id):
    appt = appointments.get(appt_id)
    if not appt:
        return jsonify({"error": "Appointment not found"}), 404
    return jsonify(appt), 200

# =====================================================
# 5️⃣ Reschedule Appointment
# =====================================================
@app.route("/v1/appointments/<int:appt_id>", methods=["PUT"])
def reschedule_appointment(appt_id):
    appt = appointments.get(appt_id)
    if not appt:
        return jsonify({"error": "Appointment not found"}), 404

    data = request.get_json()

    for a in appointments.values():
        if (
            a["doctor_id"] == appt["doctor_id"]
            and a["date"] == data["date"]
            and a["time"] == data["time"]
            and a["appointment_id"] != appt_id
            and a["status"] == "BOOKED"
        ):
            return jsonify({"error": "Time slot conflict"}), 409

    appt["date"] = data["date"]
    appt["time"] = data["time"]

    return jsonify(appt), 200

# =====================================================
# 6️⃣ Cancel Appointment
# =====================================================
@app.route("/v1/appointments/<int:appt_id>", methods=["DELETE"])
def cancel_appointment(appt_id):
    appt = appointments.get(appt_id)
    if not appt:
        return jsonify({"error": "Appointment already cancelled"}), 410

    del appointments[appt_id]
    return "", 204

# =====================================================
# Run Application
# =====================================================
if __name__ == "__main__":
    app.run(debug=True, port=5001)
