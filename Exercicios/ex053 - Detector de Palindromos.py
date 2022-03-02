frase = str(input('Digite uma frase:')).strip().upper().split()
junto = ''.join(frase)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um palindromo')
else:
    print('Não temos um palindromo')
