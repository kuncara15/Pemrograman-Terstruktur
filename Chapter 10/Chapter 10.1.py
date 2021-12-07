myFile=open('d:\Angka.txt', 'r')
readlines=myFile.readlines()

genap=0
ganjil=0
i=0


for isi in readlines:
    if int(readlines[i]) %2 == 0:
        genap+=1
    else:
        ganjil+=1
    i+=1

print('Banyak bilangan genap: ', genap)
print('Banyak bilnagan ganjil: ', ganjil)
    
