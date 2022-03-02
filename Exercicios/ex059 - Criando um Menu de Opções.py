from time import sleep
n1 = int(input('1º Valor:'))
n2 = int(input('2º Valor:'))
nm =[n1,n2]
opção = 0
while opção !=5:
    print('''    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos números
    [ 5 ] - Sair ''')
    opção = int(input('{} Qual sua opção?'.format('>' * 5)))
    if opção==1:
        print('A soma entre entre {} e {} é {}'.format(n1, n2, n1+n2))
    elif opção == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1*n2))
    elif opção == 3:
        print('O maior valor entre {} e {} é {}'.format(n1,n2,max(nm)))
    elif opção == 4:
        n1 = int(input('1º Valor:'))
        n2 = int(input('2º Valor:'))
        nm = [n1,n2]
    else:
        print('Opção invalida, escolha outro numero')
    print('-=-'*10)
    sleep(1)
print('fim')