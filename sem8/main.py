
#
# def common_elements(list):
#     dict = {}
#     newList = []
#     for ind1 in range(len(list)):
#         for ind2 in range(len(list[ind1])):
#             if list[ind1][ind2] in dict:
#                 dict[list[ind1][ind2]] += 1
#             else:
#                 dict[list[ind1][ind2]] = 1
#     print(dict)
#
#     for index, val in dict.items():
#         for elem in list:
#             value = elem.count(index) - 1
#
#         if value > 0:
#             val -= value
#
#         if val == len(list):
#             newList.append(index)
#
#     return newList


# def read_matrix(filename):
#     file = open(filename, 'r')
#     matrix = [[int(el) for el in line.strip().split(',')] for line in file]
#     file.close()
#
#     return matrix
#
#
# def is_sparse(matrix):
#     ct1 = sum([sum(line) for line in matrix])
#     ct0 = len(matrix) ** 2 - ct1
#
#     return ct0 > 0.7 * len(matrix) ** 2
#
#

# 0,0,0,0,0
# 0,1,1,1,0
# 0,1,0,1,0                a-este marginea de sus
# 0,1,1,1,0                b-este marginea de jos
# 0,0,0,0,0                c- este marginea din stanga
#                          d- este marginea din dreapta
def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            l = []
            for elem in line.strip().split(','):
                l.append(int(elem))
            matrix.append(l)

    return matrix

# b si d nu e bine


def is_square(matrix):
    ct1 = sum([sum(line) for line in matrix])#numarul elem de 1 din matrice

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                a = 1#contor marginea de sus
                q = j #retinem coloana sa o putem verifica
                while matrix[i][q] == 1 and q < len(matrix) - 1:
                      q += 1  #pentru caz de mai sus q = 3 si a = 4
                      a += 1
                c = 1#marginea din stanga
                w = i #retinem linia sa o putem verifica
                while matrix[w][j] == 1 and w < len(matrix) - 1:
                      w += 1 #pentru caz de mai sus w = 3 si c = 3
                      c += 1
                d = 1#marginea din dreapta
                r = q   #locul de unde pornim si ramane coloana
                t = i# sa nu stricam linia
                while matrix[t][r] == 1 and t < len(matrix) - 1:
                    t += 1
                    d += 1
                b = 1#marginea de jos
                y = w  #locul de unde pornim si ramane linia aceiasi
                u = j#sa nu stricam j
                while matrix[y][u] == 1 and u <len(matrix) - 1:
                    u += 1
                    b += 1
                #suma_margini = (a + b + c + d) - 4#minus 4 pentru ca am enumerat de doua ori colturile
                if (a + b + c + d) - 4 == ct1:
                    return True
    return False



def main():
    print(is_square(read_matrix('input.txt')))


# def test():
#     assert do_stuff([2, 4, 7, 9]) == [True, True, True, True]
#     assert do_stuff([2, 4, 7, 9]) == [True, True, False, False]


main()
