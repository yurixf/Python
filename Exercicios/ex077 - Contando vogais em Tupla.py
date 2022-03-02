lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'OTORRINOLARINGOLOGISTA')
for p in lista:
    print(f'Na palavra {p} temos:', end= ' ')
    for l in p:
        if l in 'AEIOU':
            print (l, end=' ')
    print(' ')

