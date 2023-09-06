#!/usr/bin/python3
"""This module defines a function for dividing a matrix by a number."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The input matrix,
                    represented as a list of lists of integers or floats.
        div (int or float): The number to divide each element of the matrix by.
    Returns:
        list of lists: A new matrix with each element divided by 'div',
                 rounded to 2 decimal places.
    Raises:
        TypeError: If 'matrix' is not a list of lists
                containing integers or floats, or if 'div' is not
                a number (int or float).
        ZeroDivisionError: If 'div' is equal to 0.
        TypeError: If the rows of the matrix have different sizes.
    """
    if (not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)
            or not all((isinstance(number, int) or isinstance(number, float))
                       for row in matrix for number in row)):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
