from flask import Flask, render_template, jsonify, request
import time

app = Flask(__name__)

users = {}

MAX_ENERGY = 100
ENERGY_REGEN = 5   # per second
MINING_POWER = 0.05

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sync", methods=["POST"])
def sync():
    user_id = str(request.json.get("user_id"))

    if user_id not in users:
        users[user_id] = {
            "balance": 0,
            "energy": MAX_ENERGY,
            "last_time": time.time(),
            "level": 1
        }

    user = users[user_id]

    now = time.time()
    elapsed = now - user["last_time"]

    # regen energy
    user["energy"] = min(MAX_ENERGY, user["energy"] + elapsed * ENERGY_REGEN)

    # mining otomatis (idle)
    mined = elapsed * MINING_POWER * user["level"]
    user["balance"] += mined

    user["last_time"] = now

    return jsonify({
        "balance": round(user["balance"], 2),
        "energy": int(user["energy"]),
        "level": user["level"]
    })

@app.route("/tap", methods=["POST"])
def tap():
    user_id = str(request.json.get("user_id"))
    user = users[user_id]

    if user["energy"] > 1:
        user["energy"] -= 2
        user["balance"] += 1 * user["level"]

    return jsonify({
        "balance": round(user["balance"], 2),
        "energy": int(user["energy"])
    })

@app.route("/upgrade", methods=["POST"])
def upgrade():
    user_id = str(request.json.get("user_id"))
    user = users[user_id]

    cost = user["level"] * 50

    if user["balance"] >= cost:
        user["balance"] -= cost
        user["level"] += 1

    return jsonify({
        "balance": round(user["balance"], 2),
        "level": user["level"]
    })
