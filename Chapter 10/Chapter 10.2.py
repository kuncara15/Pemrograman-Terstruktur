file=open('d:\datamahasiswa1.txt', 'a')

while True:
    nim=input('Masukkan NIM: ')
    nama=input('Masukkan nama MHS: ')
    alamat=input('Masukkan Alamat: ')
    mystring=nim+'|'+nama+'|'+alamat+'\n'
    file.write(mystring)
    lagi=input('\nUlangi input? (y/n):' )
    if lagi in ('N', 'n'):
        break

file.close()
