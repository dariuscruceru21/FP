def rechteck_turt():
    import turtle
    t = turtle.Pen()
    t.forward(100)
    t.left(180)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.up()
    t.forward(100)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.down()
    t.forward(25)
    t.left(180)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.clear()
    turtle.done()



def hertz():
    import turtle
    t = turtle.Pen()
    t.pensize(3)
    t.left(50)
    t.forward(133)
    t.circle(50,200)
    t.right(140)
    t.circle(50,200)
    t.forward(133)
    t.clear()
    turtle.done()




def menu():
    return """
        1 - Rechteck
        2 - Hertz
        0 - exit
    """

def main():

    while True:
        print(menu())
        opt = int(input('opt = '))

        if opt == 1:
            rechteck_turt()
        if opt == 2:
            hertz()
        if opt == 0:
            break

main()
