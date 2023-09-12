#!/usr/bin/python3
"""
This module defines a function, append_write(filename="", text=""),
for appending text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends the provided text to a file.

    Args:
        filename (str, optional): The name of the file to append.
        Defaults to an empty string.
        text (str, optional): The text to append to the file.
        Defaults to an empty string.
    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
