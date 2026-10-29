#methods in python

#string methods
name="nithin"
print("print string in uppercase:", name.upper())  #converts all characters to uppercase.
print("print string in lowercase:", name.lower())  #converts all characters to lowercase.
print("print string with first letter capitalized:", name.capitalize())  #converts the first character to uppercase and the rest to lowercase.
print("print reversed string:", name[::-1])  #reverses the string.

#replace method
word="hello world"
output=word.replace("world", "python")  #replaces the substring "world" with "python".
print("print replaced string:", output)

#split method
sentence="I am learning python programming"
words=sentence.split()  #splits the string into a list of words based on whitespace
print("print split words:", words)

new_sentence="I,am,learning,python,programming"
new_words=new_sentence.split(",")  #splits the string into a list of words based on the comma delimiter
print("print split words with comma delimiter:", new_words)

sent="Python,is#a#powerful#programming#language"
sent_words=sent.split("#")  #splits the string into a list of words based on the hash delimiter
print("print split words with hash delimiter:", sent_words)

#list methods
my_list=["apple", "banana", "cherry","cherry"]  #creates a list with duplicate elements
print("print original list:", my_list)

my_list.append("date")  #adds an element to the end of the list
print("print list after appending 'date':", my_list)

my_list.insert(2, "grape")  #inserts an element at a specific index in the list(inserts "grape" at index 2)
print("print list after inserting 'grape' at index 2:", my_list)

my_list.remove("cherry")  #removes the first occurrence of a specific element from the list
print("print list after removing 'cherry':", my_list)

my_list.pop(2)  #removes the element at index 2 from the list
print("print list after removing element at index 2:", my_list)

count=my_list.count("banana")  #counts the number of occurrences of a specific element in the list
print("print count of 'banana':", count)

my_list.clear()  #removes all elements from the list
print("print list after clearing:", my_list)

numbers=[5, 2, 9, 1, 7]

numbers.sort()  #sorts the elements of the list in ascending order
print("print sorted numbers:", numbers)

numbers.sort(reverse=True)  #sorts the elements of the list in descending order
print("print sorted numbers in descending order:", numbers)

numbers.reverse()  #reverses the order of the elements in the list
print("print reversed numbers:", numbers)

#Dictionary methods
my_dict={"name": "nithin",
          "age": 20, 
          "city": "vizag"
}  #creates a dictionary with key-value pairs
print("print name:", my_dict.get("name"))  #retrieves the value associated with the key "name" from the dictionary

print("print all keys:", my_dict.keys()) #retrieves all the keys from the dictionary

print("print all values:", my_dict.values())  #retrieves all the values from the dictionary
