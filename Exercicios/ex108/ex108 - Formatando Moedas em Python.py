import moeda


preço = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando 5%, temos {moeda.moeda(moeda.aumentar(preço,5))}')
print(f'Diminuindo 5% temos {moeda.moeda(moeda.diminuir(preço,5))}')