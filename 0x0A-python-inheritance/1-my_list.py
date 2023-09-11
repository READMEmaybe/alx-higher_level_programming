#!/usr/bin/python3
"""
This module defines a custom class, MyList,
which is a subclass of the built-in list class.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class
    and adds a method for printing the list in sorted order.
    """
    def print_sorted(self):
        """Prints the elements of the list in sorted order."""
        print(sorted(self))
