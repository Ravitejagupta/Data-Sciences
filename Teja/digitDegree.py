def digitDegree(n):
    c=0
    while(n>9):
        k=0
        c+=1
        for i in str(n):
            k+=int(i)
        n=k
    return c
