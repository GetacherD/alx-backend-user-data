#!/urs/bin/env python3
"""
saved session
"""
from models.base import Base


class UserSession(Base):
    """ saved User session """

    def __init__(self, *args: list, **kwargs: dict):
        """ initialize"""
        self.user_id = ""
        self.session_id = ""
