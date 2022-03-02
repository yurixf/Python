from time import sleep
import ex115.lib.arquivo

c = {'sem cor': '\033[m',
     'vermelho': '\033[0;31m',
     'verde': '\033[32m',
     'amarelo': '\033[0;33m',
     'azul': '\033[0;34m',
     'roxo': '\033[0;30;45m',
     'branco': '\033[107;30m'
     }


def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print(f'\033[31mTivemos um problema com os valores informados\033[m')
        except (KeyboardInterrupt):
            print(f'\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 3
        else:
            return num

def linha(tam=40):
    print('-' * tam)


def menu():

    cabeçalho("MENU PRINCIPAL")

    print(f'{c["amarelo"]}1 - {c["azul"]}Ver as pessoas cadastradas')
    print(f'{c["amarelo"]}2 - {c["azul"]}Cadastrar novas pessoas')
    print(f'{c["amarelo"]}3 - {c["azul"]}Sair{c["sem cor"]}')
    linha()


def cabeçalho(txt):
    linha()
    print(txt.center(40),c['sem cor'])
    linha()


def lista (txt):
    #cabeçalho('Lista de Cadastros')
    ex115.lib.arquivo.lerArquivo(txt)
    sleep(1)

def cadastro(txt):
    cabeçalho('CADASTRO DE PESSOAS')
    nome=str(input('Nome: ')).strip().title()
    idade=leiaint('Idade: ')
    ex115.lib.arquivo.cadastro(txt,nome,idade)
    sleep(1)


def escolha(txt):
    while True:
        menu()
        opção = leiaint((f'{c["verde"]}Sua Opção: {c["sem cor"]}'))
        if opção == 1:
            lista(txt)
            #ex115.lib.arquivo.lerArquivo(txt)
        elif opção == 2:
            cadastro(txt)
        elif opção == 3:
            cabeçalho('Saindo do Sistema...Até Logo!!')
            sleep(1)
            break
        else:
            print(f'{c["vermelho"]}ERRO - Opção Inválida{c["sem cor"]}')
