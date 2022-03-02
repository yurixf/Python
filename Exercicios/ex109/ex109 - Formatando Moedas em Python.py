import moeda


preço = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço,True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço,True)}')
print(f'Aumentando 5%, temos {moeda.aumentar(preço,5,True)}')
print(f'Diminuindo 5% temos {moeda.diminuir(preço,5)}')