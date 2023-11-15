from menu import *
from action_keys import deseneaza
from draw_auto import draw_automatic
def main():
   with open('keys_pressed.txt', 'a') as file:
       file.write("\n")
   while True:
        print(meniu())
        opt = int(input("Optiunea="))

        if opt == 1:
            draw_automatic()
        if opt == 2:
            deseneaza()
        if opt == 0:
            break

main()
