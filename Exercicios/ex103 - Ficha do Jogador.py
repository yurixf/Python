def ficha(nome='<desconhecido>', gols=0):
    if nome=='':
        nome= '<desconhecido>'
    return f'O jogador {nome}, fez {gols} gols'


n = str(input('Nome do Jogador:')).strip()
g = str(input('Numero de gols:'))
if g.isnumeric():
    g=int(g)
else:
    g=0


print(ficha(n,g))

