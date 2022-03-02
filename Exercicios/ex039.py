import datetime
ano = int(input('Ano de nascimento:'))
sexo = str(input('Informe M ou F:')).strip().upper()
atual = datetime.date.today().year
idade = atual - ano
anos_passados = idade - 18
alistamento = ano + 18
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if sexo == 'F':
    print('Mulheres não precisam se alistar')
elif idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTO!!')
elif idade > 18:
    print('Voce ja deveria ter se alistado a {} anos'.format(anos_passados))
    print('Seu alistamento foi em {}'.format(alistamento))
else: print('''Ainda faltam {} anos para o seu alistamento!
Seu alistamento será em {}'''.format(anos_passados*-1, alistamento))