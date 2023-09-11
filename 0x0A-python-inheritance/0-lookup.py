#!/usr/bin/python3
"""This module provides a single function, lookup(obj),
for retrieving a list of attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of attributes and methods of an object.

    Args:
        obj: The object for which to retrieve attributes and methods.
    Returns:
        List[str]: A list of strings containing the names of attributes
        and methods associated with the given object.
    """
    return dir(obj)
