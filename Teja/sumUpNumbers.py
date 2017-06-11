def sumUpNumbers(inputString):
    r = inputString.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    j = r.translate ({ord(c): " " for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"})
    k = j.split()
    print(k)
    return sum(int(i) for i in k)


################################################################################################
sumUpNumbers = lambda s : sum(map(int, re.sub("[^\d]", " ", s).split()))
#################################################################################################
