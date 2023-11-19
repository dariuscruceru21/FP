def palindrom(value):
    return value == value[::-1 ]

def countpalindrom(filename):
    pal_dict = {}

    with open(filename, 'r') as file:
        for line in file:
            val = line.strip().split()
            for cf in val:
                if palindrom(cf):
                    if cf in pal_dict:
                        pal_dict[cf] += 1
                    else:
                        pal_dict[cf] = 1

    return pal_dict

def main():

    filename = 'datei.txt'
    dicti = countpalindrom(filename)

    print(dicti)

main()
