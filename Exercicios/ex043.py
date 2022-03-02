peso = float(input('Peso (kg):'))
altura = float(input('Altura (m):'))
icm = peso / altura**2
print('O ICM dessa pessoaa é {:.2f} kg/m²'.format(icm))
if icm < 18.5:
    print('Abaixo do Peso!')
elif icm < 25:
    print('Peso ideal!')
elif icm <30:
    print('Sobrepeso')
elif icm <40:
    print('Obesidade')
else:
    print('Obesidade mórbida! CUIDADO')