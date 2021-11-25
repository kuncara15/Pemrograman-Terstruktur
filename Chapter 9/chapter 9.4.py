def shuffleString(x, n):
    import random
    result = []
    for i in range (n):
        acak=[]
        if acak not in result:
            acak = ''.join(random.sample(x, len (x)))
            result+=[acak]
            i+=1
    print(result)

shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
