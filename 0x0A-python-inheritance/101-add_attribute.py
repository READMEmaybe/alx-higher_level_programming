#!/usr/bin/python3
"""This module defines a function, add_attribute(obj, attribute, value),
for adding a new attribute to an object if it supports it.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute with a specified value to an object if it supports it.

    Args:
        obj: The object to which the attribute will be added.
        attribute (str): The name of the attribute to add.
        value: The value to assign to the new attribute.
    Raises:
        TypeError: If the object does not support adding new attributes.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
