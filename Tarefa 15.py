#Matheus Moreira - Esse código não funciona logo apontei aonde eu encontrei erros no mesmo

import turtle

def geraPontos(i):
 """ Gera pontos para quadrados de qualquer tamanho """                            #ESPAÇAMENTO ERRADO, ERRO DE COMPILAÇÃO
   return [(i, 0), (i, i), (0, i), (0, 0)]

def desenhaPoligono(inicio, pontos, corLinha="black", corRecheio="white"):
   turtle.pencolor(lineColour)                                                     # LINECOLOUR E FILLCOLOUR NAO ESTÃO DECLARADOS, ERRO DE COMPILAÇÃO
   turtle.fillcolor(fillColour)

   turtle.penup()

   turtle.goto(inicio)  

   turtle.pendown()
   turtle.begin_fill()

   x, y = start                                                                    # MÉTODO START NÃO ESTÁ DEFENIDO, ERRO DE LÓGICA/COMPILAÇÃO

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
   quadrado_maior = geraPontos(100)                                                 #OCORRERÁ ERRO AO CHAMAR ESSE MÉTODO
   desenhaPoligono((-200, 200), quadrado_maior, cor="green")

   # Triangulo
   triangulo = [(200, 0), (100, 100), (0, 0)]
   desenhaPoligono((100, -100), triangulo, cor="green")


def main():
   teste()
   turtle.done()

main()
