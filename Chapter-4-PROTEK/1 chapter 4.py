#import library
import time

#Harga rental mobil yang diberikan
print('____________________Rental Mobil____________________')

#jeda 2 detik
time.sleep(2)

print('Harga sewa 12 jam pertama:Rp.200000')

#jeda 3 detik
time.sleep(3)

print('Harga sewa setelah 12 jam per jamnya:Rp.10000')
Harga=float('200000')
Hargatambahan=float('10000')
print('_____________________________________________________________')

#jeda 3 detik
time.sleep(3)

#Waktu sewa mobil yang dipakai
print('Waktu peminjaman:')
jam1=float(input('Jam:'))
menit1=float(input('menit:'))
print('Waktu pengembalian:')
jam2=float(input('Jam:'))
menit2=float(input('menit:'))
SelisihJam=jam2-jam1
SelisihMenit=menit2-menit1
print('Total waktu:',round(SelisihJam),'jam',round(SelisihMenit),'menit')
print('_____________________________________________________________')

#jeda 3 detik
time.sleep(3)

#Pembayaran rental mobil
if(SelisihJam > 12):
    print('Harga sewa total:Rp.',Harga+(Hargatambahan*(SelisihJam-12)+Hargatambahan*(SelisihMenit/60)))
elif(SelisihJam < 12):
    print('Harga sewa total:Rp.',(Harga/12*(SelisihJam)+Harga/12/60*(SelisihMenit)))
else:
    print('Harga sewa total:Rp.',Harga)
