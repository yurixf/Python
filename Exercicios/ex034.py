salario = float(input('Salário:R$'))
if salario > 1250:
    nsalario = salario*1.1
else:
    nsalario = salario*1.15
print('Quem ganhava {:.2f}, passa a ganhar {:.2f}'.format(salario, nsalario))