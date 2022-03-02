from random import randint

lista = []
jogos = []

quantidade = int(input('Quantos Jogos?'))

tot = 1

while tot <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista = []
    tot += 1
for j, n in enumerate(jogos):
    print(f'Jogo {j + 1}: {n}')
