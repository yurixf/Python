from random import randint
from time import sleep

def sortear(lista):
    print('Sorteando 5 valores da lista:',end=' ')
    for c in range(0,5):
        n=randint(1,10)
        lista.append(n)
        print(n,end=' ')
        sleep(0.5)
    print('PRONTO!')

def par(lista):
    soma =0
    for n in lista:
        if n % 2==0:
            soma +=n
    print(f'Somando os valores pares de {lista  } temos {soma}')


numeros = list()
sortear(numeros)
par(numeros)
