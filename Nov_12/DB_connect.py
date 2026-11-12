#python to mysql connection
#pip-package installer python 
import mysql.connector
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "nov11_db"
)
print("Connection established successfully")

#*************************************************************
cursor = connection.cursor()  #pipeline to execute sql queries
#*************************************************************

def insert_data():
    emp_id = int(input("Enter employee id: "))
    emp_name = input("Enter employee name: ")
    emp_address = input("Enter employee address: ")
    age = int(input("Enter employee age: "))

    query="insert into employee_details(emp_id, emp_name, emp_address, age) values(%s,%s,%s,%s)"
    values=(emp_id, emp_name, emp_address, age)

    cursor.execute(query, values)
    connection.commit()  #commit the changes to the database
    print("data saved successfully")
#insert_data()




def fetch_data():
    query = "select * from employee_details"
    cursor.execute(query)
    result = cursor.fetchall()  #fetch all the records from the table
    for row in result:
        print(row)

fetch_data()