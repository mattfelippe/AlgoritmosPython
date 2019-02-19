# Matheus Moreira - verifique se o elemento existe na tupla e retorne o indice do mesmo
tupla = ('1', '2', '3', '4')
numero = input("Digite um número de 1 a 4: ")

cont = 0
numero_encontrado = False

for n in tupla:
    if numero == n:
        print("Número, ", n , " no índice: ", cont)
        numero_encontrado = True
    cont += 1
if numero_encontrado == False:
    print("Não possui registro!")