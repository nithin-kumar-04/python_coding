def second_largest(numbers):
    # Remove duplicates so a repeated largest value is not returned.
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort()
    return unique_numbers[-2]


numbers = [45, 12, 89, 67, 89, 34]
print("List:", numbers)

result = second_largest(numbers)

if result is None:
    print("The list does not have a second-largest number.")
else:
    print("Second-largest number:", result)
