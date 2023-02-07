#!/usr/bin/env python3
"""
basic auth
"""
from .auth import Auth
from typing import Optional
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> Optional[str]:
        """ decode_base64_authorization_header """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            return base64.b64decode(
                base64_authorization_header.encode("utf-8")).decode("utf-8")
        except Exception:
            return None
