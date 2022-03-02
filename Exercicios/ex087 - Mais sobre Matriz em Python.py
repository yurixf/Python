matriz = [[0, 0, 0, ], [0, 0, 0], [0, 0, 0]]
par = 0
c3 = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor para posição[{l}][{c}]'))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            c3 += matriz[l][c]
print('-=-'*20)
for c in range (3):
    for l in range (3):
        print(f'[{matriz[c][l]:^5}]',end='')
    print('')
print('-=-'*20)

print(f'A soma dos valores pares é {par}')
print(f'A soma dos  valores da terceira coluna é {c3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

