from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "APP RUNNING ✅"

@app.route("/balance", methods=["POST"])
def balance():
    user_id = request.json.get("user_id")

    if user_id not in users:
        users[user_id] = 1000

    return jsonify({"balance": users[user_id]})

@app.route("/mine", methods=["POST"])
def mine():
    user_id = request.json.get("user_id")

    if user_id not in users:
        users[user_id] = 1000

    users[user_id] += 10

    return jsonify({"balance": users[user_id]})
