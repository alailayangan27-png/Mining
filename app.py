from flask import Flask, render_template, jsonify, request
import time
import random

app = Flask(__name__)

users = {}

MINING_BASE = 0.2

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sync", methods=["POST"])
def sync():
    data = request.json
    user_id = str(data.get("user_id"))

    if user_id not in users:
        users[user_id] = {
            "balance": 0,
            "last_time": time.time(),
            "speed": 1
        }

    user = users[user_id]

    now = time.time()
    elapsed = now - user["last_time"]

    earned = elapsed * MINING_BASE * user["speed"]
    user["balance"] += earned
    user["last_time"] = now

    return jsonify({
        "balance": round(user["balance"], 2),
        "speed": user["speed"]
    })

@app.route("/upgrade", methods=["POST"])
def upgrade():
    data = request.json
    user_id = str(data.get("user_id"))

    user = users[user_id]

    cost = user["speed"] * 10

    if user["balance"] >= cost:
        user["balance"] -= cost
        user["speed"] += 1

    return jsonify({
        "balance": round(user["balance"], 2),
        "speed": user["speed"]
    })

@app.route("/chart")
def chart():
    # generate fake price data
    data = []
    price = 100

    for i in range(30):
        price += random.uniform(-2, 2)
        data.append(round(price, 2))

    return jsonify(data)
