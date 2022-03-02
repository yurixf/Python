preco = float(input('Informe o preço do produto:R$'))
desconto = float(input('Informe o % de desconto desse produto:'))
d = 1-(desconto/100)
precof = preco*d
print('O produto que custava {:.2f}, na promoção, com desconto de {}%, vai custar {:.2f}'.format(preco, desconto, precof))
