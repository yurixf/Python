exp = list(str(input('Digite a expressão: ')))
abre = exp.count('(')
fecha = exp.count(')')
if abre == fecha:
    print('Sua expressão está correta')
else:
    print('Sua expressão esta errada')