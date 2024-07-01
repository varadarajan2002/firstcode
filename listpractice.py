#create a list

a=[1,2,3,4]
print(a)

#accessing a element in list

a=[1,2,3,4]
print(a[2])

#length of the list

a=[1,2,3,4]
print(len(a))

#list concatenation
a=[1,2,3,4]
b=[5,6,7,8]
print(a+b)

#list slicing print 2,3,4 elements of a list
a=[123,33,2,42,4,32,5,2,3]
print(a[2:5])


#adding elements to a list

a=[1,2,3,4]
a.append(6)
print(a)

#remove a element
a=[1,2,3,4]
a.remove(4)
print(a)

#list comprehension
#print square numbers from 1 to 10

l=[]
for i in range(1,11):
    l.append(i**2)
print(l)
