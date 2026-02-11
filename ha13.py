# Loo Pythoni Turtle-iga programm, mis palub kasutajal sisestada joonlaua pikkuse sentimeetrites kasutades numinput funktsiooni.

#     Seejärel joonistab programm ekraanile joonlaua, märkides iga sentimeetri kriipsu ja numbri.
#     Iga sentimeetri kriips peaks olema lühem ja iga viie sentimeetri tagant pikem, et eristada erinevaid mõõtmeid selgemalt.
#     Numbrid kirjutatakse vastavate pikemate kriipsude juurde, märkides sentimeetrite arvu alates joonlaua algusest.


import turtle
screen = turtle.Screen()
pikkus = screen.numinput("Pikkuse sisestamine", "Kui pikk peab olema?", default=20, minval=0, maxval=200)
turtle.speed(0)
pikk = 10
number = 0
for i in range(1,int(pikkus)):
    turtle.lt(90)
    turtle.fd(10+pikk)
    turtle.bk(10+pikk)
    turtle.rt(90)
    turtle.fd(20)
    if i%5==0:
        pikk = 10
    else:
        pikk = 0


turtle.penup()
turtle.goto(0,0)
turtle.lt(90)
turtle.fd(10+pikk+20)
turtle.rt(90)

for i in range(0,int(pikkus)):
    if i%5==0:
        turtle.write(number, font=("Arial", 8, "normal"))
    turtle.fd(20)
    number+=1















turtle.done()