import datetime
buka = open("d:/dataPERPUS.txt", "r")
file  = []
file2 = []
file3 = []
file4 = []
file5 = []

for line in buka:
    splitfile = line.split("|")
    file.append(splitfile[0])
    file2.append(splitfile[1])
    file3.append(splitfile[2])
    file4.append(splitfile[3])
    file5.append(splitfile[4].strip())

lagi = str(input("Masukkan kode member yang mau dicari : "))
if lagi in file:
    find = True
    i = file.index(lagi)
    now = datetime.datetime.now()
    x = file5[i]
    from datetime import datetime
    x = datetime.strptime(x, "%Y-%m-%d")
    rumus = x - now
    from datetime import *
    kembali = datetime.date(now)
    maks = datetime.date(x)
else:
    print("file tidak ditemukan")
    exit()
if find == True:
    rumus = datetime.date(now) - maks
    rumus = int(rumus.days)
    denda = 0
    if rumus >= 0:
        denda = 2000 *(rumus)
        rumus = abs(rumus)
    elif rumus <= 0:
        rumus = 0

    print("\nfile Peminjaman Buku\n"
         "\nKode Member                    : ",file[i],
         "\nNama Member                    : ",file2[i],
         "\nJudul Buku                     : ",file3[i],
         "\nTanggal Mulai Peminjaman       : ",file4[i],
         "\nTanggal Maks Peminjaman        : ",file5[i],
         "\nTanggal Pengembalian           : ",kembali,
         "\ntelat                          : ", rumus,"Hari"
         "\nTotal denda                    :  Rp.",denda)

else:
    print("Data tidak ditemukan")
        
