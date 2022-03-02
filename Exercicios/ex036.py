casa = float(input('Valor da casa:R$'))
salario = float(input('Salário do comprador:R$'))
anos = int(input('Anos de financiamento:'))
meses = anos*12
prestação = casa / meses
teste = salario*0.3

print('Para pagar uma casa de R${:.2f} em {} anos a prestação vai ser de R${:.2f} por mes' .format(casa, anos, prestação))

if prestação > teste:
    print('Emprestimo NEGADO!!')
else:
    print('Emprestimo APROVADO, parabens')