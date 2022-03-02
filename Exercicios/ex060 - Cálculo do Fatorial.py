import math
f = int(input('Digite um numero para calcular o fatorial:'))
fatorial = math.factorial(f)
print('Calculando {0}! = {0}'.format(f), end=' x ')
while f !=1:
    f -=1
    if f>1:
        print(f, end=' x ')
    else:
        print(f, end=' = ')
print(fatorial)
print('fim')
