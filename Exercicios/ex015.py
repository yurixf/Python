d = int(input('Dias alugados:'))
km = float(input('km rodados:'))
cd = d * 60
ckm = km * 0.15
ct = cd ++ ckm
print('O valor total a pagar é R${:.2f}'.format(ct))