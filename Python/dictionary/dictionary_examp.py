# Initial dictionary with contact information
contactbook = {
    "John": "123-456-7890",
    "Alice": "234-567-8901",
    "Bob": "345-678-9012",
    "Carol": "456-789-0123",
    "David": "567-890-1234"
}

# Print the initial contact book
print(contactbook)

# Taking input for a new contact's name and phone number
namecontact = input("Enter the name for the contact: ")
numbercontact = input("Enter the number for the new contact: ")

# Adding the new contact to the dictionary
contactbook[namecontact] = numbercontact
# Print the contact book after adding the new contact
print(contactbook)

# Deleting the contact for 'John'
del contactbook['John']
# Print the contact book after deleting 'John'
print(contactbook)

# Updating Bob's phone number
contactbook.update({'Bob': '777-777-7777'})
# Print the contact book after updating Bob's phone number
print(contactbook)
