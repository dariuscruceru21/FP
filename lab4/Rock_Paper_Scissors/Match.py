def Match(utilizator, calculator):
    if utilizator == calculator:
        return 'Egalitate'
    elif (utilizator == 'Schere' and calculator == 'Papier') or (utilizator == 'Stein' and calculator == 'Schere') or (utilizator == 'Papier' and calculator == 'Stein'):#toate posibilitatiile in care utilizatorul castiga
        return 'Utilizatorul a castigat'
    else:
        return 'Calculatorul a castigat'
