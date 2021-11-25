def ubahHuruf(teks, a, b):
    Teks=teks.split()
    gabung=""
    for Teks in teks:
        if Teks==a:
            Teks=b
        gabung=''.join([gabung,Teks])
    return gabung

print(ubahHuruf("MATEMATIKA", "T", "S"))
