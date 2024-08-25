a=[1,2,35,4,3,6,4,3,5]
a.sort()
low=0
high=len(a)-1
target=6

while low<=high:
    mid=(low+high)//2
    if a[mid]==target:
        print(a[mid])
        break
    elif a[mid]>target:
        high= mid-1
        # print(mid)
    else:
        low=mid+1
        #print(mid)
else:
    print("not found")
