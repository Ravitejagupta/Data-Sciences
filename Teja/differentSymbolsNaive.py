def differentSymbolsNaive(s):
    res = []
    for i in s:
        if i not in res:
            res.append(i)
    return len(res)
