#!/usr/bin/env python3
"""
session_authentication demo
"""
from uuid import uuid4
from .auth import Auth


class SessionAuth(Auth):
    """ SessionAuth class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create session """
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        key = str(uuid4())
        self.user_id_by_session_id[key] = user_id
        return key
