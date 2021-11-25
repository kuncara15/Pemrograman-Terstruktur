nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*65)
data=("NIM\t NAMA MHS\t MID\t UAS\t N.AKHIR\t STATUS")
print(data.center(41))
print('-'*65)

for i in nilai:
    akhir = (i['mid'] + 2*i['uas']) / 3
    akhir_bulat=round(akhir)
    if akhir_bulat >= 60:
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'
    print(i['nim'].ljust(5).rjust(6), i['nama'].ljust(9).rjust(11), str (i['mid']).rjust(8),
          str(i['uas']).rjust(8), str(akhir_bulat).ljust(10).rjust(16),
          str(status).rjust(9))

print('-'*63)
