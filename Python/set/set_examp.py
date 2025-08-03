# Creating a set with 5 users
myset = {'Jhon', 'George', 'Nick', 'Bill', 'Harry'}

# Printing the initial set
print(myset)

# Adding a new user (Bradley) to the set
myset.add('Bradley')
print(myset)  # The set after adding Bradley

# Removing the user 'George' from the set
myset.remove('George')
print(myset)  # The set after removing George

# Creating a second set with other users
myset2 = {'Jhon', 'George', 'Georgia', 'Sara', 'Helen'}

# Union of the two sets - the result is all unique elements from both sets
union_result = myset.union(myset2)
print(union_result)  # Printing the union of myset and myset2

# Difference between the two sets - the result is elements that are in myset but not in myset2
difference_result = myset.difference(myset2)
print(difference_result)  # Printing the difference between myset and myset2

# Intersection of the two sets - the result is the common elements between the two sets
intersection_result = myset.intersection(myset2)
print(intersection_result)  # Printing the intersection between myset and myset2

# Checking if myset is a subset of myset2
subset_result = myset.issubset(myset2)
# This checks if myset contains only elements that are also in myset2
print("Is myset subset of myset2? ", subset_result)
