lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for c in range(0, len(lista),2):
    print(f'{lista[c]:.<30}R$ {lista[c+1]:>7.2f}')