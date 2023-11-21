def entfernen(l):#1 works
    result = []
    for i in l:
        if i not in result:
            result.append(i)
    print(result)
l = [12, 24, 48]
def symetriesch(l):#2
    count = 0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if (l[i] % 10 == l[j]//10) and (l[i]//10 == l[j] % 10):
                count += 1
    print(count)

def konkat(l):#3
    list1 = []
    for i in l:
        list1.append(i % 10)
        list1.append(i // 10)
    list1.sort(reverse=True)#sorteaza lista descrescator
    x = 0
    for i in list1:
        x = x*10+i
    print(x)

def domino_teilfolge(l):
    count = 0
    for i in range(len(l) - 1):
        if l[i] % 10 == l[i+1] //10:
            count += 1
    print(count + 1)

def crypt(l):
    cif = l[0]
    for i in range(1,len(l)):
        l[i] = l[i] + cif
    print(l)
def cmmdc(a, b):
    while b:
        a, b = b, a%b
    return a

def final_cmmdc(from_nr, to_nr,l):
    l = l[from_nr:to_nr+1]
    result = l[0]
    for i in range(1,len(l)):
        result = cmmdc(result, l[i])
    print(result)

def main():
    pass


#entfernen(l)
#symetriesch(l)
#konkat(l)
#domino_teilfolge(l)
#crypt(l)
#final_cmmdc(0, 3, l)

main()

