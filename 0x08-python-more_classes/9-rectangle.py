#!/usr/bin/python3
"""This module defines a basic Rectangle class."""


class Rectangle:
    """This class represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): The number of Rectangle instances created.
        print_symbol (str): The symbol used for printing the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Creates a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        string += "\n".join(str(self.print_symbol) * self.__width
                            for _ in range(self.__height))
        return string

    def __repr__(self):
        """Return an official string representation of the rectangle.

        Returns:
            str: An official string representation of the rectangle.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor method for Rectangle instances."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to determine the bigger or equal rectangle.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.
        Returns:
            Rectangle: The bigger rectangle or rect_1 if equal in area.
        Raises:
            TypeError: If either rect_1 or rect_2
                is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a square Rectangle instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        Returns:
            Rectangle: A square Rectangle instance with equal width and height.
        """
        return cls(size, size)
