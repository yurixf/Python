import random
from time import sleep
n2 = random.randint(1,5)
print ('-=-'*20)
print('Vou pensar em um numero entre 1 e 5, tente adivinhar')
print('-=-'*20)
num = int(input('Em que numero eu pensei?'))
print('PROCESSANDO')
sleep(1)
if num == n2:
    print('Parábens, voce venceu!!')
else:
    print('GANHEI!! Eu pensei no numero {} e não no {}'.format(n2, num))