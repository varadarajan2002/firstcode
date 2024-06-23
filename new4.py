Age=int(input("Enter Your Age:"))

if age<18:
    print(f"you are not eligible to vote as minimum age to vote is 18, you are only {age}")
elif age==18:
    print("You are 18 yrs old you are eligible to vote")
else:
    print("eligible to votes")
