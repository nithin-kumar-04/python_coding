numbers=[1,2,3,4,5,6,7,8,9,10]

odd_numbers=[]
even_numbers=[]

for i in numbers:
    if i%2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(f"odd numbers are: {odd_numbers}")
print(f"even numbers are: {even_numbers}")