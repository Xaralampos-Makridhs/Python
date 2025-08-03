# Create an empty list to store the products
mylist = []

# Ask the user to input 5 products
for i in range(5):
    product = input(f"Enter the {i+1} product: ")  # Prompt the user to input the product name
    mylist.append(product)  # Add the product to the list

# Display the current list of products
print("Current list of products:", mylist)

# Ask the user for the product name they want to delete
del_product = input("Enter the name of the product you want to delete: ")

# Check if the product exists in the list
if del_product in mylist:
    mylist.remove(del_product)  # Remove the product from the list if it exists
    print(f"{del_product} has been successfully removed.")  # Confirmation message that the product was removed
else:
    print("The product you entered is not in the list.")  # Message if the product is not found in the list

# Ask the user for the product name they want to add
add_product = input("Enter the name of the product you want to insert: ")

# Insert the new product at the 4th position (index 3)
mylist.insert(3, add_product)  # Insert at the 4th position (index 3)

# Sort the list alphabetically
mylist.sort()

# Display the sorted list
print("Sorted list of products:", mylist)

# Display the number of products in the list
print(f"There are {len(mylist)} products in the list.")
