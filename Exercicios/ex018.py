import math
ang = float(input('Digite o angulo desejado:'))
ar = math.radians(ang)
print('O angulo de {:.2f}° tem o SENO de {:.2f} , o COSSENO de {:.2f} e a TANGENTE de {:.2f}'.format(ang, math.sin(ar), math.cos(ar), math.tan(ar)))
