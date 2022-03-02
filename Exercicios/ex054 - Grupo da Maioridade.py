from datetime import date
maior = 0
menor = 0
hoje = date.today().year
for c in range (1,8):
    ano = int(input('{}º - Ano de Nascimento:'.format(c)))
    if hoje-ano >= 18:
        maior +=1
    else:
        menor +=1
print('Ao todo tivemos {} pessoas mariores de idade e {} menores de idade'.format(maior,menor))
