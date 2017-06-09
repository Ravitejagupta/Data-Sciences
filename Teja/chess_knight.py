def chessKnight(cell):
    a=[[1,2],[2,1],[-1,-2],[-2,-1],[-1,2],[-2,1],[1,-2],[2,-1]]
    c=0
    for i in a:
        if ((i[0]+ord(cell[0])-96) in list(range(1,9))) and (i[1]+int(cell[1]) in list(range(1,9))) :
            c+=1
    return c
