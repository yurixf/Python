from random import sample

print('-'*30)
print(f'{"JOGOS DA MEGA SENA":^30}')
print('-'*30)
jogos = int(input('Quantos jogos?'))
print('-=-'*2,f'SORTEANDO {jogos} JOGOS','-=-'*2)
for c in range (jogos):
    n = sample(range(1,25), k=15)
    n.sort()
    print(f'Jogo {c+1}: {n}')
print('-=-'*3, '< BOA SORTE >', '-=-'*3)
