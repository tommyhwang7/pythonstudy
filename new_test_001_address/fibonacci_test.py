n=13
a=0;b=1
print('0', end='')
while b<=n:
    print(', %d'%b, end='')
    t=a
    a=b
    b=t+b


