nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1+nota2)/2
print('Tirando {} e {}, a media do aluno é {}'.format(nota1, nota2, media))
if media>=6:
    print('Aluno APROVADO')
elif media<5:
    print('Aluno REPROVADO')
else:
    print('Aluno em RECUPERAÇÃO')