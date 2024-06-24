print("this a login check")

login=input("Enter yor username:")
loginn=input("Enter your password:")

value1_username="varadarajan"
value1_password="1234"
value2_username="virat"
value2_password="12345"

if value1_username==login and value1_password==loginn:
    print("your are a valid user")

elif value2_username==login and value2_password==loginn:
    print("your are a valid user")
else:
    print("invalid user")
