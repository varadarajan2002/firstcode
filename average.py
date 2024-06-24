#average of numbers



total=int(input("enter the total numbers:"))
sum=0

for i in range(1,total+1):
    num = int(input(f"enter the value {i}:"))
    sum+=num
    
average=sum/total
print("the average of the given numbers are:",average)
