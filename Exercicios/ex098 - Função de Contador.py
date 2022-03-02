from time import sleep


def contador(i, f, p):
    print('-=-'*30)
    sleep(1)
    if p < 0:
        p *=-1
    if p == 0:
        p =1
    print(f'Contagem de {i} até {f} com passo de {p}')
    while True:
        print(i, end=" ",flush=True)
        if i > f:
            i -= p
            if i<f:
                break
        else:
            i += p
            if i > f:
                break
        sleep(.3)
    print('')


contador(1, 10, 1)
contador(10, 2, 2)
print('Informe os valores para contagem:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
