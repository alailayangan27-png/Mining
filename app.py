from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# fake database (sementara)
balance = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mine", methods=["POST"])
def mine():
    global balance
    balance += 1
    return jsonify({"balance": balance})

@app.route("/balance")
def get_balance():
    return jsonify({"balance": balance})
