def leiaint (txt):
    while True:
        num = input(txt)
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print(f'\033[31mERRO! Digite um número inteiro valido!\033[m')

n = leiaint('Digite um número:')
print(f'Voce acabou de digitar o número {n}')
