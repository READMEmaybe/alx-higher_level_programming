#!/usr/bin/python3
"""
This module defines a function, is_same_class(obj, a_class),
for checking if an object is an instance of a specific class.
"""


def is_same_class(obj, a_class):
    """
        Checks if an object is an instance of a specific class.

    Args:
        obj: The object to check.
        a_class: The class to check against.
    Returns:
         bool: True if the object is an instance of the specified class,
                False otherwise.
    """
    return type(obj) == a_class
