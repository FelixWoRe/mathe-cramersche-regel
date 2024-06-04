import math as ma
from random import randint
matrix_size = 11
import copy

def calc_matrix_type(matrix):
    type = {"row": 0, "column": 0}
    if len(matrix) == 0:
        return type
    type["row"] = len(matrix)
    type["column"] = len(matrix[0])
    return type


def is_square_matrix(matrix):
    type = calc_matrix_type(matrix)
    return type["row"] == type["column"]


def is_diagonal_matrix(matrix):
    if not is_square_matrix(matrix):
        return False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] != 0:
                return False
    return True


def is_identity_matrix(matrix):
    if not is_diagonal_matrix(matrix):
        return False
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            return False
    return True


def calc_determinant(matrix):
    if not is_square_matrix(matrix):
        return None
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for i in range(len(matrix)):
        det += matrix[0][i] * ma.pow(-1, i) * calc_determinant([row[:i] + row[i + 1:] for row in matrix[1:]])
    return det


def generate_matrix(row, column):
    matrix = []
    for i in range(row):
        matrix.append([])
        for j in range(column):
            matrix[i].append(0)
    return matrix


def fill_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = randint(0, 10)
    return matrix


def cramerische_regel(matrix, loesung):
    if not is_square_matrix(matrix):
        return None
    if calc_determinant(matrix) == 0:
        return None
    result = []
    for i in range(len(matrix)):
        new_matrix = copy.deepcopy(matrix)
        for j in range(len(matrix)):
            new_matrix[i][j] = loesung[j]
        result.append(calc_determinant(new_matrix) / calc_determinant(matrix))
    return result

