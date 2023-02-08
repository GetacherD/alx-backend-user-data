#!/usr/bin/env python3
"""
saved session
"""
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ db session """

    def create_session(self, user_id=None):
        """ create new session """
        pass

    def user_id_for_session_id(self, session_id=None):
        """ set user id """
        pass

    def destroy_session(self, request=None):
        """ destroy_session """
        pass
