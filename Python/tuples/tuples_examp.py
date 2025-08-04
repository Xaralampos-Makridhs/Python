# 1. Creating a tuple
fruit_tuple = ("apple", "banana", "cherry", "apple", "grape")
print(f"Created tuple: {fruit_tuple}")

# 2. Accessing elements of the tuple using indexing
print(f"First element: {fruit_tuple[0]}")
print(f"Last element: {fruit_tuple[-1]}")

# 3. Counting the occurrences of a specific element (count)
apple_count = fruit_tuple.count("apple")
print(f"The word 'apple' appears {apple_count} times in the tuple.")

# 4. Finding the index of a specific element (index)
banana_index = fruit_tuple.index("banana")
print(f"The word 'banana' is at index {banana_index}.")

# 5. Concatenating two tuples
vegetable_tuple = ("carrot", "potato")
combined_tuple = fruit_tuple + vegetable_tuple
print(f"Combined tuple: {combined_tuple}")

# 6. Repeating the tuple (repetition)
repeated_tuple = fruit_tuple * 2
print(f"Repeated tuple: {repeated_tuple}")

# 7. Checking if an element is in the tuple (membership)
is_grape_in_tuple = "grape" in fruit_tuple
print(f"Is 'grape' in the tuple? {is_grape_in_tuple}")

# 8. Finding the length of the tuple (length)
tuple_length = len(fruit_tuple)
print(f"The length of the tuple is: {tuple_length}")

# 9. Tuple inside other data structures (nested tuples)
nested_tuple = (fruit_tuple, vegetable_tuple)
print(f"Nested tuple: {nested_tuple}")
