# Matheus Moreira - desenhe um polígono de lado N composto somente por triângulos.
import turtle

lado = float(input("Digite o lado N: "))

def triangulo(lado):
    angulo = 120
    for i in range(6):
        for i in range(3):
            turtle.lt(angulo)
            turtle.fd(lado)
        
        turtle.lt(60)
        turtle.fd(lado)
    
triangulo(lado)