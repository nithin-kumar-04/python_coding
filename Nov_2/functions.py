#function
#function is a block of code which only runs when it is called.
#you can pass data, known as parameters, into a function. 
#A function can return data as a result.



def odd_even(num):
    if num % 2 == 0:
        print(f"{num} is an even number")
        return "Even"
    else:
        print(f"{num} is an odd number")
        return "Odd"

#odd_even(8)

def my_function(first_name, last_name, age):
    print(f"Hello {first_name} {last_name}, you are {age} years old.")

#my_function("Nithin", "Kumar", 20)

#function returning a value
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def sub(a, b):
    return a - b   
 

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    user_choice = input("Choose an operation (add, subtract, multiply, divide): ")
    if user_choice == "add":
        print(f"The sum of {a} and {b} is: {add(a, b)}")
    elif user_choice == "subtract":
        print(f"The difference between {a} and {b} is: {sub(a, b)}")
    elif user_choice == "multiply":
        print(f"The product of {a} and {b} is: {mul(a, b)}")   
    elif user_choice == "divide":
        print(f"The quotient of {a} and {b} is: {div(a, b)}")
    else:
        print("Invalid operation. Please choose from add, subtract, multiply, or divide.")

#main()