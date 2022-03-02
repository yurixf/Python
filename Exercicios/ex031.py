distancia = float(input('Qual é a distancia da viagem?'))
print('Voce vai começar uma vagem de {:.2f} km'.format(distancia))
if distancia > 200:
    preço = distancia*0.45
else:
    preço = distancia*0.5
print('O preço da sua passagem será R${:.2f}'.format(preço))