v1 = int(input('Valor 1:'))
v2 = int(input('Valor 2:'))
v3 = int(input('Valor 3:'))
vt = [v1, v2, v3]
print('O menor valor digitado foi {}'.format(min(vt)))
print('O mario valor digitado foi', max(vt))

# Solução do Guanabara - Curso em Video
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3

maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

print(menor, maior)
