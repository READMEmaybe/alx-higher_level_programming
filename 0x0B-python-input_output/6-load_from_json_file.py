#!/usr/bin/python3
"""
This module defines a function, load_from_json_file(filename),
for loading an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.

    Args:
        filename (str): The name of the JSON file from which to load the object
    Returns:
        object: The object loaded from the JSON file.
    Note:
        The function expects that the file contains valid JSON data.
    """
    with open(filename) as f:
        return json.load(f)
