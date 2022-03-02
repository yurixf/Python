def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print(f'\033[31mTivemos um problema com os valores informados\033[m')
        except (KeyboardInterrupt):
            print(f'\033[31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return num

def leiafloat(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mTivemos um problema com os valores informados\033[m')
        except (KeyboardInterrupt):
            print(f'\033[31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return num



n=leiaint('Digite um numero:')
f=leiafloat('Digite um valor real:')
print(f'Voce acabou de digitar o número {n}')
print(f'Voce acabou de digitar o número {f}')