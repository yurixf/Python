def leiadinheiro(valor):
    cor = {'limpa': '\033[m',
           'vermelho': '\033[31m'}
    while True:
        num = str(input(valor)).replace(',','.')
        if num.isalpha() or num.strip()=='':
            print(f'{cor["vermelho"]}ERRO!! "{num}" não é um valor válido!{cor["limpa"]}')
        else:
            num=float(num)
            return num

