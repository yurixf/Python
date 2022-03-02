pessoas = []
while True:
    individuo = {}
    individuo['nome']=str(input('Nome: ')).strip().title()
    while True:
        individuo['sexo']= str(input('Sexo[M/F]: ')).strip().upper()[0]
        if individuo['sexo'] in 'MF':
            break
        else:
            print('ERRO!! Digite M ou F')
    individuo['idade']= int(input('Idade: '))
    pessoas.append(individuo)
    while True:
        cont = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
        else:
            print('ERRO!! Responda S ou N')
    if cont == 'N':
        break

print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')

idadet=0

for c in range(len(pessoas)):
    idadet += pessoas[c]['idade']
media=idadet/len(pessoas)
print(f'B) A média de idades é de {media:.2f} anos')

print('C) As mulheres cadastradas foram:',end=' ')
for c in pessoas:
    if c['sexo'] == 'F':
        print( f'{c["nome"]}',end=' ')

print("")
print('Lista de pessoas que estão acima da média:')
for c in pessoas:
    if c['idade']>= media:
        print('    ', end='')
        for k,v in c.items():
            print(f'{k} = {v}', end=' ')
        print('')
        #print(f'nome = {c["nome"]}; sexo = {c["sexo"]}, idade = {c["idade"]}')