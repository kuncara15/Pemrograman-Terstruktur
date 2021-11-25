def bintang(n):
    space=2*n-1
    for i in range(n):
        print(('*'*(2*i+1)).center(space))


def bintang2(n):
    space=3*n-1
    for i in range(n):
        print(('*'*(2*(n-i)-1)).center(space))

def bintang3(n):
    if(n % 2 == 0):
        bintang(n//2)
    else:
        bintang(n//2 + 1)
    bintang2(n//2)
        

bintang3(7)
