
# 1. ARITHMETIC OPERATORS (Math)

a = 10
b = 3

print("Addition (+):", a + b)        
print("Subtraction (-):", a - b)     
print("Multiplication (*):", a * b)  
print("Division (/):", a / b)        
print("Remainder (%):", a % b)       
print("Floor Division (//):", a // b)
print("Power (**):", a ** b)        


# 2. ASSIGNMENT OPERATORS (Store/Update)

x = 10
x += 5   # Same as: x = x + 5
print("\nx after += 5:", x)          

x -= 3   # Same as: x = x - 3
print("x after -= 3:", x)           


# 3. COMPARISON OPERATORS (True or False)

print("\nIs a equal to b? (==):", a == b)      
print("Is a not equal to b? (!=):", a != b)  
print("Is a greater than b? (>):", a > b)    
print("Is a less than b? (<):", a < b)       


# 4. LOGICAL OPERATORS (Combine conditions)

# 'and' = both must be True
print("\nBoth are True (and):", (a > 5) and (b < 5)) 

# 'or' = at least one is True
print("At least one is True (or):", (a < 5) or (b < 5)) 

# 'not' = flips the result
print("Flipping True to False (not):", not (a > 5))     


# 5. MEMBERSHIP OPERATORS (Inside or not)

fruits = ["apple", "banana", "mango"]

print("\nIs 'apple' in list? (in):", "apple" in fruits)         # True
print("Is 'grapes' missing? (not in):", "grapes" not in fruits) # True


# 6. IDENTITY OPERATORS (Same memory address)

list1 = [1, 2]
list2 = [1, 2]
list3 = list1

print("\nDo list1 and list3 share memory? (is):", list1 is list3)      # True
print("Do list1 and list2 share memory? (is):", list1 is list2)      # False
print("Are list1 and list2 different? (is not):", list1 is not list2) # True
