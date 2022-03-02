valores = tuple(int(input(f'Digite o {c+1}º valor:'))for c in range(5))
print(f'Voce digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} veze(s)')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados:', end=' ')
for c in valores:
    if c % 2 == 0:
        print(c, end= " ")