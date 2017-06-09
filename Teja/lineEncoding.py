def lineEncoding(s):
    d = {}
    c=[]
    for i in s:
        if i in d:
            d[i]+=1
        else:
            if len(d)>0:
                if list(d.values())[0] !=1:
                    c.append(str(list(d.values())[0]))
                c.append(list(d.keys())[0])
                d.clear()
            d[i] = 1
    if list(d.values())[0] !=1:
        c.append(str(list(d.values())[0]))
    c.append(list(d.keys())[0])
    return ''.join(c)
