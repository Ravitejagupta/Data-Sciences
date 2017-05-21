import copy

def minesweeper(matrix):
    b = [0]*(len(matrix[0]) + 2)
    for a in matrix:
        a.insert(len(a),0)
        a.insert(0,0)
    matrix.insert(0,b)
    matrix.insert(len(matrix),b)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] =1
            else:
                matrix[i][j] =0
    print(matrix)
    result = copy.deepcopy(matrix)
    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix[0])-1):
            result[i][j] =sum([matrix[i][j-1],matrix[i][j+1],matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1],matrix[i+1][j-1],matrix[i+1][j],matrix[i+1][j+1]])
    result = result[1:-1]
    res1 = [i[1:-1] for i in result]
    return(res1)
    
