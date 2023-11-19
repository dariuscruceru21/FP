m = [[4, 5, 6],
     [1, 2, 3],
     [7, 8, 9]]

def verificare(m):
    for i in range(len(m)):
         if i  % 2 == 0:
             for j in range(len(m) - 1):
                 if m[i][j] > m[i][j + 1]:
                    return False
         if i % 2 != 0:
             for j in range(len(m) - 1 , 0, -1):
                 if m[i][j] > m[i][j - 1]:
                     return False

    return True

print(verificare(m))
