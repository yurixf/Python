céd = 50
c = total = 0
saque = int(input('Deseja sacar quanto: R$'))
while True:
    if saque>céd:
        saque -=céd
        c +=1
    else:
        if c > 0:
            print(f'Total de {c} de {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        c = 0
        if c == 0:
            break
