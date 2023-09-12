#!/usr/bin/python3
"""
This module defines a function, write_file(filename="", text=""),
for writing text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes the provided text to a file.

    Args:
        filename (str, optional): The name of the file to write.
        Defaults to an empty string.
        text (str, optional): The text to write to the file.
        Defaults to an empty string.
    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
