from time import sleep

c = {'sem cor': '\033[m',
     'vermelho':'\033[0;30;41m',
     'verde':'\033[0;30;42m',
     'amarelo':'\033[0;30;43m',
     'azul':'\033[0;30;44m',
     'roxo':'\033[0;30;45m',
     'branco':'\033[107;30m'
     }


def ajuda(com):
    titulo (f'Acessando o manual do comando \'{com}\'',c['azul'])
    print(c['branco'], end='')
    help(com)
    print(c['sem cor'],end='')
    sleep(2)


def titulo(msg, cor=c['sem cor']):
    tam=len(msg)+4
    print(cor,end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c['sem cor'],end='')
    sleep(1)


#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP',c['verde'])
    comando = str(input('Função ou Biblioteca:')).lower().strip()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('Até Logo',c['vermelho'])