from flask import Flask, request, jsonify

app = Flask(__name__)

customers = {}
current_id = 1

# POST – Create Customer
@app.route("/customers", methods=["POST"])
def create_customer():
    global current_id
    data = request.get_json()

    customer = {
        "id": current_id,
        "name": data["name"],
        "email": data["email"],
        "balance": data.get("balance", 0)
    }

    customers[current_id] = customer
    current_id += 1

    return jsonify(customer), 201


# GET – Retrieve Customer
@app.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = customers.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify(customer), 200


if __name__ == "__main__":
    app.run(debug=True)
