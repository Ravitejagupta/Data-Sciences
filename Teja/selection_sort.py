a=[5,4,3,2,1,78,7,8,10,9]
for i in range(len(a)):
  min = a[i]
  for j in range(1,len(a)-i):
    if a[i+j] < min:
      min = a[i+j]
      temp = a[i]
      a[i] = a[i+j]
      a[i+j] = temp
print(a)
      