# Matheus Moreira - desenhe um triângulo de lado N.
import turtle

n = 100

def triangulo(n):
    for i in range(3):
        turtle.forward(n)
        turtle.left(120)
        
triangulo(n)