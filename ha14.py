import turtle
ekraan = turtle.Screen()
turtle.speed(0)

# valik = ekraan.numinput("Vali kujund", "1: ruut\n2: ring", default=1, minval=1, maxval=2)
def muuda_punane():
    turtle.color("red")
def muuda_roheline():
    turtle.color("green")
def muuda_sinine():
    turtle.color("blue")

ekraan.onkey(muuda_punane, "r")
ekraan.onkey(muuda_roheline, "g")
ekraan.onkey(muuda_sinine, "b")


def vasakKlikk(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(4):
        turtle.fd(100)
        turtle.lt(90)
    
def paremKlikk(x, y):
    for _ in range(8):
        turtle.undo()

ekraan.onscreenclick(vasakKlikk, 1) # Vasak klõps
ekraan.onscreenclick(paremKlikk, 3) # Parem klõps

ekraan.listen()
turtle.mainloop()

