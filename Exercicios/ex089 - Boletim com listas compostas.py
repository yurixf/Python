alunos = []
temp = []
while True:
    notas = [0, 0]
    nome = str(input('Nome: ')).strip().title()
    notas[0] = float(input('Nota 1:'))
    notas[1] = float(input('Nota 2:'))
    temp.append(nome)
    temp.append(notas[:])
    alunos.append(temp[:])
    temp = []
    continuar = str(input('Deseja Continuar?[S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 30)
print(f'{"N":<2} {"Nome":^10} {"Média":>}')
print('-' * 30)
for i, n in enumerate(alunos):
    print(f'{i:<2} {n[0]:^10} {(alunos[i][1][0] + alunos[i][1][1]) / 2:>2.2f}')
print('-' * 30)

while True:
    indvidual = int(input('Mostrar as notas de qual aluno?[999 interrompe]'))
    if indvidual == 999:
        break
    if indvidual<=len(alunos)-1:
        print(f'As notas de {alunos[indvidual][0]} são {alunos[indvidual][1]}')
        print('-' * 30)
