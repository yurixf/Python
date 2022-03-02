maior = ''
menor = ''
continuar = 's'
total = c = 0
while continuar == 's':
    if continuar != 's' and continuar != 'n':
        print('Opção inválida')
    else:
        num = int(input('Digite um número:'))
        c += 1
        total += num
        if maior == '':
            maior = num
        elif num > maior:
            maior = num
        if menor == '':
            menor = num
        elif num < menor:
            menor = num
    continuar = str(input('Quer continuar[s/n]?')).lower().strip()[0]
print('Voce digitou {} números e a média foi {}'.format(c, total / c))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
