#!/usr/bin/python3
"""
This module defines a function, to_json_string(my_obj),
for converting an object to a JSON-encoded string.
"""
import json


def to_json_string(my_obj):
    """
    Converts an object to a JSON-encoded string.

    Args:
        my_obj: The object to be converted to a JSON string.
    Returns:
        str: A JSON-encoded string representation of the object.
    """
    return json.dumps(my_obj)
