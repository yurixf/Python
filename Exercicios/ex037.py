num = int(input('Digite um numero:'))
print('''Escolha uma das bases para conversão:
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} em BINARIO é {:b}'.format(num, num))
elif opção == 2:
    print('{} em OCTAL é {:o}'.format(num, num))
elif opção == 3:
    print('{} em HEXADECIMAL é {:x}'.format(num, num))
else:
    print('A opção escolhida não é validada')
