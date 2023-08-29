#!/usr/bin/python3
"""Square class"""


class Square:
    """The square"""
    def __init__(self, size=0):
        """Initialize Square"""
        self.size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
