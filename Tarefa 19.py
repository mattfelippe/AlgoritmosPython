# Matheus Moreira - desenhe com a ferramenta turtle.
import turtle
lado = 1
n = int(input("Entre com um dado N: "))

def quadrado(lado):
    lineColour = "blue"
    turtle.pencolor(lineColour)
    for i in range(n):
        turtle.forward(lado)
        turtle.left(90)
        lado += 1
        
quadrado(lado)

