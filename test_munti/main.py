def reee(filename):
    with open(filename,'r') as file:
        for line in file:
            for elem in line:
                elem = elem[::-1]
        c = len(file)

    return c

print(reee('output.txt'))
