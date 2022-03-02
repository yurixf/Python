soma = 0
velho = ""
nvelho = ""
mulher = 0
for c in range(1, 5):
    print('{0} {1}ª pessoa {0}'.format('-' * 5, c))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper().strip()
    soma += idade
    if sexo == 'M':
        if velho == '':
            velho = idade
            nvelho = nome
        elif velho < idade:
            velho = idade
            nvelho = nome
    else:
        if idade < 20:
            mulher += 1
media = soma / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))
