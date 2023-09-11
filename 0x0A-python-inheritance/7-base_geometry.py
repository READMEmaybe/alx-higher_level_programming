#!/usr/bin/python3
"""This module defines a base class, BaseGeometry, for geometric objects."""


class BaseGeometry:
    """
    A base class for geometric objects.

    This class serves as the foundation for defining various geometric objects
    and their properties.

    Methods:
        area(): Placeholder method for calculating the area of a geometric
            object.
    """
    def area(self):
        """
        Placeholder method for calculating the area of a geometric object.

        Raises:
            Exception: This method should be implemented in subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
