# OOP section

# Base class for Animals
class Animal:  # General class for Animals
    def __init__(self, name, species):  # Initializes the class (constructor)
        self.name = name  # This is a specific attribute of an animal
        self.species = species  # This is a specific attribute of an animal

    def speak(self):  # 'self' refers to the current object
        print(f"{self.name} says hello!")  # This is how we refer to the property of an object

# Creating an object
dog = Animal("Buddy", "Dog")  # Created an object 'dog' of type Animal, giving it the name 'Buddy' and species 'Dog'
dog.speak()  # Calling the speak method of the dog object

# Inheritance
class Dog(Animal):  # Created class 'Dog' that inherits properties and methods from Animal
    def __init__(self, name, breed):  # Constructor for Dog class
        super().__init__(name, "Dog")  # Calls the constructor of Animal and passes name and species as 'Dog'
        self.breed = breed  # New attribute specific to the Dog class

    def speak(self):  # Overriding the 'speak' method from Animal class
        print(f"{self.name} barks!")  # Now, the dog barks instead of saying hello

# Polymorphism
class Cat(Animal):  # Created class 'Cat' that also inherits from Animal
    def speak(self):  # Overriding the 'speak' method from Animal class
        print(f"{self.name} meows!")  # Now, the cat meows instead of saying hello

# Creating a 'Cat' object
cat = Cat("Ben", "Cat")
cat.speak()  # Calling the speak method for the cat object

# List of animals (both dog and cat objects)
animals = [dog, cat]

# Iterating over the animals list and calling the speak method for each animal
for animal in animals:
    animal.speak()  # This will call the appropriate 'speak' method depending on the type of object (Dog or Cat)
