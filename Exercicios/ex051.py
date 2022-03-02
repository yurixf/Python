primeiro = int(input('1º termo:'))
razão = int(input('Razão:'))
decimo = primeiro + (11-1) * razão
for c in range (primeiro, decimo, razão):
    print(c, end="->")
print('Acabou')