#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        len = len(matrix[i]) - 1
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end=" " if j != len else "")
        print()
