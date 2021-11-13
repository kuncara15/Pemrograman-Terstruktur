def kuadrat(bil):
    if(isinstance(bil, list)):
        for i in range(len(bil)):
            bil[i] **= 2
        return bil
    return False

def getListFromUser():
    try:
        inputData = int(input('Banyak angka yang ingin dimasukkan: '))
        jum = 0
        data = []
        while jum < inputData:
            bilangan = int(input("Masukkan bilangan bulat ke-%d"% (jum+1)))
            data.append(bilangan)
            jum += 1

        return data
    except ValueError:
        print('\ndata yang anda masukan salah')
        return False

listData = getListFromUser()

if(listData):
    print("\nHasil kuadrat dari list",listData,':')
    hasil = kuadrat(listData)
    print(hasil)
