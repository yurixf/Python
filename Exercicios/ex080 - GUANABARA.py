lista = []
for c in range (5):
    n = int(input('Digite um numero:'))
    if c == 0 or n>lista[-1]:
        lista.append()
        print('Valor inserido no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n<=lista[pos]:
                lista.insert(pos,n)
                print(f'Valor adicionado na posição {pos}')
                break
            pos+=1
print(lista)