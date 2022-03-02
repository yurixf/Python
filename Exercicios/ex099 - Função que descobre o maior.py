def valores(* val):
    print('-'*30)
    print('Analisando os valores passados...')
    for c in val:
        print(c, end= ' ')
    print(f'Foram informados {len(val)} valores ao todo.')
    print(f'O maior valor informado é o {max(val)}')


valores(4,7,3,5,1)
valores(2,9,5,0,8,1,12)
valores(2,5)
valores(1)