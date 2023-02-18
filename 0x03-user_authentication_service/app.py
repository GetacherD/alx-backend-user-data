#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, jsonify, abort, make_response, redirect, url_for
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


@app.route("/sessions", strict_slashes=False, methods=["POST"])
def login():
    """ log in user """
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if not AUTH.valid_login(email, password):
            abort(401)
        sid = AUTH.create_session(email)
        resp = make_response(
            jsonify({"email": f"{email}", "message": "logged in"}))
        resp.set_cookie("session_id", sid)
        return resp


@app.route("/sessions", strict_slashes=False, methods=["DELETE"])
def logout() -> str:
    """ log out user session """
    if request.method == "DELETE":
        sid = request.cookies.get("session_id")
        if sid:
            user = AUTH.get_user_from_session_id(sid)
            if user:
                AUTH.destroy_session(user.id)
                return redirect(url_for("index"))
        else:
            abort(403)


@app.route("/profile", strict_slashes=False)
def profile():
    """ display user profile """
    sid = request.cookies.get("session_id")
    if sid:
        user = AUTH.get_user_from_session_id(sid)
        if user:
            email = user.email
            return jsonify({"email": email}), 200
    abort(403)


@app.route("/reset_password", strict_slashes=False, methods=["POST"])
def get_reset_password_token():
    """ get reset password token """
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except Exception:
        abort(403)


@app.route("/reset_password", strict_slashes=False, methods=["PUT"])
def update_password():
    """ update password"""
    form_data = request.form
    if "email" not in form_data:
        return jsonify({"message": "email required"}), 400
    if "reset_token" not in form_data:
        return jsonify({"message": "reset_token required"}), 400
    if "new_password" not in form_data:
        return jsonify({"message": "new_password required"}), 400
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
