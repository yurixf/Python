def comando(msg):
    from time import sleep
    while True:
        print(f'\033[97;42m{"~" * 26} \n SISTEMA DE AJUDA PyHELP\n{"~" * 26}')
        print('\033[m')
        função = input(msg).lower().strip()
        if função == 'fim':
            break
        print(
            f'\033[97;47m{"~" * (29 + len(função) + 4)}\n ACESSANDO O MANUAL DO COMANDO {função}\n{"~" * (29 + len(função) + 4)}')
        sleep(1)
        print('\033[107;30m')
        help(função)
        sleep(1)


comando('Função ou Biblioteca:')
