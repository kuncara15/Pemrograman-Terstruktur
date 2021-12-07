file = open('d:\SAYASUKAPYTHON2.txt', 'r')
key = int(input('Masukkan banyak keyword : '))
baca = file.read()
listData = list(baca)
data = []

for x in listData:
    if (x == ' ') :
        y = ord(x)
    else :
        i = ord(x)
        y = i - key
        if (y < 65) :
            y = y + 26
        elif (90 < y and y < 97) :
            y = y + 26
    character = chr(y)
    data.append(character)
gabung = ''.join(data)

hasil = open('d:\SAYASUKAPYTHON3.txt', 'w')
hasil.write(gabung)
hasil.close()
hasil2 = open('d:\SAYASUKAPYTHON3.txt', 'r')
print(hasil2.read())
hasil2.close()
