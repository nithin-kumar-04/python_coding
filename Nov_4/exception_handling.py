#python Exception Handling
#it's helps us to manage errors in our program and prevent it from crashing.
#try
#except
#finally

def demo():
    try: #try to test the code for any errors
        x = int(input("Enter a number: "))  
        if x%2 == 0:
            print(f"x is an even number.") 
        else:
            print(f"x is an odd number: {x}") 
    except: #if any error occurs then this block will be executed
        print("this is an error.")
    else: #if no error occurs then this block will be executed
        print("this is executed if no error occurs.")
    finally: #this block will be executed no matter what
        print("always executed.")
demo()