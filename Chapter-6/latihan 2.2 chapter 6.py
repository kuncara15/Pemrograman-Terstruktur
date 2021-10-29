def starFormation1 (n):
    kolom=1
    a=0
    while(a<n):
        b=0
        while(b<kolom):
            print('*', end='')
            b+=1
        kolom+=1
        print('')
        a+=1

def starFormation2 (n):
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

def starFormation3(n):
    if(n % 2 == 0): 
        starFormation1(n//2)
    else:
        starFormation1(n//2 + 1)
    starFormation2(n//2)

starFormation3(7)
