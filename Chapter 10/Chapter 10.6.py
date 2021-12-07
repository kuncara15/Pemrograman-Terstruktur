File = input('Masukkan nama file : ')
key = int(input('Masukkan nilai n : '))
buka= open(File, 'r')
baca = buka.read()
char = list(baca)
data = []

for x in char :
    Ascii_1 = ord(x)
    if Ascii_1 == 32:
        Ascii_2 = Ascii_1
    else:
        Ascii_2 = Ascii_1 + key

        if (Ascii_2 > 122):
            kurang = Ascii_2 - 26
        elif (Ascii_2 > 90 and Ascii_2 < 97) :
            Ascii_2 =Ascii_2 - 26
            
    x = chr(Ascii_2)
    data = data + [x]
    if not char :
        break
gabung = ''.join(data)

hasil = open('d:\SAYASUKAPYTHON2.txt', 'a')
hasil.write(gabung)
hasil.close()
