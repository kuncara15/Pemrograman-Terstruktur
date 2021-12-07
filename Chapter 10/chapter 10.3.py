file=open('d:\datamahasiswa1.txt', 'r')

listfile=[]
lines=file.readlines()
for i in range(len(lines)):
     splitdata=lines[i].split('|')
     dictlines={'nim': splitdata[0], 'nama': splitdata[1], 'alamat': splitdata[2].rstrip('\n')
                }
     listfile.append(dictlines)
print(listfile)
file.close()
