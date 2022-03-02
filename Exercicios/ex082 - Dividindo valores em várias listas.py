valores = []
par = []
impar = []
while True:
    valores.append(int (input('Digite um valor:')))
    while True:
        c = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
        if c not in 'SN':
            print('Resosta invalida!')
        else:
            break
    if c == 'N':
        break
for v in valores:
    if v%2==0:
        par.append(v)
    else:
        impar.append(v)
print('-=-'*20)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de imparews é {impar}')