#Matheus Moreira

import turtle

def desenhaPoligono(inicio, pontos, corLinha="black", corRecheio="white"):
   turtle.pencolor(corLinha)                                                    
   turtle.fillcolor(corRecheio)

   turtle.penup()

   turtle.goto(inicio)  

   turtle.pendown()
   turtle.begin_fill()

   x, y = inicio                                                                    

   for ponto in pontos:  
       dx, dy = ponto
       turtle.goto(x + dx, y + dy)
   turtle.goto(inicio)  

   turtle.end_fill()
   turtle.penup()


def teste():
   # Primeiro quadrado
   quadrado = [(50, 0), (50, 50), (0, 50), (0, 0)]
   desenhaPoligono((200, 200), quadrado)

   # Segundo quadrado
   quadrado_maior = [(100, 0), (100, 100), (0, 100), (0, 0)]                                                 
   desenhaPoligono((-200, 200), quadrado_maior)

   # Triangulo
   triangulo = [(200, 0), (100, 100), (0, 0)]
   desenhaPoligono((100, -100), triangulo)
   
   # Circulo
   pen = turtle.Pen()
   pen.circle(100)


def main():
   teste()
   turtle.done()

main()

