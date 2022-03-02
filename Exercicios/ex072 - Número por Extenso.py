números = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if num < 0 or num > 20:
            print('Valor INVALIDO, tente novamente. ', end='')
        else:
            break
    print(f'Voce digitou o numero {números[num]}')
    while True:
        continuar = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Opção Invalida')
    if continuar == 'N':
        break

