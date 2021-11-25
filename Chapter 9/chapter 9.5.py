nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*60)
data=("NIM\t NAMA MHS\t MID\t UAS")
print(data.center(41))
print('-'*60)

for i in range (len(nilai)):
    print(nilai[i]['nim'].ljust(5).rjust(14), end='')
    print(nilai[i]['nama'].ljust(15).rjust(18), end='')
    print(str (nilai[i]['mid']).rjust(4).ljust(5), end='')
    print(str(nilai[i]['uas']).rjust(7))

print('='*60)
