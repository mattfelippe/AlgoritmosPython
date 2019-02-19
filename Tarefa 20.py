# Matheus Moreira - desenhe com a ferramenta turtle.
import turtle
lado = 1
n = int(input("Entre com um dado N: "))

def quadrado(lado):
    lineColour = "red"
    turtle.pencolor(lineColour)
    for i in range(n):
        turtle.forward(lado)
        turtle.left(90 + 2)
        lado += 2
        
quadrado(lado)


