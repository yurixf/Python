from datetime import date
trabalhador = {}
trabalhador['nome']=str(input('Nome: ')).strip().title()
nasc=int(input('Ano de Nascimento: '))
trabalhador['idade']=date.today().year-nasc
trabalhador['ctps']=int(input('Nº Carteira de Trabalho (0 se não tem): '))
if trabalhador['ctps']>0:
    trabalhador['ano']=int(input('Ano de Contratação: '))
    trabalhador['salario']=float(input('Salário: '))
    trabalhador['aposentadoria'] = 35+trabalhador['ano']-nasc

for v,k in trabalhador.items():
    print(f'   -{v} tem valor {k}')
print(trabalhador)