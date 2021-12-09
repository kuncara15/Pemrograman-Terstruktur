from datetime import *

try:
    def diffDate(x):
        now= datetime.date(datetime.now())
        print('Tanggal hari ini: ', now)
        splittgl=x.split('-')
        x=date(year=int(splittgl[0]), month=int(splittgl[1]), day=int(splittgl[2]))
        selisih=x-now
        print(selisih.days)
        return

    tgl=input('Masukkan tanggal (tahun-bulan-tanggal): ')
    diffDate (tgl)
except ValueError:
    print('Maaf format tanggal yang anda masukkan salah')
except IndexError:
    print('Maaf format tanggal yang anda masukkan salah')
