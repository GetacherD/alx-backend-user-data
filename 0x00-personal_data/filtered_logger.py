#!/usr/bin/env python3
"""
Regex scramble user data
"""
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str, message: str,
                 separator: str) -> str:
    """ Regex filter and replace some data inside string"""
    data = message.split(separator)
    return ";".join([re.sub("(.*=)(.*)", r"\1" + redaction, d)
                     if d.split("=")[0] in fields else d for d in data])
