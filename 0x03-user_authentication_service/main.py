#!/usr/bin/env python3
"""
Main test File
"""
import requests
from db import User, DB
from auth import Auth
from typing import Optional
conn = Auth()


def register_user(email: str, password: str) -> None:
    """ test register_user """
    conn.register_user(email, password)


def log_in_wrong_password(email: str, password: str) -> None:
    """ check incorrect password """
    data = {"email": email, "password": password}
    resp = requests.post("http://0.0.0.0:5000/sessions", data=data)
    assert resp.status_code == 401


def log_in(email: str, password: str) -> Optional[str]:
    """ log in user """
    sid = None
    if conn.valid_login(email, password):
        sid = conn.create_session(email)
    return sid


def profile_unlogged() -> None:
    """ anonymous user """
    cookies = {"session_id": None}
    resp = requests.get("http://0.0.0.0:5000/profile", cookies=cookies)
    assert resp.status_code == 403


def profile_logged(session_id: str) -> None:
    """ logged profile """
    cookies = {"session_id": session_id}
    resp = requests.get("http://0.0.0.0:5000/profile", cookies=cookies)
    assert resp.status_code == 200


def log_out(session_id: str) -> None:
    """ log out test"""
    resp = requests.delete("http://0.0.0.0:5000/sessions",
                           cookies={"session_id": session_id})
    assert resp.status_code == 200


def reset_password_token(email: str) -> str:
    """ reset password token """
    return conn.get_reset_password_token(email)


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ update password """
    data = {"email": email, "reset_token": reset_token,
            "new_password": new_password}
    resp = requests.put("http://0.0.0.0:5000/reset_password", data=data)
    ans = {"email": data.get("email"), "message": "Password updated"}
    assert resp.json() == ans


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
