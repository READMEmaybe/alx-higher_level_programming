#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, which inherits from BaseGeometry.

    This class defines attributes for width and height and provides validation
    for these attributes.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
