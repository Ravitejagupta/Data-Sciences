def longestDigitsPrefix(inputString):
    c = 0
    m = []
    if not inputString[0].isdigit():
        return ""
    else:
        for i in inputString:
            if i.isdigit():
                m.append(i)
            else:
                break
        return ''.join(m)
            
