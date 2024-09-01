a=[0,1,2,3,4]
for i in range(0,6):
    for j in range(0,5-i-1):
        print(a[j],a[j+1])
    print()