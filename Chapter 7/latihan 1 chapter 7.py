inputFile=input('Masukkan nama file: ')

try:
    file=open(inputFile, "r")
    print('Isi file', inputFile, 'adalah: ', file.read())
except:
    print('File tidak ditemukan atau terdapat salah penulisan')
