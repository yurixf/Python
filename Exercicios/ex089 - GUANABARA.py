ficha = []
while True:
    nome = str(input('Nome: ')).title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1, nota2],media])
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('-'*30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>5}')
print('-'*30)
for i,v in enumerate(ficha):
    print(f'{i:<4}{v[0]:<10}{v[2]:>5.2f}')
while True:
    print('-'*25)
    escolha = int(input('Mostrar notas de qual aluno?[999 para sair]'))
    if escolha == 999:
        break
    if escolha <= len(ficha)-1:
        print(f'Notas de {ficha[escolha][0]} são {ficha[escolha][1]}')