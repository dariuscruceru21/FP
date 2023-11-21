import random
def utilizator1():#utilizatorul introduce de la tastatura o posibilitate
    while True:
        utilizator = input("utilizator=").capitalize().strip()
        if utilizator in('Stein', 'Papier', 'Schere'):
            return utilizator
        else:
            print("Nu este bun")


def calculator1():#se asigneaza o valoare random la calculator dintre posibilitati
    l = ['Stein', 'Papier','Schere'] #posibilitatiile jocului
    calculator = random.choice(l)
    return calculator
