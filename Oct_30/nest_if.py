
#nested if statement
#if inside if then it is called nested if statement

num = int(input("Enter a number: "))   
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")