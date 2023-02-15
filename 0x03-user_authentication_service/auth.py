#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from db import DB, User
from uuid import uuid4
from typing import Optional


def _hash_password(password: str) -> bytes:
    """ hash password """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(12))


def _generate_uuid() -> str:
    """ generate new uuid """
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ check valid user """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode("utf-8"), user.hashed_password):
                return True
        except Exception:
            return False
        return False

    def create_session(self, email: str) -> Optional[str]:
        """ create session id for user """
        try:
            user = self._db.find_user_by(email=email)
            uid = _generate_uuid()
            user.session_id = uid
            self._db._session.commit()
            return uid
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """ get User from session_id """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id) -> None:
        """ remove user from session """
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
            self._db._session.commit()
        except Exception:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """ generate reset token"""
        try:
            user = self._db.find_user_by(email=email)
            uid = _generate_uuid()
            user.reset_token = uid
            self._db._session.commit()
            return uid
        except Exception:
            raise ValueError
