from flask import Flask, render_template, jsonify, request
import time

app = Flask(__name__)

users = {}

MINING_RATE = 0.5  # coin per detik

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
            "last_time": time.time()
        }

    now = time.time()
    last = users[user_id]["last_time"]

    # hitung auto mining
    earned = (now - last) * MINING_RATE
    users[user_id]["balance"] += earned
    users[user_id]["last_time"] = now

    return jsonify({
        "balance": round(users[user_id]["balance"], 2)
    })
