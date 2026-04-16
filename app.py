from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mine", methods=["POST"])
def mine():
    data = request.json
    user_id = str(data.get("user_id"))

    if user_id not in users:
        users[user_id] = 0

    users[user_id] += 1

    return jsonify({"balance": users[user_id]})

@app.route("/balance", methods=["POST"])
def balance():
    data = request.json
    user_id = str(data.get("user_id"))

    return jsonify({"balance": users.get(user_id, 0)})
