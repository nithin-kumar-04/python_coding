import os
def delete_file():
    try:
            os.remove("data.txt") #delete the file
            print("File deleted successfully.")
    except FileNotFoundError:
            print("File not found.")
delete_file()