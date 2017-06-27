a=[6,5,4,3,2,1]
for i in range(1,len(a)):
  m=a[i-1]
  for j in range(i):
    if a[i-j] < a[i-j-1]:
      temp = a[i-j-1]
      a[i-j-1] = a[i-j]
      a[i-j] = temp
    else:
      m = a[i]
print(a)