#sum of series upto n terms

num=int(input("enter the value for sequence:"))
start=5
series=0
for i in range(1,num):
    series+=start
    start=start*10+5
    
print("the series of the numbers are:",series)
print("the sum of series are::",start)
