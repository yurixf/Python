valores = []
while True:
    num = int(input('Digite um valor:'))
    if num in valores:
            print('Valor duplicado, não foi adicionado')
    else:
        valores.append(num)
    continuar = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
valores.sort()
print('-=-'*20)
print(f'Voce digitou os valores {valores}')
