lista = []
n = 0
while n < 5:
    v = int(input('Digite um valor:'))
    if v in lista:
        print('Valor ja existente!!')
    else:
        if not lista or v>lista[-1]:
            print('Adicionado ao final da lista')
            lista.append(v)
            n +=1
        else:
            for i, num in enumerate(lista):
                if v <= num:
                    lista.insert(i,v)
                    n+=1
                    print(f'Valor adicionado na posição {i}')
                    break
print(lista)