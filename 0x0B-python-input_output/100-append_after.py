#!/usr/bin/python3
"""
This module defines append_after(filename, search_string, new_string),
for appending a string after a specified search string in a text file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a string after a specified search string in a text file.

    Args:
        filename (str): The name of the text file to process.
        search_string (str): The string to search for in each line of the file.
        new_string (str): The string to append after the found search string.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
