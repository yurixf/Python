import lib

arq = "teste.txt"
if not lib.arquivo.arquivoExiste(arq):
    lib.arquivo.criarArquivo(arq)


opção=lib.interface.escolha(arq)

