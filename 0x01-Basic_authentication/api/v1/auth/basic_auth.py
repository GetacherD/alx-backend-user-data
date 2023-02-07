#!/usr/bin/env python3
"""
basic auth
"""
from .auth import Auth
from typing import Optional


class BasicAuth(Auth):
    """ Basic Auth class """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> Optional[str]:
        """ extract_base64_authorization_header """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]
