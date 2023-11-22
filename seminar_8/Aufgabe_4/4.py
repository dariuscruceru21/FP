import math
def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            l = []
            for elem in line.strip().split(','):
                l.append(int(elem))
            matrix.append(l)

    return matrix


def is_sparse(matrix):
    ct1 = 0
    ct0 = 0
    ctline = 0
    for line in range(len(matrix)):
        ctline += 1
        for row in range(len(matrix)):
            if matrix[line][row] == 0:
                ct0 += 1
            elif matrix[line][row] == 1:
                ct1 += 1
    elemtotal = ctline * len(matrix)
    procent = 0.7 * elemtotal
    if ct1 + ct0 == ctline * len(matrix):
        if math.ceil(procent) == ct0:
            return True
        else:
            return False

def is_square(matrix):
    n = len(matrix)
    # Iterate through each element in the matrix
    for i in range(n):
        for j in range(len(matrix[i])):
            # Check if there is enough space for a square starting at (i, j)
            if i + 1 < n and j + 1 < len(matrix[i]):
                # Check if a square exists starting at (i, j)
                if (matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1] == 1):
                    return True
    flag = 0
    for column in range(n):
        for row in range(n):
            if matrix[0][column] == 1 and matrix[len(matrix) - 1][column] == 1 and matrix[row][0] == 1 and matrix[row][len(matrix) - 1] == 1:
                flag = 1
            else:
                flag = 0
    if flag == 1:
        return True

    return False

print(is_square(read_matrix('input.txt')))


