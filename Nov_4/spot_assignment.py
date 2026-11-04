import os
try:
    file = open("data.txt", "x") #open the file in read mode
    file.write(input("Enter data to write to the file: ")) #write to the file   
    content = os.path.getsize("data.txt") #read the content of the file
    print(content) #print the content of the
    file.close() #close the file
except FileNotFoundError:
    print("File not found.")
except FileExistsError:
    print("File already exists.")  
except PermissionError:
    print("File cannot be read.")