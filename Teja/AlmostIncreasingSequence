import copy
def almostIncreasingSequence(a):
	c=copy.deepcopy(a)
	c.append(10000)
	b=[]
	for i in range(len(c)-1):
		if c[i]<c[i+1] and c[i] not in b:
			b.append(c[i])
	if len(a)<=2 and len(b)<2:
		return True
	if len(b) <len(a)-1 and len(a)>2:
		return False
	else:
		return True
