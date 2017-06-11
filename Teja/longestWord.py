import re
def longestWord(text):
    d=[]
    a=0
    b=0
    removeSpecialChars = text.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:./<>?\|`~-=_+"})
    for i in removeSpecialChars.split(","):
        i.strip()
        print(len(i))
        d.append(len(i.strip()))
    b = d[0]
    print(removeSpecialChars)
    for i in range(1,len(removeSpecialChars.split(","))):
        if d[i]>b:
            b=d[i]
            a=i
    return(removeSpecialChars.split(",")[a].strip())
