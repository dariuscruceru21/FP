def chenar_matrice(matrix):
    s = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix) - 1:
                if matrix[i][j] != 1:
                    return False
    return True


def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            l = []
            for elem in line.strip().split(','):
                l.append(int(elem))
            matrix.append(l)

    return matrix

def main():

    if chenar_matrice(read_matrix('input.txt')) == False:
        print('da')
    else:
        print('nu')

main()
