def digitsProduct(product):
    for i in range(1,10000):
        if prod(map(int,str(i))) == product:
            return i
    return -1
        
import operator
from functools import reduce
def prod(iterable):
    return reduce(operator.mul, iterable)
