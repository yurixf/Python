val = [[],[]]
for c in range (7):
    v = int(input(f'Digite o {c+1}º valor:'))
    if v%2==0:
        val[0].append(v)
    else:
        val[1].append(v)
val[0].sort()
val[1].sort()
print(f'Os valores parares digitados foram {val[0]}')
print(f'Os valores impares digitados foram {val[1]}')