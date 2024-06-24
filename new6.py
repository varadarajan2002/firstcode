num1=int(input("enter the value of num1:"))
num2=int(input("enter the value of num2:"))
num3=int(input("enter the value of num3:"))

if num1>num2 and num1>num3:
    print(f"{num1} is the greatest among the three values")

elif num2>num1 and num2>num3:
    print(f"{num2} is the greatest among the three values")

else:
    print(f"{num3} is the greates among the three values")
         
