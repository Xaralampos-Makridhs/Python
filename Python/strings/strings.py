#create a string
string1 = 'Hello'
string2 = "World"

#multi-line string
string3 = '''This is
a multi-line
string.'''

#slicing
print(string1[0]) #prints 'H'
print(string2[-1]) #prints 'o' (negative index)

print(string1[1:4])  # 'ell' 
print(string1[:3])   # 'Hel' 
print(string1[3:])   # 'lo'

#length
print(len(string1)) #5

#compare strings
s1="apple"
s2="banana"

print(s1<s2) #True because (A)pple comes before (B)anana

#STRING METHODS

#upper lower
print(string1.upper()) #HELLO
print(string2.lower()) #hello

#strip
string="  Hello  "
print(string.strip()) #Hello (removes spaces)

#replace
print(string1.replace('e','a')) #Hallo

#split
s="apple,banana,orange"
print(s.split(',')) #['apple', 'banana']

#join
words=['apple','banana','orange']
print(", ".join(words)) # 'apple, banana'

#find() index()
s="Hello"
print(s.find('e')) #1
print(s.index('o')) #4

#count()
s = "Hello, hello"
print(s.count('hello'))  # 2

#new line
s = "Hello\nWorld"  #newline
print(s)  # 'Hello' next line 'World'

#strings and print
name = "John"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")

#string 
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # 'Hello World'

print("Hi! " * 3)  # 'Hi! Hi! Hi! '

#regular expressions

import re #library for regular expressions

s="The quick brown fox"
result=re.search(r'quick',s) #search for the substring quick, if result is true prints found
if result:
    print("Found")


