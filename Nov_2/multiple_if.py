username=input("Enter your username: ")
password=int(input("Enter your password: "))
if username=="":
    print("enter your username")
if password=="":
    print("enter your password")
if username=="admin" and password==1234:
    print("login successful")
if username!="admin" and password!=1234:
    print("invalid credentials. Please enter valid username and password")