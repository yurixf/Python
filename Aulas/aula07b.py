n1 = int(input('Digite valor 1: '))
n2 = int(input('Digite valor 2: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
r = n1%n2
e = n1**n2
print ('Considerando os valores {} e {}, \n a soma é {}, o produto é {} e a divisão é {:.3f}'.format(n1, n2, s, m, d), end='. ')
print ('A divisão inteira é {}, o resto da divisão é {} e a potencia é {}'.format(di, r, e))
# \n comando para quebrar linha
# end='' comando para colocar dois prints na mesma linha
# :.3f dentro das chaves serve para devinir o numero de casas depois da virgula
