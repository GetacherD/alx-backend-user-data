#!/usr/bin/env python3

"""
bcrypt for password
"""
import bcrypt as BC


def hash_password(password: str) -> bytes:
    """ hash_password """
    return BC.hashpw(password.encode("utf-8"), BC.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ check if password is valid"""
    return BC.checkpw(password.encode("utf-8"), hashed_password)
