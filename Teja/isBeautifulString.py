import collections

def isBeautifulString(inputString):
    if inputString.count('a') == 0:
        return False
    d = {}
    for i in inputString:
        d[i] = inputString.count(i)
    od = collections.OrderedDict(sorted(d.items()))
    k = list(od.values())
    s = sorted(od)
    if (ord(s[len(s)-1]) - ord(s[0]) + 1 == len(s)):
        return(k == sorted(k,reverse = True))
    else:
        return False
