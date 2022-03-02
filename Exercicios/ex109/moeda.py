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
    return f'{moeda}{preço:>.2f}'.replace('.',',')
