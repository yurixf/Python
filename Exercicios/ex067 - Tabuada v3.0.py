while True:
    num = int(input('Quer ver a tabuada de qual valor?'))
    if num < 0:
        break
    print('-'*20)
    c=0
    while c < 10:
        c+=1
        print(f'{num} x {c:2} = {num*c}')
    print('-'*20)
