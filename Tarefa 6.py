# Matheus Moreira -  desenhe os ângulos de um círculo
from turtle import*

for angle in range(0, 360, 15):
    setheading(angle)
    forward(150)
    write(str(angle)+ 'º')
    backward(150)