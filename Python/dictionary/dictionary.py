#create dictionary
my_dictionary = {
    'name': 'John',  # 'key': 'value'
    'age': 30,
    'city': 'Thessaloniki'
}

print(my_dictionary['name'])  # Prints: John

#update values
my_dictionary['age'] = 25  # Updates the value of 'age' to 25
print(my_dictionary['age'])  # Prints: 25

#add new item
my_dictionary['email'] = 'example@gmail.com'  # Adds the new pair 'email': 'example@gmail.com'
print(my_dictionary)  # Prints: {'name': 'John', 'age': 25, 'city': 'Thessaloniki', 'email': 'example@gmail.com'}

#delete
del my_dictionary['email']  # Deletes the 'email' key from the dictionary
print(my_dictionary)  # Prints: {'name': 'John', 'age': 25, 'city': 'Thessaloniki'}

#delete and returning the value with pop()
age = my_dictionary.pop('age')  # Deletes 'age' and returns its value
print(age)  # Prints: 25
print(my_dictionary)  # Prints: {'name': 'John', 'city': 'Thessaloniki'}

#clear
my_dictionary.clear()  # Clears all elements in the dictionary
print(my_dictionary)  # Prints: {}

#check if there is a key
if 'name' in my_dictionary:  # Checks if the key 'name' exists in the dictionary
    print("The key 'name' is in dictionary")

#keys()
print(my_dictionary.keys())  # Prints the keys of the dictionary (it will return dict_keys([]) because it's empty)

#values()
print(my_dictionary.values())  # Prints the values of the dictionary (it will return dict_values([]) because it's empty)

#items()
print(my_dictionary.items())  # Prints the key-value pairs of the dictionary (it will return dict_items([]) because it's empty)

#get()
print(my_dictionary.get('name'))  # Prints: None (the value for 'name' no longer exists)
print(my_dictionary.get('email'))  # Prints: None (the value for 'email' no longer exists)

#update()
my_dictionary.update({'age': 30, 'email': 'example@gmail.com'})  # Updates or adds the 'age' and 'email' pairs
print(my_dictionary)  # Prints: {'age': 30, 'email': 'example@gmail.com'}
