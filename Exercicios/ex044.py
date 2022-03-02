print('{0} LOJAS GUANABARA {0}'.format('='*10))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à Vista dinheira
[ 2 ] à Vista Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão''')
opção = int(input('Qual a opção?'))
if opção == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, preço*0.9))
elif opção == 2:
    print('Sua compra de R${:.2f} va custar R${:.2f} no final'.format(preço, preço*0.95))
elif opção == 3:
    print('Sua compra foi de R${:.2f} foi feita em 2x e o valor da parcela será de R${:.2f}'.format(preço, preço/2))
elif opção == 4:
    parcelas = int(input('Quantidade de parcelas:'))
    nvalor = preço*1.2
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, nvalor/parcelas))
    print('Sua compra foi de R${:.2f} e ela vai custar R${:.2f}'.format(preço, nvalor))
else:
    print('Opção inválida')
