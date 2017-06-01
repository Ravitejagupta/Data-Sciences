def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    u1 = max(yourLeft,yourRight)
    p1 = max(friendsLeft,friendsRight)
    if(yourLeft+yourRight == friendsLeft+friendsRight):
        return(u1 == p1)
    return False
