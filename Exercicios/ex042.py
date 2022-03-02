a = float(input('Aresta 1:'))
b = float(input('Aresta 2:'))
c = float(input('Aresta 3:'))

ab = a+b
ac = a+c
bc = b+c

if ab>c and ac>b and bc>a:
    print('As arestas PODEM formar um triangulo', end=' ')
    if a == b and b == c:
        print('EQUILATERO')
    elif a==b or a==c or b==c:
        print('Isóceles')
    else:
        print('Escaleno')
else:
    print('As arestas NÃO PODEM formar um triangulo')
