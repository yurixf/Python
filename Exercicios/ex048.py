total = 0
contador = 0
for c in range (0, 501, 3):
    if c%2 == 1:
        total += c
        contador +=1
print('A soma de todos os {} valores solicitados é {}'.format(contador, total))
