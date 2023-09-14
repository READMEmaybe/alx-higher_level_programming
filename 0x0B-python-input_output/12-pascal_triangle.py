#!/usr/bin/python3
"""
This module defines pascal_triangle(n), for generating Pascal's triangle.
Pascal's triangle is a mathematical triangle where each number is the sum of
the two numbers directly above it.The first row is [1], and each subsequent row
is constructed by adding a 1 at each end and filling the remaining numbers with
the sum of the two numbers above it.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.
    Returns:
        List[List[int]]: A list of lists representing Pascal's triangle
        up to the specified number of rows.
    """
    if n <= 0:
        return []

    result = [[1]]
    for i in range(1, n):
        prev_row = result[i - 1]
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        result.append(row)

    return result
