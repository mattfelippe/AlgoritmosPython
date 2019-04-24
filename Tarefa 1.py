#Tarefa 1 Matheus Moreira - Leia uma tupla contendo 3 números inteiros, (n1, n2, n3) e os imprima em ordem crescente.

numero1 = int(input('Digite o primeiro número : '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

tupla = (numero1, numero2, numero3)
tupla_na_ordem_crescente = sorted(tupla)

print('Tupla normal: ',tupla)
print('')
print('Tupla na ordem crescente: ',tupla_na_ordem_crescente)