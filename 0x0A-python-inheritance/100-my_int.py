#!/usr/bin/python3
"""
This module defines a custom integer class, MyInt,
with inverted equality operators.
"""


class MyInt(int):
    """
    A custom integer class that inverts the equality operators.

    This class inherits from the built-in int class but reverses the behavior
    of the equality operators '==' and '!='.

    Args:
        int (int): An integer value to initialize the MyInt instance.
    Methods:
        __eq__(self, other): Overrides the '==' operator to return
        the opposite of the default behavior.
        __ne__(self, other): Overrides the '!=' operator to return
        the opposite of the default behavior.
    """
    def __eq__(self, other):
        """
        Overrides the '==' operator to return the opposite of
        the default behavior.

        Args:
            other (int): The integer to compare with.
        Returns:
            bool: True if the integers are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the '!=' operator to return the opposite of
        the default behavior.

        Args:
            other (int): The integer to compare with.
        Returns:
            bool: True if the integers are equal, False otherwise.
        """
        return super().__eq__(other)
