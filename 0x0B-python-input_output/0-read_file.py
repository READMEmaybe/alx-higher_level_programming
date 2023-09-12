#!/usr/bin/python3
"""
This module defines a function, read_file(filename=""),
for reading and printing the contents of a file.
"""


def read_file(filename=""):
    """
    Reads and prints the contents of a file.

    Args:
        filename (str, optional): The name of the file to read.
        Defaults to an empty string.
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
