valores = []
while True:
    valores.append(int(input('Digite um valor:')))
    while True:
        continuar = str(input('Continuar?[S/N]')).strip().upper()[0]
        if continuar not in 'SN' or continuar == '':
            print('Opção Inválida')
        else:
            break
    if continuar == 'N':
        break
print(f'Voce digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescentes são {valores}')
if 5 not in valores:
    print('O valor 5 não faz parte da lista')
else:
    print('O valor 5 faz parte da lista')