a=[1,2,4,2,4,3,5,78]
for i in range(0,len(a)-1,1):
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
print(a)
    