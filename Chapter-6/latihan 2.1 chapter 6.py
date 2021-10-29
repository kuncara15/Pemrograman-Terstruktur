def starFunction1 (n):
    kolom=n
    a=0
    while(a<n):
        b=0
        while(b<kolom):
            print('*', end='')
            b+=1
        kolom-=1
        print('')
        a+=1

n=4
starFunction1(n)
