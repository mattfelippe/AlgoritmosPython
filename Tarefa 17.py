# Matheus Moreira -  “aeiou” -> “ouaei”
palavra = str(input("Digite uma palavra: "))
numero = int(input("Digite um número: "))

n = numero

tamanho = len(palavra)

divide_palavra = list(palavra)

diferenca = tamanho - numero

agrupar_final = (divide_palavra[numero-1])

for i in range(diferenca):
    agrupar_final += (divide_palavra[numero])
    numero += 1
    
n = n - 1

for i in range(n):
    agrupar_final += (divide_palavra[i])


print("Sua palavra é: ", palavra)
print ("Sua palavra rotacionada é :", agrupar_final)

