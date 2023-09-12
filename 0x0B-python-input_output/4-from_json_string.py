#!/usr/bin/python3
"""
This module defines a function, from_json_string(my_str),
for parsing a JSON-encoded string and returning an object.
"""
import json


def from_json_string(my_str):
    """
    Parses a JSON-encoded string and returns an object.

    Args:
        my_str (str): The JSON-encoded string to be parsed.
    Returns:
        object: The object represented by the JSON string.
    """
    return json.loads(my_str)
