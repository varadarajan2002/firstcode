#calculate the cube of all the given numbers from 1 to given number

total=int(input("enter the total number you want the cube value:"))
cube=1

for i in range(1,total+1):
    num=int(input(f"enter the value {i}:"))
    cube=num*num*num
    print("cubic value of the given number is::",cube)
    
