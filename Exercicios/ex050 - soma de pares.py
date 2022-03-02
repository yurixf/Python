total = 0
cont = 0
for c in range (1,7):
    num = int(input('Informe o {}º Número:'.format(c)))
    if num%2 == 0:
        total +=num
        cont +=1
print('Você informou {} números pares e a soma deles é {}'.format(cont, total))