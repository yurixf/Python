lista = []
for c in range (0,5):
    lista.append(int(input(f'Digite o valor para a posição {c}:')))
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado é o {max(lista)} e ele aparece nas posições:', end= ' ')
for v, n in enumerate(lista):
    if n == max(lista):
        print(f'{v}...',end='')
print(f'\nO menor valor digitado é o {min(lista)} e ele aparece nas posições:', end=' ')
for v, n in enumerate(lista):
    if n == min(lista):
        print(f'{v}...',end='')