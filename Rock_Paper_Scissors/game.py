from Utilizator_si_caculator import utilizator1
from Utilizator_si_caculator import calculator1
from Match import Match

def jocul():
    me = 0
    pc = 0
    for i in range(3):
        utilizator = utilizator1()
        print(utilizator)
        calculator = calculator1()
        print(calculator)
        if Match(utilizator, calculator) == 'Utilizatorul a castigat':
            me += 1
            print("Utilizator  =", me)
            print("Calculator  =", pc)
        elif Match(utilizator, calculator) == 'Calculatorul a castigat':
            pc += 1
            print("Utilizator  =", me)
            print("Calculator  =", pc)
        else:
            me += 1
            pc += 1
            print("Utilizator  =", me)
            print("Calculator  =", pc)

    if me > pc:
        print('Utilizatorul a castigat')
        print('Utilizatorul a obtinut =', me)
        print('Calculator a obtinut =', pc)
    elif pc > me:
        print('Calculatorul a castigat')
        print('Utilizatorul a obtinut =', me)
        print('Calculator a obtinut =', pc)
    elif pc == me:
        print('Egalitate')
        print('Calculator a obtinut =', pc)
        print('Utilizatorul a obtinut =', me)

