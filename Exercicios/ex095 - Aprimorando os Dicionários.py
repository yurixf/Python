time = []
while True:
    total = 0
    temp = []
    jogador = {}
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input('Quantidade de Partidas: '))
    for c in range(jogador['partidas']):
        gol = int(input(f'Quantos gols na {c + 1}ª partida: '))
        total += gol
        temp.append(gol)
    jogador['gols'] = temp.copy()
    jogador['total'] = total
    time.append(jogador)
    while True:
        resp = str(input('Deeja continuar?[S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Responda S ou N')
    if resp == 'N':
        break
print('-=-' * 30)
# print(f'{"Cod":<5}{"Nome":<10}{"Gols":>5}{"Total":>15}')
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<10}', end=' ')
print()
print('-' * 45)
for i, v in enumerate(time):
    # print(f'{i:<5}{v["nome"]:<10}{v["gols"]!s:<10}{v["total"]:>10}')
    print(f'{i:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<10}', end=' ')
    print('')
print('-' * 45)
while True:
    dados = int(input('Mostrar dados de qual jogador? [999 - sair] '))
    if dados == 999:
        break
    elif dados > len(time):
        print('Opção invalida! Escolha um valor da lista acima')
    else:
        print(f'--- LEVANTAMENTO DE DADOS DO JOGADOR {time[dados]["nome"]} ---')
        for c, g in enumerate(time[dados]["gols"]):
            print(f'No jogo {c + 1} fez {g} gols')
