sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
#whilw sexo not in 'MmFf': - RESOLUÇÃO GUANABARA
    print('Dados inválidos!!')
    sexo= str(input('Informe seu sexo:')).strip().upper()
print('Sexo {} registrado!'.format(sexo))