velocidade = int(input('Velocidade do carro:'))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print('MULTADO!! Voce excedeu o limite permitido de 80 km/h')
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia!! Dirija com segurança!!')