#import library
import time

#header
print('_______________Status Kelulusan Ujian Mahasiswa________________')

#input nilai
BhsIndo=int(input('Masukan nilai Bahasa Indonesia: '))
IPA=int(input('Masukkan nilai IPA: '))
Mate=int(input('Masukkan nilai Matematika: '))
print('_______________________________________________________________')

#jeda 3 detik
time.sleep(3)

#Status kelulusan
if(BhsIndo >=60 and BhsIndo <=100 and IPA >=60 and IPA <=100 and Mate >70 and Mate <=100):
    print('Status Kelulusan: Lulus')
elif(not(BhsIndo >=0 and BhsIndo <=100 and IPA >=0 and IPA <=100 and Mate >=0 and Mate <=100)):
    print('Maaf input ada yang tidak valid')
else:
        sebab = ""
        if(BhsIndo < 60):
            sebab += "- Nilai bahasa indonesia kurang dari 60\n"
        if(IPA < 60):
            sebab += "- Nilai IPA kurang dari 60\n"
        if(Mate <= 70):
            sebab += "- Nilai Matematika kurang dari sama dengan 70\n"
        print("\nTIDAK LULUS")
        print("Sebab : ")
        print(sebab)
