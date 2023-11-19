m = [[4, 3, 1],
     [1, 2, 1],
     [0, 5, 1]]

def ex2(m):
    a =[]
    for i in range(len(m)):
        sum = 0
        for j in range(len(m)):
            if i != j:
                sum += m[i][j]
        if sum == m[i][i]:
            a.append(True)
        else:
            a.append(False)
    print(a)

ex1(m)
