#palindrome string

my_string=input("Enter a string: ") #string input
my_string=my_string.lower() #string in lowercase

if(my_string==my_string[::-1]): #my_string[::-1] is reverses string
    print("True")
else:
    print("False")
    print(my_string[::-1]) #prints reverse string


