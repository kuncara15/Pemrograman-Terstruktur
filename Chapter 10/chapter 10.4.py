file=open('d:\datamahasiswa1.txt', 'r')

nim=[]
nama=[]
alamat=[]
lines=file.readlines()
for i in range(len(lines)):
     splitdata=lines[i].split('|')
     nim.append(splitdata[0])
     nama.append(splitdata[1])
     alamat.append(splitdata[2].strip('\n'))
NIM=input('Masukkan NIM yang mau dicari: ')
if NIM in (nim):
     x=nim.index(NIM)
     print('Data Mahasiswa: ')
     print('\nNIM: ', nim[x])
     print('Nama: ', nama[x])
     print('Alamat: ', alamat[x])
else:
     print('\nData mahasiswa tidak ditemukkan')
     

