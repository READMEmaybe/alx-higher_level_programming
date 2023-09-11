#!/usr/bin/python3
"""
This module defines a function, is_kind_of_class(obj, a_class),
for checking if an object is an instance of a class or its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """
        Checks if an object is an instance of a specific
        class or its subclasses.

    Args:
        obj: The object to check.
        a_class: The class to check against.
    Returns:
        bool: True if the object is an instance of the specified
            class or any of its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
