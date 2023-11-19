def perfekt_zahl(x):
    sum = 0
    for i in range(2, x):
        if x % i == 0:
            sum += i
    if sum + 1 == x:
        return True
    else:
        return False

def main():
 m = [[4, 3, 10],
     [1, 2, 10],
     [1, 1, 8]]

 for i in range(len(m)):
     sum = 0
     for j in range(len(m)):
        sum += m[j][i]
     if perfekt_zahl(sum) == False:
         return False

 return True
print(main())
