# Matheus Moreira - desenhe um quadrado de n N
import turtle

n = 100

def quadrado(n):
    for i in range(4):
        turtle.forward(n)
        turtle.left(90)

quadrado(n)