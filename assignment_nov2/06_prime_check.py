number = int(input("Enter a number: "))

if number < 2:
    print(number, "is not a prime number")
else:
    is_prime = True

    # Check if any number from 2 to number - 1 divides it exactly.
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
