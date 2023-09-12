#!/usr/bin/python3
"""
This module defines a function, class_to_json(obj),
for converting a class instance to a JSON-serializable dictionary.
"""


def class_to_json(obj):
    """
    Converts a class instance to a JSON-serializable dictionary.

    Args:
        obj: The class instance to be converted.
    Returns:
        dict: A dictionary containing the class instance's attributes and their values.
    """
    return obj.__dict__
