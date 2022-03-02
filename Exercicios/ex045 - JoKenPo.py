import random, time
jokenpo = ['pedra', 'papel', 'tesoura']
vpc = 0
vjg = 0
emp = 0

partidas = int(input('Deseja jogar quantas partidas?'))

for c in range(0, partidas):
    pc = random.randint(0,2)
    print('''Suas opções:
    [ 0 ] - Pedra
    [ 1 ] - Papel
    [ 2 ] - Tesoura ''')
    escolha = int(input('Qual a sua jogada?'))
    time.sleep(0.2)
    if escolha<3:
        print('JO')
        time.sleep(0.4)
        print('KEN')
        time.sleep(0.4)
        print('PO!!')
        time.sleep(0.2)
        print('''{0}
    Jogador jogou {1} 
    Computador jogou {2}
{0}'''.format('-=-'*10,jokenpo[escolha], jokenpo[pc]))
        time.sleep(0.2)
        if pc == escolha:
            print('EMPATE')
            emp +=1
        elif pc == 0 and escolha == 1:
            print('Jogador GANHOU!')
            vjg +=1
        elif pc == 1 and escolha == 2:
            print('Jogador GANHOU!')
            vjg +=1
        elif pc == 2 and escolha == 0:
            print('Jogador GANHOU!')
            vjg +=1
        else:
            print('PC Ganhou')
            vpc +=1
    else:print('Escolha invalida!!')
    print('-=-'*10)
print(f'Voce ganhou {vjg} vez(es), eu ganhei {vpc} vez(es) e empatamos {emp} vez(es)')
