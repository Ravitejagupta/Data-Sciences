import math
def differentSquares(matrix):
    if len(matrix)<2 or len(matrix[0])<2:
        return 0
    
    lis=[]
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            vec=[matrix[i][j],matrix[i][j+1],matrix[i+1][j],matrix[i+1][j+1]]
            print(vec)
            if lis.count(vec)==0:
                lis=lis+[vec]
    
    return len(lis)
