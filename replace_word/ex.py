def Replace(filename, word, replacedword):
   with open(filename, 'r') as date:
       text = date.read()
       text1 = text.replace(word, replacedword)
       ct = text1.count(replacedword)
   with open(filename, 'w') as date:
       date.write(text1)

   if ct > 0:
       print(f"{word} s-a schimbat cu {replacedword} de {ct} ori")
   else:
       print("Nu s-a schimbat nimic")

def main():
    filename = 'datei.txt'
    word = 'ana'
    replacedword = 'ION'
    Replace(filename, word, replacedword)
main()
