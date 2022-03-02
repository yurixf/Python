pessoas = []
add = []
maior = menor = ''
while True:
    add.append(str(input('Nome: ')).strip().title())
    add.append(float(input('Peso: ')))
    pessoas.append(add[:])
    add = []
    while True:
        c = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
        if c not in 'SN':
            print('Opção Invãlida')
        else:
            break
    if c == 'N':
        break
for p in pessoas:
    if maior == menor == '':
        maior = p[1]
        menor = p[1]
    else:
        if maior<p[1]:
            maior = p[1]
        if menor>p[1]:
            menor = p[1]
print('-=-'*20)
print(f'Ao todo voce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior:.2f}kg. Peso de ', end='')
for kg in pessoas:
    if kg[1] == maior:
        print(kg[0], end= ' ')
print(f'\nO menor peso foi de {menor:.2f}kg. Peso de ',end='')
for kg in pessoas:
    if kg[1] == menor:
        print(kg[0],end=' ')
