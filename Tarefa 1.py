# Matheus Moreira - Retornar a soma de todos os números de 1 até N inclusive;
n = int(input("Digite um número: "))
inicio = 1
total = 0

while(inicio <= n):
    inicio += 2
    total = total + inicio

total = total - inicio
print("Total:", total)