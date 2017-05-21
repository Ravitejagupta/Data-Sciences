def palindromeRearranging(inputString):
    a=list(set(inputString))
    l1 = list(inputString)
    l1.sort()
    d = dict()
    c=0
    for i in a:
        d[i] = l1.count(i)
    for k in d.values():
        if k%2 !=0 :
            c+=1
    return(c<=1)
