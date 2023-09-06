#!/usr/bin/python3
"""This module defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
       Perform matrix multiplication using NumPy.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.
    Returns:
        numpy.ndarray: The result of matrix multiplication.
    """
    return np.matmul(m_a, m_b)
