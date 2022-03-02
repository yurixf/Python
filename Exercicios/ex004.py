n = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaços:{}'.format(n.isspace()))
print('É numero:{}'.format(n.isnumeric()))
print('É alfabético:{}'.format(n.isalpha()))
print('As letras são maiusculas:{}'.format(n.isupper()))
print('As letras são minusculas:{}'.format(n.islower()))
print('Está capitalizada:{}'.format(n.istitle())) #Capitalizado significa que tem letras maisculas e minusculas
