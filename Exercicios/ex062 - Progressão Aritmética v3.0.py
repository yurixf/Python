primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
c = 0
t = 10
while c < t:
    print(primeiro, end=' >> ')
    primeiro += razão
    c += 1
    if c == t:
        print('PAUSA')
        t2 = int(input('Quantos termos voce quer mostrar a mais?'))
        if t2>0:
            t+=t2
        else:
            t=t
print('Processo finalizado com {} termos mostrados'.format(t))