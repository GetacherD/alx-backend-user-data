#!/usr/bin/env python3
"""
basic auth
"""
from .auth import Auth
from typing import Optional, TypeVar
import base64
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extract_user_credentials """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        data = decoded_base64_authorization_header.split(":")
        return (data[0], data[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ get user object """
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        u = User.search({"email": user_email})
        if not u:
            return None
        for user in u:
            if user.is_valid_password(user_pwd):
                return user
        return None
