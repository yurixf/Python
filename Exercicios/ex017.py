import math
co = float(input('Cateto oposto:'))
ca = float(input('Cateto Adjacente:'))
hip = math.sqrt(co ** 2 + ca ** 2)
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(co, ca)))
print('A hipotenusa vai medir {:.2f}'.format(hip))
