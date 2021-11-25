mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']


print('='*60)
print('NIM'.ljust(10, ' '), 'NAMA MAHASISWA'.ljust(20, ' '),
      'TGL LAHIR'.ljust(15, ' '), 'TEMPAT LAHIR'.ljust(20, ' '))
print('-'*60)

for i in mhs:
    listdata=i.split(':')
    splittgl=listdata [2]
    lahir=splittgl[2]+'/'+splittgl[1]+'/'+splittgl[0]
    print(listdata[0].ljust(10, ' '), listdata[1].ljust(20, ' '),
      listdata[2].ljust(15, ' '), listdata[3].ljust(20, ' '))
    
print('-'*60)
