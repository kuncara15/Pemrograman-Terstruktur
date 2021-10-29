#import library
import time

#header
print('_______________Status Kelulusan Ujian Mahasiswa________________')

#input nilai
BhsIndo=int(input('Masukkan nilai Bahasa Indonesia: '))
IPA=int(input('Masukkan nilai IPA: '))
Mate=int(input('Masukkan nilai Matematika: '))
print('_______________________________________________________________')

#jeda 3 detik
time.sleep(3)

#Status kelulusan
if(BhsIndo >= 60 and IPA >= 60 and Mate > 70):
    print('Status Kelulusan: Lulus')
else:
    print('Status Kelulusan: Tidak Lulus')
    

