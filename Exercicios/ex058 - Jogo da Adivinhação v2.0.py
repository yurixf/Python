from random import randint
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que voce consegue adivinhar qual foi?''')
num = int(input('Qual o seu palpite?'))
pc = randint(0, 10)
palpites = 1
while num !=pc:
    if num<pc:
        print('Mais, tente outra vez!!')
    else:
        print('Menos, tente outra vez!!')
    num = int(input('Qual o seu palpite?'))
    palpites += 1
print('Acertou com {} tentativas, Parabens!!'.format(palpites))


