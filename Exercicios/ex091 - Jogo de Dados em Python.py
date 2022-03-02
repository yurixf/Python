from random import randint
from time import sleep

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(0.5)
print('-=-' * 20)
print('RANKING DOS JOGADORES')
p = 1
while p < 4:
    for i in sorted(jogadores, key=jogadores.get, reverse=True):
        print(f'{p}º Lugar: {i} com {jogadores[i]}')
        p += 1
