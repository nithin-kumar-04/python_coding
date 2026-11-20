from dotenv import load_dotenv
import os
print(load_dotenv())

password=os.getenv("password")
print(password)
api_key=os.getenv("api_key")
print(api_key)