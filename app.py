from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# database sederhana
users = {}

@app.route("/")
def home():
    return "API RUNNING"

# simpan deposit
@app.route("/deposit", methods=["POST"])
def deposit():
    user_id = request.json.get("user_id")
    amount = float(request.json.get("amount"))

    if user_id not in users:
        users[user_id] = {"total": 0}

    users[user_id]["total"] += amount

    return jsonify({
        "total": users[user_id]["total"]
    })

# ambil data user
@app.route("/user", methods=["POST"])
def get_user():
    user_id = request.json.get("user_id")

    if user_id not in users:
        users[user_id] = {"total": 0}

    return jsonify(users[user_id])
