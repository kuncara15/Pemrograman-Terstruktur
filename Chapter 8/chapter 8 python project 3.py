try:
    n = int(input("\nBanyaknya Data: "))
    print(n)
    data = []
    jum = 0
    while jum < n:
        temp = input("Masukkan data ke-:%s\n"%(jum+1))
        data.append(temp)
        jum+=1

    data.sort()
    print("\nUrutan bilangan bulat dari kecil ke besar:")
    for temp in data:
        print("{0} ({1}karakter)".format(temp,len(tuple(temp))))

except ValueError:
    print('Data yang dimasukkan salah')
