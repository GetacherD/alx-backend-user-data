#!/usr/bin/env python3
"""
Basic Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication Class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ decorator to make sure logged in """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization_header """
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """ get current logged in user """
        return None
