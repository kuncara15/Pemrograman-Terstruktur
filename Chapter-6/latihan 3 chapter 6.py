def faktorial(n):
    angka = n
    while(n > 1):
        n-=1
        angka*=n
    return angka

def kombinasi (n,r):
    return faktorial(n)/(faktorial(n-r)*faktorial(r))

def permutasi (n,r):
    return faktorial(n)/(faktorial(n-r))

print(kombinasi(5,3))
print(permutasi(10,7))
    
