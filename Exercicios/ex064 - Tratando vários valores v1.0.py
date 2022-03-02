n=0
c=0
soma = 0
while n != 999:
    n=int(input('Digite um número [999 para parar]:'))
    if n != 999:
        soma +=n
        c+=1
print('Voce digitou {} e a soma entre eles foi {}'.format(c,soma))
