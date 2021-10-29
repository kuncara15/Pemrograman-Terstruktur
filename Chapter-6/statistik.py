def average(*bil):
    hasil=0
    x=0
    for i in bil:
         hasil+=i
         x+=1
    print(hasil/x)


def maks(*bil):
    hasil=0
    for i in bil:
        if i >= hasil:
            hasil=i
    print(hasil)


def min(*bil):
    hasil=999999999999999999999
    for i in bil:
        if i <= hasil:
            hasil=i
    print(hasil)
