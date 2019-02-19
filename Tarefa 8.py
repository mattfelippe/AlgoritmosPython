# Matheus Moreira - receba três valores e verifique se esses valores podem ser os comprimentos dos lados de um triângulo
tuplas = ()
x = input("Entre com o 1° lados do triângulo: ")
y = input("Entre com o 2° lados do triângulo: ")
z = input("Entre com o 3° lados do triângulo: ")

tuplas = (x, y, z)

if((x == y) and (x == z) and (y == z)):
    print("Essas medidas são de um Triângulo Equilátero!")
    
if((x == y) and (x != z)):
    print("Essas medidas são de um Triângulo Isósceles!")
    
if((x == z) and (y != z)):
    print("Essas medidas são de um Triângulo Isósceles!")
    
if((y == z) and (y != x)):
    print("Essas medidas são de um Triângulo Isósceles!")
    
if((x != y) and (x != z) and (y != z)):
    print("Essas medidas são de um Triângulo Escaleno!")