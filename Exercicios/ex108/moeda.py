def aumentar (n=0,p=0):
    v = n*(1+p/100)
    return v


def diminuir (n=0,p=0):
    v = n*(1-p/100)
    return v


def dobro(n=0):
    v=n*2
    return v


def metade (n):
    v=n/2
    return v


def moeda (preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')
