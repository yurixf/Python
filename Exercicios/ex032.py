import datetime

ano = int(input('Que ano quer analisar? (0 para o atual):'))

# Ano que vai ser analisado
if ano == 0:
    ano = datetime.date.today().year

print(ano)

#Verificando se é Bissexto
d10 = ano % 4
d100 = ano % 100
d400 = ano % 400

if d10 == 0 and d100 !=0 or d400 == 0:
    print('Bissexto')
else:
    print('Não é Bissexto')