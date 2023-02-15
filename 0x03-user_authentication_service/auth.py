#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from db import DB, User


def _hash_password(password: str) -> bytes:
    """ hash password """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(12))


class Auth:
    """ Auth class to interact with authentication db. """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register_user"""
        """ check if user exists """
        try:
            usr = self._db.find_user_by(email=email)
        except Exception:
            usr = None
        if usr:
            raise ValueError(f"User {email} already exists")
        pwd = _hash_password(password)
        return self._db.add_user(email, pwd)
