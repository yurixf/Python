c50 = 0
c20 = 0
c10 = 0
c01 = 0
saldo = 0
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
saque = int(input('Qual valor quer sacar?'))
if saque >= 50:
    c50 = saque//50
    saque = saque%50
    print(f'Total de {c50} cédulas de R$50')
if saque >= 20:
    c20 = saque //20
    saque = saque %20
    print(f'Total de {c20} cedulas de R$20')
if saque >= 10:
    c10 = saque//10
    print(f'Total de {c10} cédulas de R$10')
    saque= saque%10
if saque>0:
    c01 = saque
    print(f'Total de {c01} cédulas de R$1')
#if saque >=1: