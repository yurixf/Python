def aumentar (n=0,p=0,f=False):
    v = n*(1+p/100)
    if f:
        v=moeda(v)
        return v
    else:
        return v


def diminuir (n=0,p=0,f=False):
    v = n*(1-p/100)
    if f:
        v=moeda(v)
        return v
    else:
        return v


def dobro(n=0,f=False):
    v=n*2
    if f:
        v=moeda(v)
        return v
    else:
        return v


def metade (n, f=False):
    v=n/2
    if f:
        v=moeda(v)
        return v
    else:
        return v


def moeda (preço=0, moeda='R$'):
    return f'{moeda:>2}{preço:>.2f}'.replace('.',',')

def resumo (preço=0, a=0,r=0):
    print(f'-'*25)
    print(f'{"RESUMO DO VALOR".center(25)}')
    print(f'{"-"*25}')
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'{a}% de aumento: \t{aumentar(preço,a,True)}')
    print(f'{r}% de redução: \t{diminuir(preço,r,True)}')
    print(f'{"-"*25}')