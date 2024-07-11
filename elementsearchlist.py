lst=[1,2,3,4,3,2,4,22,3,4,2,3,4,3,3,54,33,3,2]
search=int(input("enter the element to search:"))
for i in lst:
    if i==search:
        pos=lst[i]
    
print("element found at position:",pos)
    
