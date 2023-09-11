#!/usr/bin/python3
"""
This module defines a function, inherits_from(obj, a_class),
for checking if an object's type inherits from a specific class.
"""


def inherits_from(obj, a_class):
    """
       Checks if an object's type inherits from a specific class.

    Args:
        obj: The object whose type to check.
        a_class: The class to check if the object's type inherits from.
    Returns:
        bool: True if the object's type inherits from the specified class,
                and the object's type is not the same as the specified class;
                otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
