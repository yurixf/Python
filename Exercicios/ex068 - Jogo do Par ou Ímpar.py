from random import randint
vj = 0
print('-=-'*9)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-'*9)
while True:
    pc = randint(0, 10)
    num = int(input('Diga um valor:'))
    escolha = str(input('Par ou Impar [P/I]:')).strip().upper()[0]
    print('-'*15)
    if escolha == 'P' or escolha =='I':
        print(f'Voce jogou {num} e eu joguei {pc}. Total {num + pc},', end=' ')
        teste = (pc + num) % 2
        if teste == 0:
            print('DEU PAR')
            if escolha == 'P':
                print('Voce Ganhou')
                vj +=1
            else:
                break
        elif teste == 1:
            print('DEU IMPAR')
            if escolha == 'I':
                print('Voce ganhou')
                vj +=1
            else:
                break
        print('-'*15)
        print('Vamos Jogar novamentw')
    else:
        print('Escolha inválida!!')
print('-'*10)
print('Voce Perdeu')
print(f'GAME OVER!!! Voce venceu {vj} vezes')