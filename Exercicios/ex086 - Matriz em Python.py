matriz = [[],[],[]]
for l in range (3):
    for c in range (3):
        matriz[l].append(int(input(f'Digite o valor para [{l}][{c}]: ')))
for v in range(3):
    for p in range(3):
        print(f'[{matriz[v][p]:^5}]', end=' ')
    print('')