#CRUD operations in Python
#Create, Read, Update, Delete
import os

try:
    file = open("data.txt", "x") 
    file.write(input("Enter data to write to the file: "))
    file.close()
    if os.path.exists("data.txt"): 
        file = open("data.txt", "a") 
        file.write(input("Enter data to update the file: ")) 
        content = os.path.getsize("data.txt")
        print(content)
        file.close() 
    elif os.path.exists("data.txt") and os.path.getsize("data.txt") == 0:
        file = open("data.txt", "w") 
        file.write(input("Enter data to write to the file: ")) 
        content = os.path.getsize("data.txt")
        print(content)
        file.close() 
except FileNotFoundError:
    print("File not found.")    
except PermissionError:
    print("File cannot be read.")
except FileExistsError:
    print("File already exists.")