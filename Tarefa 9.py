# Matheus Moreira - Faça uma função que desenhe o triângulo
import turtle

def triangulo():
    turtle.shape('turtle')
    for count in range(3):
        turtle.forward(100 + 100)
        turtle.left(120)

triangulo()