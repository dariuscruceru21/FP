from litere_desenate import *
def draw_automatic():
    sterge()
    word = input("Enter your word=")
    for letter in word:
        al[letter]()


