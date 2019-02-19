# Matheus Moreira - Informe um número e retorne o fatorial
n = int(input('Digite um número: '))

contador = n
fatorial = 1

print('Calculando {}! = '.format(n), end='')

for count in range(contador):
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador = contador - 1
print('{}'.format(fatorial))