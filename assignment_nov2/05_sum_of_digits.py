number = int(input("Enter a number: "))

# Work with a positive value so negative numbers are handled too.
number = abs(number)

total = 0
while number > 0:
    digit = number % 10      # Get the last digit
    total = total + digit
    number = number // 10    # Remove the last digit

print("Sum of digits =", total)
