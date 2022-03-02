import random as r

lista_sorteado = []

def lotofacil():
    
    for i in range(1, 16):
        numero_sorteado = r.randrange(1, 26)
        while numero_sorteado in lista_sorteado:
            numero_sorteado = r.randrange(1, 26)
        if numero_sorteado not in lista_sorteado:
            lista_sorteado.append(numero_sorteado)
            lista_sorteado.sort()
    return lista_sorteado

for c in range(10):
    print(lotofacil())
