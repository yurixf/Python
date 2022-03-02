import ex115.lib.interface


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        ex115.lib.interface.cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dados=linha.split(';')
            dados[1]=dados[1].replace('\n','')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')

    finally:
        a.close()

def cadastro(arq, nome='Desconhecido', idade=0):
    try:
        a=open(arq,"at")
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao salvar os dados')
        else:
            print(f'Novo registro de {nome} adicionado')