#!/usr/bin/python3
"""This module defines a locked class."""


class LockedClass:
    """Defines a locked class.

        The `LockedClass` class is designed to have
        a limited attribute set specified by the `__slots__` attribute.
        Instances of this class can only have an attribute named 'first_name'
        and cannot have any additional attributes added dynamically.

    Attributes:
        first_name (str): A string representing the first name of an object.
    """
    __slots__ = ["first_name"]
