from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {}

@app.route("/")
def home():
    return "API RUNNING"

@app.route("/deposit", methods=["POST"])
def deposit():
    user_id = request.json.get("user_id")
    amount = float(request.json.get("amount"))

    if user_id not in users:
        users[user_id] = {"total": 0}

    users[user_id]["total"] += amount

    return jsonify(users[user_id])

@app.route("/user", methods=["POST"])
def user():
    user_id = request.json.get("user_id")

    if user_id not in users:
        users[user_id] = {"total": 0}

    return jsonify(users[user_id])
