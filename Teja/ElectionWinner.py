def electionsWinners(votes, k):
    c=0
    m = votes[0]
    mod =0
    for i in votes:
        if i>m:
            m=i
            mod =1
        elif i==m:
            mod+=1
    print(mod)
    if k==0:
        if mod>1:
            return 0
        else:
            return 1
    else:
        for i in votes:
            if i+k > m:
                c+=1
        return c
