#!/usr/bin/python3
"""Square class"""


class Square:
    """The square"""
    def __init__(self, size=0):
        """Initialize Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """computes the area of the square.

        Returns:
            int: the result of the calculation.
        """
        return self.__size ** 2
