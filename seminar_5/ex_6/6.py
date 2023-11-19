def palindrom(word):
    return word == word[::-1]

def lucru(filename, filename1):

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if palindrom(word):
                    with open(filename1,'a') as file1:
                        file1.write(word)
                        file1.write("\n")

    file.close()
    file1.close()

def main():

    filename = 'in.txt'
    filename1 = 'out.txt'

    lucru(filename, filename1)

main()
