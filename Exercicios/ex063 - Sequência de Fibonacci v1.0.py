print('-'*25)
print('sequencia de Fibonacci')
print('-'*25)
termos = int(input('Quantos termos qdeseja ver?'))
c=0
t = 0
a = 0
b = 0
t2 = termos-1
while c < t2:
    print(t,end='>>')
    if t == 0:
        t+=1
        a = t
        b = t
    elif t==1:
        print(t, end='>>')
        t = a+b
        a = t
    else:
        t = a+b
        b=a
        a=t
    c+=1
print('FIM')

