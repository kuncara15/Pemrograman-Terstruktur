from datetime import *

file=open('d:\dataPERPUS.txt', 'a')
while True:
    x=datetime.date(datetime.now())
    y=x+timedelta(days=7)
    kode=str(input('\nMasukkan Kode Member: '))
    nama=str(input('Masukkan Nama Member: '))
    buku=str(input('Masukkan Judul Buku: '))
    data=[kode, nama, buku, str(x), str(y)]
    file.write('|'.join(data)+'\n')
    mystring=kode+'|'+nama+'|'+buku+'\n'
    lagi=input('\nUlangi input? (y/n): \n' )
    if lagi in ('Y', 'y'):
       continue
    elif lagi in ('N', 'n'):
        print('Data peminjam sudah tersimpan')
        break
    else:
        print('\nUlangi input? (y/n) ')
        break
    file.write(mystring)

file.close()
