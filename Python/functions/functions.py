# Define a function that greets the user by name
def greet(name):
    print(f"Hey {name} ")  # Print a greeting message with the user's name

greet('George')  # Call the greet function with 'George' as the argument

# Define a function that adds two numbers and returns the result
def add(a, b):
    return a + b  # Return the sum of a and b

print(add(5, 4))  # Call the add function with 5 and 4 as arguments and print the result

# Define a function that greets the user and tells their age
def greet2(name, age):
    print(f"Hello {name}, you are {age} years old")  # Print a greeting with the user's name and age

greet2(age=25, name="Giannhs")  # Call greet2 function with named arguments (age=25, name="Giannhs")

# Define a recursive function to calculate the factorial of a number
def factorial(n):
    if n == 1:  # Base case: if n is 1, return 1
        return 1
    else:  # Recursive case: return n multiplied by the factorial of (n-1)
        return n * factorial(n - 1)

print(factorial(5))  # Call the factorial function with 5 and print the result (5! = 120)

# Here we will later explore *args and **kwargs for variable arguments