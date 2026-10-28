#python Data types
#text type->string(5/10)
#strings are characters surrounded by quotes, either single or double or triple.

#number type->int,float(1/10)
#type is keyword to identify what data type you are using.

address="visakhapatnam"
print(type(address))

x=10
print(type(x))

y=10.5
print(type(y))

#sequance type->list,tuple(10/10)

#lists are used to store multiple items in a single variable. lists are created using square brackets [].
#lists are ordered, changeable(mutatable)["we can modify them after list has been created"] and allow duplicate values.
students=["beasent","sai","sai","sai","sai",20,30,40,50,60]
students[1]="krishna"
students[-3]="Nithin"
print(students[-5])  # indexing starts from right to left using negative indexing.
print(students[4])  #indexing starts from left to right using positive indexing.
print(students)
print(type(students)) 

#tuple
#tuples are used to store multiple items in a single variable. tuples are created using parentheses ().
#tuples are ordered, unchangeable(immutable)["we cannot modify them after tuple has been created"] and allow duplicate values.
fruits=("apple","banana","cherry","apple","banana")
#fruits[1]="kiwi"  #this will give an error because tuples are immutable.
print(fruits)
print(fruits[1])
print(fruits[-2])
print(type(fruits))

#set type->set(6/10)

#set also used to store multiple items in a single variable. sets are created using curly brackets {}.
#sets are unordered, changeable(mutable)["we can modify them after set has been created"] and do not allow duplicate values.
colors={"red","green","blue","yellow","red"}
#colors[2]="orange"  #this will give an error because sets are unordered and do not support indexing.
colors.add("orange")  #adding an item to the set.
colors.remove("green")  #removing an item from the set.
print(colors)
print(type(colors))

#mapping type->dict(100/10)

#dictionaries are used to store data values in key:value pairs. dictionaries are created using curly brackets {}.
#dictionaries are unordered, changeable(mutable)["we can modify them after dictionary has been created"] and do not allow duplicate keys.
#we cannot access using indexing because dictionaries are unordered. we can access using keys.
person={"name":"Nithin","age":20,"city":"visakhapatnam"}
person["age"]=21  #modifying the value of the key "age".
person["country"]="India"  #adding a new key:value pair to the dictionary.
print(person)
print(type(person))

#boolean type->bool(2/10)
#none type->none(2/10)