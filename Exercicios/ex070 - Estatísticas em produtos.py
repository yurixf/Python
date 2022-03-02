total = mil = 0
barato = ''
pb = ''
while True:
    produto = str(input('Nome do produto:')).strip().title()
    preço = float(input('Valor: R$'))
    total +=preço
    if preço > 1000:
        mil+=1
    if barato == '' or barato > preço:
        barato = preço
        pb = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {pb} e custou R${barato:.2f}')