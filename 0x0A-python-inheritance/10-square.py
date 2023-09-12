#!/usr/bin/python3
"""This module defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, which inherits from Rectangle.

    This class defines attributes for size and provides validation
    for the size.

    Args:
        size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with the specified size.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
