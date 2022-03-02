times = ('Gremio', 'Atletico/MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Corinthians', 'Bragantino',
         'Fluminense', 'América', 'Atletico/GO', 'Santos', 'Ceará', 'São Paulo', 'Athetico/PR', 'Cuiaba',
         'Juventude', 'Bahia', 'Sport', 'Chapecoense', 'Inter')

print('-=-'*30)
print(f'Lista dos times do Brasileirão: {times}')
print('-=-'*30)
print(f'Time em ordem alfabetica: {sorted(times)}')
print('-=-'*30)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=-'*30)
print(f'Os 4 últimos são {times[-4:]}')
print('-=-'*30)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')# Utilizado aspas dupla(")   devido a programação ja estar dentro de aspas simples (')


