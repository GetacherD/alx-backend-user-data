#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, jsonify
from auth import Auth
from flask import request


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def index():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", strict_slashes=False, methods=["POST"])
def users():
    """ create user route """
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        try:
            user = AUTH.register_user(email, password)
            return jsonify({"email": f"{email}", "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
