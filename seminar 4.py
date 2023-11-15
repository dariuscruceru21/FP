# 1/2 operati pe fracti
from math import gcd

def simplify(a):
    d = gcd(a[0], a[1])

    return a[0]//d, a[1]//d
def add (a, b):
    return simplify((a[0] * b[1] + a[1]*b[0], a[1]*b[1]))

def sub(a, b):
    return simplify((a[0] * b[1] - a[1]*b[0], a[1]*b[1]))

def add_frac(fracs, frac):
    fracs.append(frac)

def multiply(a, b):
    return simplify((a[0]*b[0], a[1]*b[1]))

def division(a, b):
    return simplify((a[0]*b[1], a[1]*b[0]))

def stergere(l, poz):
    l.pop(poz)

def max(l):
    max =(-1, -1)
    max1 = -1
    for frac in range(len(l)):
       if  l[frac][0] / l[frac][1] > max1:
           max1 = l[frac][0] / l[frac][1]
           max = l[frac]
    return max

def min(l):
    min =(999, 999)
    min1 = 999
    for frac in range(len(l)):
       if  l[frac][0] / l[frac][1] < min1:
           min1 = l[frac][0] / l[frac][1]
           min = l[frac]
    return min



def sum_frac(fracs):
    sum = 0, 1

    for frac in fracs:
        sum = add(sum, frac)

    return sum

def test_add():
    assert add( (1, 2),  (2, 3)) == (7, 6)
    assert add( (1, 2),  (1, 2)) ==  (1, 1)

def test_sum_frac():
    assert sum_frac([(1, 2), (2, 3), (1, 2)]) == (5, 3)
    assert sum_frac([(1, 2), (1, 2)]) == (1, 1)



def menu():
    return """
        1 - add frac
        2 - sum frac
        3 - stergere frac
        4 - max
        5 - min
        0 - exit
    """
def main():
    fracs = []

    while True :
        print(menu())
        opt = int(input('opt='))

        if opt == 1:
            n = int(input('n='))
            m = int(input('m='))
            add_frac(fracs, (n,m))
        if opt == 2:
            s = sum_frac(fracs)
            print(s)
        if opt == 3:
            poz = int(input('poz='))
            stergere(fracs, poz)
        if opt == 4:
           print(max(fracs))
        if opt == 5:
            print(min(fracs))
        if opt == 0:
            break

#print(max(l))
# test_add()
# test_sum_frac()
main()
