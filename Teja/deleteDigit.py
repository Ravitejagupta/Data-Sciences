def deleteDigit(n):
    r=[]
    k=str(n)
    for i in range(len(k)):
        r.append(int(k[0:i]+k[i+1:]))
    return max(r)
