def extractEachKth(inputArray, k):
    res = []
    for i in range(len(inputArray)):
        if (i+1)%k == 0:
            pass
        else:
            res.append(inputArray[i])
    return res
