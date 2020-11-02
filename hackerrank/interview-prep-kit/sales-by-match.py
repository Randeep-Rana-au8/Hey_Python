def sockMerchant(n, ar):
    newList = list(set(ar))
    x = 0
    for i in newList:
        count = 0
        for j in ar:
            if i == j:
                count+=1
        x+=(count//2) 
        print(x)
    return x
