# Matheus Moreira
import turtle

def quadrado():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
        
def triangulo():
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
        
def circulo():
    pen = turtle.Pen()
    pen.circle(100)


turtle.listen()

turtle.onkey(quadrado, 'q')
turtle.onkey(triangulo, 't')
turtle.onkey(circulo, 'c')


