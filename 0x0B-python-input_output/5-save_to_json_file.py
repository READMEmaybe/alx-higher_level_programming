#!/usr/bin/python3
"""
This module defines a function, save_to_json_file(my_obj, filename),
for saving an object to a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a JSON file.

    Args:
        my_obj: The object to be saved to the JSON file.
        filename (str): The name of the JSON file to which
            the object will be saved.
    Note:
        The function will create or overwrite the specified file
        with the serialized JSON data.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
