maior = ''
menor = ''
for c in range (1,6):
    p = float(input('Informe o peso da {}ª pessoa:'.format(c)))
    if maior == '':
        maior = p
    else:
        if p > maior:
            maior = p
    if menor == '':
        menor=p
    else:
        if p < menor:
            menor=p
print('O maior peso lido foi de {:.2f} kg'.format(maior))
print('O menor peso lido foi de {:.2f} kg'.format(menor))
