from datetime import date
nascimento = int(input('Ano de mascimento:'))
idade = date.today().year - nascimento
print('O atleta tem {} anos'.format(idade))
if idade > 25:
    print('Classificação: MASTER')
elif idade >19:
    print('Classificação: SÊNIOR')
elif idade > 14:
    print('Classificação: JUNIOR')
elif idade > 9:
    print('Classificação: Infantil')
elif idade >= 5:
    print('Classificação Mirim')
else:
    print('Crianças abaixo de 5 anos não podem competir')