# 0,0,0,0,0,0
# 0,1,1,1,0,0
# 0,1,0,1,0,0
# 0,1,1,1,0,0
# 0,0,0,0,0,0
# 0,0,0,0,0,0


def matrix_square(matrix):
    ct_elem_1 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                ct_elem_1 += 1

    return ct_elem_1


