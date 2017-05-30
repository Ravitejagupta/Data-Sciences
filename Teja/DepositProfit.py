def depositProfit(deposit, rate, threshold):
    k=0
    t=0
    while(t<threshold):
        t = deposit*(1 + rate/100)**k
        k+=1
    return(k-1)
