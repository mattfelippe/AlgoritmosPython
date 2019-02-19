# Matheus Moreira - Informar um número e retornar o fatorial com while

n = int(input('Digite um número: '))
contador = n
fatorial = 1

print('Calculando {}! = '.format(n), end='')

while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador = contador - 1
print('{}'.format(fatorial))