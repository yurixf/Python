mulheres = homens = maiores = 0

while True:
    print('='*20)
    print('CADASTRO DE PESSOAS')
    print('='*20)
    sexo = ' '
    idade = int(input('Idade:'))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]')).strip().upper()[0]
    if idade > 18:
        maiores +=1
    if sexo == 'M':
        homens +=1
    if sexo == 'F' and idade<20:
        mulheres +=1
    print('-'*20)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('='*20)
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Total de homens cadastrados {homens}')
print(f'Temos {mulheres} mulher(es) com menos de 20 anos')