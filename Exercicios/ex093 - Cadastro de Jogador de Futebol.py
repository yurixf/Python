jogador = {}
jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
temp = []
total = 0
for c in range(partidas):
    gol = int(input(f'Quantos gols na {c + 1}ª partida? '))
    total += gol
    temp.append(gol)
jogador['gols'] = temp[:]
jogador['total'] = total
print('-=-'*25)
print(jogador)
print('-=-'*25)
for v,k in jogador.items():
    print(f'O campo {v} tem o valor {k}')
print('-=-'*25)
print(f'O jogador {jogador["nome"]} jogou um total de {partidas} partidas')
for c,g in enumerate(jogador['gols']):
    print(f'  =>Na {c+1}ª partida fez {g} gols')
print(f'Foi um total de {jogador[total]} gols')
