fileInput=input('Masukkan nama file: ')
tambah='y'
 
try:
    file=open(fileInput, "r")
    while tambah=='y':
        append=input('Data yang mau ditambahkan: ')
        file=open(fileInput, "a")
        file.write(append)
        tambah=input('Mau lagi (y/n): ')
        file=open(fileInput, "a")

except FileNotFoundError:
    print('File tidak ditemukan atau terdapat salah penulisan')
