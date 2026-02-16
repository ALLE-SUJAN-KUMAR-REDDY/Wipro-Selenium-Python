from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
customers = {}
current_id = 1


# -------------------------
# HOME (Health Check)
# -------------------------
@app.route("/", methods=["GET"])
def home():
    return "Banking Customer API is running", 200


# -------------------------
# POST – Create Customer
# -------------------------
@app.route("/customers", methods=["POST"])
def create_customer():
    global current_id
    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid request body"}), 400

    customer = {
        "id": current_id,
        "name": data["name"],
        "email": data["email"],
        "balance": data.get("balance", 0)
    }

    customers[current_id] = customer
    current_id += 1

    return jsonify(customer), 201


# -------------------------
# GET – Retrieve Customer by ID
# -------------------------
@app.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = customers.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify(customer), 200


# -------------------------
# GET – Retrieve ALL Customers
# -------------------------
@app.route("/customers", methods=["GET"])
def get_all_customers():
    return jsonify(list(customers.values())), 200


# -------------------------
# PUT – Update Customer
# -------------------------
@app.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    customer = customers.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    data = request.get_json()

    customer["name"] = data.get("name", customer["name"])
    customer["email"] = data.get("email", customer["email"])
    customer["balance"] = data.get("balance", customer["balance"])

    return jsonify(customer), 200


# -------------------------
# DELETE – Remove Customer
# -------------------------
@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    if customer_id not in customers:
        return jsonify({"error": "Customer not found"}), 404

    del customers[customer_id]
    return "", 204


# -------------------------
# POST – Bulk Create Customers (OPTIONAL)
# -------------------------
@app.route("/customers/bulk", methods=["POST"])
def create_customers_bulk():
    global current_id
    data = request.get_json()

    if not isinstance(data, list):
        return jsonify({"error": "Expected a list of customers"}), 400

    created_customers = []

    for item in data:
        customer = {
            "id": current_id,
            "name": item["name"],
            "email": item["email"],
            "balance": item.get("balance", 0)
        }
        customers[current_id] = customer
        created_customers.append(customer)
        current_id += 1

    return jsonify(created_customers), 201


# -------------------------
# RUN APPLICATION
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
