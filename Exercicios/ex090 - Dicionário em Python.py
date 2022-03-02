aluno = {}
aluno['nome'] = str(input('Nome:')).strip().title()
aluno['media'] = float(input('Média:'))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Em Recuperação'
print('-=-' * 30)
for k, v in aluno.items():
    print(f'{k} é {v}')
