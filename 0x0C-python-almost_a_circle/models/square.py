#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, which is a special case of a rectangle
    with equal width and height.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): An optional identifier for the square.
    Methods:
        __init__(self, size, x=0, y=0, id=None):
            Initializes a new Square instance.
        __str__(self):
            Returns a string representation of the square.
        update(self, *args, **kwargs):
            Updates attributes of the square.
        to_dictionary(self):
            Converts the square's attributes to a dictionary.
    Properties:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position
            (default is 0).
            y (int, optional): The y-coordinate of the square's position
            (default is 0).
            id (int, optional): An identifier for the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes of the square.

        Args:
            *args: Positional arguments for id, size, x, and y.
            **kwargs: Keyword arguments for id, size, x, and y.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """
        Convert the square's attributes to a dictionary.

        Returns:
            dict: A dictionary containing the square's attributes.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
