print('-'*20)
print('Sequenci de Fibonacci')
print('-'*20)
n = int(input('Nº de termos: '))
t1 = 0
t2 = 1
print(t1,'>>',t2, end=' >> ')
c = 3
while c <= n:
    t3 = t1+t2
    print(t3, end=' >> ')
    t1=t2
    t2=t3
    c +=1
print('FIM')