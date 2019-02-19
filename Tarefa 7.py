# Matheus Moreira - desenhe uma série de quadrados um do lado do outro
import turtle

def quadradros():
    quadrado = 0

    while quadrado < 4:
        for count in range(4):
            turtle.forward(100)
            turtle.left(90)
        turtle.forward(100)
        quadrado += 1

quadradros()