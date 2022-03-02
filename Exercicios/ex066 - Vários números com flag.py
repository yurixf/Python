soma = c = 0
while True:
    num = int(input('Digite um número:'))
    if num == 999:
        break
    c +=1
    soma +=num
print(f'A soma dos {c} valores foi {soma}')