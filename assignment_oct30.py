print("***********************The Magic Forest Adventure***********************")
print("One day, a boy named Rahul goes to a magic forest. At the entrance, he sees a guard who asks him for his age.")
age = int(input("Enter your age: "))
if age < 10:
    print("The guard says: You are too young to enter the magic forest.")
elif age >= 10 and age <= 18:
    print("The guard says: You can enter the magic forest, but you must be careful.")
else:
    print("The guard says: Welcome! You are free to explore the magic forest.") 

print("Inside the forest, Rahul finds a mysterious box. The box asks him to choose a number ")
num=int(input("Enter a number between 1 and 3: "))
if num == 1:
    print("he gets a golden key. Do you want to open the treasure chest? (yes/no)")
    choice = input("Enter your choice: ")
    if choice=="yes":
        print("Rahul opens the treasure chest and finds a pile of gold coins!")
    elif choice=="no":
        print("Rahul decides not to open the treasure chest and continues his adventure.")
    else:
        print("The box says: Invalid choice. You get nothing.")
elif num == 2:
    print("he gets a magic sword.")
elif num == 3: 
    print("he gets a treasure map.")
else:
    print("The box says: Invalid choice. You get nothing.")

print("After finding the treasure, Rahul encounters a dangerous dragon guarding the forest exit.")
print("The dragon asks Rahul to answer a simple question: How many legs does a spider have?")
answer = int(input("Enter your answer: "))
if answer == 8:
    print("The dragon says: Correct! You may pass and exit the forest safely.")
else:
    print("The dragon says: try again! you have one more chance to answer the question.")
