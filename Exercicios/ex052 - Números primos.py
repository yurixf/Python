num = int(input('Digite um número:'))
contador = 0
cores = {'limpa':'\033[m','vermelho':'\033[31m','branco':'\033[33m'}
for c in range (1, num+1):
    if num%c == 0:
        contador +=1
        print('{}{}{}'.format(cores['branco'],c,cores['limpa']), end=' ')
    else:
        print('{}{}{}'.format(cores['vermelho'],c,cores['limpa']), end=' ')
print('')
print('O numero {} foi divisivel {} vezes'.format(num, contador))
if contador>2:
    print('Por isso o ele NÃO é PRIMO')
else:
    print('Por isso ele é PRIMO')