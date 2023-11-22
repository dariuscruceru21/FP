# # # def f(x=1, y):
# # #     return x+y
# # # print(f(3,2))
# #
# # # d = {0:[[3, 0], [8, 4]]}[0][1][0]
# # # print(d)
# #
# # # y = 1
# # # z = 1
# # # x = y == z
# # # print(x)
# #
# # # l = [1,2,3,4]
# # # l.insert(1,9)
# # # print(l)
# #
# # # d = {1:3, 2:5, 3:9}
# # # l  = [[1, 2, 3, 4],[4, 5, 1],[7, 8, 5, 1, 4]]
# # #
# # # for word in d:
# # #     print(d[word])
# #
# # # l = [11, 12, 13, 14 ,15]
# # #
# # # for i in range(len(l)):
# # #     print(i)
# #
# #
# # # m = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1]]
# # # ctline = 0
# # # for line in range(len(m)):
# # #         ctline += 1
# # # print(ctline)
# # procentdezero = 0.7 * 16
# # print(int(procentdezero))
# #
# #     latura1_2 = 0
# #     latura3_4 = 0
# #     for column in range(len(matrix)):
# #         if matrix[0][column] == 1 and matrix[len(matrix) - 1][column]:
# #             latura1_2 +=1
# #     for line in range(len(matrix) - 1):
# #         if matrix[line +1][0] ==1 and matrix[line + 1][len(matrix) - 1] == 1:
# #             latura3_4 +=1
# #
# import math
#
# p = math.ceil(3/3)
#
# def check_square(matrix):
#     # Finden Sie die Koordinaten aller mit 1 besetzten Zellen
#     ones_coordinates = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 1]
#
#     if not ones_coordinates:
#         # Es gibt keine mit 1 besetzten Zellen
#         return False
#
#     # Überprüfen, ob die Punkte ein Quadrat bilden
#     x_values = [x for x, y in ones_coordinates]
#     y_values = [y for x, y in ones_coordinates]
#
#     min_x, max_x = min(x_values), max(x_values)
#     min_y, max_y = min(y_values), max(y_values)
#
#     # Überprüfen, ob die Differenzen zwischen den maximalen und minimalen x- und y-Werten gleich sind
#     return (max_x - min_x) == (max_y - min_y)
#
#
# # Beispielaufruf
# matrix = [
#     [1, 0, 1],
#     [0, 1, 0],
#     [1, 1, 1]
# ]
#
# result = check_square(matrix)
# print(result)

# def can_form_square(matrix):
#     # Finden Sie die Koordinaten aller mit 1 besetzten Zellen
#     ones_coordinates = [(i, j) for i in range(len(matrix)) for j in range(len(matrix)) if matrix[i][j] == 1]
#     print(ones_coordinates)
#     if not ones_coordinates:
#         # Es gibt keine mit 1 besetzten Zellen
#         return False
#     if len(ones_coordinates) % 2 != 0:
#         return False
#     # Überprüfen, ob die Punkte ein Quadrat bilden
#     min_x, min_y = min(ones_coordinates)
#     print(min_x,min_y)
#     max_x, max_y = max(ones_coordinates)
#     print(max_x,max_y)
#
#     # Überprüfen, ob die Differenzen zwischen den maximalen und minimalen x- und y-Werten gleich sind
#     return (max_x - min_x + 1) == (max_y - min_y + 1)
#
#
# Beispielaufruf
matrix = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1]
]

# result = can_form_square(matrix)
# print(result)

l1 = []
l2 = []
for column in range(len(matrix)):
    if matrix[0][column] == 1 and matrix[len(matrix) - 1][column] == 1:
            l1.append(True)
    else:
            l1.append(False)
for row in range(len(matrix)):
    if matrix[row][0] == 1 and matrix[row][len(matrix) - 1] == 1:
        l2.append(True)
    else:
        l2.append(False)

print(l1,l2)
