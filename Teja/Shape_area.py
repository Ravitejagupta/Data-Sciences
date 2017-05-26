def shapeArea(n):
    area = 0
    if n == 1 :
        return 1
    for i in range(1,(2*n-1),2):
        area += 2*i
    print(area)
    return(area +( 2*n -1))
