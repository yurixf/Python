lar = float(input('Largura: '))
alt = float(input('Altura: '))
area = lar*alt
c=2
tinta = area/c
print('Sua parede tem dimensões de {} x {} e sua área é de {}m²'.format(lar, alt, area))
print('Para pintar essa parede, voce precisara de {}l de tinta'.format(tinta))