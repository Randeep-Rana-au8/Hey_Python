def jumpingOnClouds(c):
    steps = 0
    n = len(c)
    i = 0
    while i < n-1:
        if i < (n-2) and c[i+2] == 0:
                steps+=1
                i+=2
        elif i < (n-1) and c[i+1] == 0:
            steps+=1
            i+=1
        
    return steps