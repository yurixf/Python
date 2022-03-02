salario = float(input('Informe o sálario do funcionario:R$'))
aumentop = float(input('Informe o percentual do aumento:'))
aumento = 1+(aumentop/100)
salarion = salario*aumento
print('Um funcionario que ganhava R${:.2f}, com aumento de {}%, passa a receber R${:.2f}'.format(salario, aumentop, salarion))
