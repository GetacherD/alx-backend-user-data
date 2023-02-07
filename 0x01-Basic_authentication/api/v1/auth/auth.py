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
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        _path = path
        if _path[-1] != "/":
            _path = _path + "/"
        if _path in excluded_paths:
            print(_path, "in",  excluded_paths)
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header """
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """ get current logged in user """
        return None
