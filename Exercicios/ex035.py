print('-=-' * 20)
print('Analisador de Triangulos')
print('-=-' * 20)
a = float(input('Aresta 1:'))
b = float(input('Aresta 2:'))
c = float(input('Aresta 3:'))

ab = a + b
ac = a + c
bc = b + c

if ab > c and ac > b and bc > a:
    print('As arestas acima PODEM formar um triangulo')
else:
    print('As arestas acima NÃO PODEM formar um triangulo')
