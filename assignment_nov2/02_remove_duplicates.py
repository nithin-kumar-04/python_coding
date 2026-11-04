numbers = [10, 20, 10, 30, 20, 40, 50, 30, 10]

print("Original list          :", numbers)

# Create a new list and add an item only if it is not already there.
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("List without duplicates:", unique_numbers)

# Another easy way is:
# unique_numbers = list(set(numbers))
# But set() may not keep the original order.
