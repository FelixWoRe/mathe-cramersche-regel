from random import randint
import copy
matrix_size = 30

def calc_matrix_type(matrix): # calculate the type of the matrix
    type = {"row": 0, "column": 0} # initialize the type
    if len(matrix) == 0: # check if the matrix is empty
        return None # return None if the matrix is empty
    type["row"] = len(matrix) # calculate the number of rows
    type["column"] = len(matrix[0]) # calculate the number of columns
    return type # return the type of the matrix


def is_square_matrix(matrix): # check if the matrix is square
    type = calc_matrix_type(matrix) # calculate the type of the matrix
    return type["row"] == type["column"] # check if the matrix is square


def is_diagonal_matrix(matrix): # check if the matrix is diagonal
    if not is_square_matrix(matrix): # check if the matrix is square
        return False
    for i in range(len(matrix)): # check if the matrix is diagonal
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] != 0:
                return False
    return True


def is_identity_matrix(matrix): # check if the matrix is identity
    if not is_diagonal_matrix(matrix): # check if the matrix is diagonal
        return False
    for i in range(len(matrix)):
        if matrix[i][i] != 1: # check if the diagonal elements are 1
            return False
    return True


def calc_determinant(matrix): # calculate the determinant of the matrix
    if not is_square_matrix(matrix): # check if the matrix is square
        return None
    if len(matrix) == 1: # calculate the determinant of a 1x1 matrix
        return matrix[0][0]
    if len(matrix) == 2: # calculate the determinant of a 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    # for i in range(len(matrix)): # calculate the determinant with the laplace expansion
    #     det += matrix[0][i] * ma.pow(-1, i) * calc_determinant([row[:i] + row[i + 1:] for row in matrix[1:]])
    det = determinant(matrix) # calculate the determinant with the LU decomposition
    return det


def lu_decomposition(matrix): # perform the LU decomposition
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n): # Perform LU decomposition
        L[i][i] = 1.0
        for j in range(i, n): # calculate the L and U matrix
            sum_u = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = matrix[i][j] - sum_u
        for j in range(i + 1, n): # calculate the L matrix
            sum_l = sum(U[k][i] * L[j][k] for k in range(i))
            L[j][i] = (matrix[j][i] - sum_l) / U[i][i]

    return L, U


def determinant(matrix): # calculate the determinant of the matrix
    n = len(matrix)
    if n != len(matrix[0]):
        return None  # Matrix is not square

    # Perform LU decomposition
    L, U = lu_decomposition(matrix)

    # The determinant is the product of the diagonal elements of U
    det = 1.0
    for i in range(n):
        det *= U[i][i]

    return det


def generate_matrix(row, column): # generate a matrix with given row and column
    matrix = []
    for i in range(row):
        matrix.append([])
        for j in range(column):
            matrix[i].append(0) # initialize the matrix with zeros
    return matrix


def fill_matrix(matrix): # fill the matrix with random numbers
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = randint(0, 100000) # fill the matrix with random numbers
    return matrix


def cramerische_regel(matrix, loesung): # calculate the solution of the matrix with cramer's rule
    if not is_square_matrix(matrix): # check if the matrix is square
        return None
    if calc_determinant(matrix) == 0: # check if the determinant is zero
        return None
    result = []
    for i in range(len(matrix)): # calculate the solution with cramer's rule
        new_matrix = copy.deepcopy(matrix)
        for j in range(len(matrix)): # replace the column with the solution
            new_matrix[i][j] = loesung[j]
        result.append(calc_determinant(new_matrix) / calc_determinant(matrix)) # append the solution to the result
    return result

