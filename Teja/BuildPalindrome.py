def buildPalindrome(st):
    st1 = list(st)
    stre = list(reversed(st))
    for i in range(len(st)):
        if(st1[i:] == stre[:len(st1)-i]):
            res = st1[:i]+st1[i:]+list(reversed(st1[:i]))
            break
    return ''.join(res)
