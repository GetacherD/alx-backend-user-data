#!/usr/bin/env python3
"""
expire session demo
"""
from .session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ expire session class """

    def __init__(self):
        """ initialize objects """

        try:
            self.session_duration = int(getenv("SESSION_DURATION"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ overload create_session """
        res = super().create_session(user_id)
        if not res:
            return None
        self.user_id_by_session_id[res] = {
            "user_id": user_id, "created_at": datetime.now()}
        return res

    def user_id_for_session_id(self, session_id=None):
        """ get user_id for session """
        if session_id is None:
            return None
        print(session_id, "session_id", self.user_id_by_session_id)
        if session_id not in self.user_id_by_session_id:
            return None

        if not self.user_id_by_session_id.get(session_id).get("created_at"):
            return None
        tm = self.user_id_by_session_id.get(session_id).get("created_at")
        print(tm)
        future = self.user_id_by_session_id.get(session_id).get(
            "created_at") + timedelta(seconds=self.session_duration)
        now = datetime.now()
        if future < now:
            print("Gena New")
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id.get(session_id)
        return self.user_id_by_session_id.get(session_id).get("user_id")
