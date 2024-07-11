#count frequency of a number in a list
a=[1,2,2,3,2,3,4]
element=int(input("enter the element to count:"))
count=0
for i in a:
    if element == i:
        count+=1
print(count)
