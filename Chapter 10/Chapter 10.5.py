file=open('d:\Angka2.txt', 'r')
file1=open('d:\hasilAngka2.txt', 'w+')

x=[]
lines=file.readlines()
for i in range(len(lines)):
     splitdata=lines[i].split('|')
     jumlah=int(splitdata[0])+int(splitdata[1].strip('\n'))
     x+=[jumlah]

for i in range(len(x)):
    file1.write(str(x[i])+'\n')
file1.close()

hasil=open('d:\hasilAngka2.txt')
print(hasil.read())


file.close()
hasil.close()
