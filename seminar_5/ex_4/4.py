def executa(filename):
    d = {}

    with open(filename, 'r') as file:
        for line in file: # reads every line
            words = line.strip().split()# splits the words in the line in a list
            max_lenght_perline = 0
            for word in words:# iterrates through the list of words from each line
                word_length = len(word)
                if word_length > max_lenght_perline:
                    max_lenght_perline = word_length

            d[word] = max_lenght_perline

    return d

def main():

    filename = 'date.in'
    print(executa('date.in'))

main()
