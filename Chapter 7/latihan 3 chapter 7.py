print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')

jml=0
rata=0
lagi='y'
while lagi=='y':
    try:
        masuk=int(input('Masukkan bilangan bulat: '))
        jml+=masuk
        rata+=1
        lagi=input('Lagi (y/n)? : ')
    except ValueError:
        print("Bukan bilangan bulat")
print('\nRata-ratanya adalah: ', jml/rata)
        
