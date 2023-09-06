#!/usr/bin/python3
"""This module defines a function for formatting
    text with indentation based on punctuation.
"""


def text_indentation(text):
    """Formats text with indentation based on punctuation.

    This function takes a string of text as input and adds line breaks after
    sentences, identified by the punctuation marks '?', '.', and ':'. It also
    removes leading spaces at the beginning of the text.

    Args:
        text (str): The input text to be formatted.
    Raises:
        TypeError: If 'text' is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
