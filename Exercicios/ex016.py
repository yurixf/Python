import math

num = float(input('Informe um numero:'))
print('O numero informado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))  # opção 1
print('O numero informado foi {} e sua porção inteira é {}'.format(num, int(num)))  # opção 2
