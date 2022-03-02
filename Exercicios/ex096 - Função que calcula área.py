def area(a,b):
    ar=a*b
    print(f'A área de um terreno de {a}x{b} é {ar}m²')


print('Controle de Terrenos')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura,comprimento)