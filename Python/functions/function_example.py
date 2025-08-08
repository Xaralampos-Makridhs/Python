# List for books
books = []  # We can create a dictionary inside the list

# Function to add a new book
def add_book(books):
    title_to_add = input('Enter the title of the book: \n')  # Prompt for the title of the book
    author_to_add = input('Enter the author of the book:\n')  # Prompt for the author
    year_to_add = input('Enter the year of the book: \n')  # Prompt for the year
    borrow_to_add = input('Is this book borrowed (yes or no): \n')  # Ask if the book is borrowed

    # Convert the input for borrowed status to a boolean value
    if borrow_to_add.lower() == 'yes':
        isBorrowed = True
    else:
        isBorrowed = False

    # Add the book as a dictionary to the books list
    books.append({
        'title': title_to_add,  # Title of the book
        'author': author_to_add,  # Author of the book
        'year': year_to_add,  # Year of the book
        'isBorrowed': isBorrowed  # Whether the book is borrowed or not
    })

    print(f"The book '{title_to_add}' has been added successfully.")  # Confirmation message

# Function to delete a book from the list
def delete_book(books):
    title_to_delete = input('Enter the book title that you want to delete: \n')  # Prompt for the title to delete

    # Loop through the books list to find and delete the book
    for book in books:
        if book['title'].lower() == title_to_delete.lower():  # Compare titles, case-insensitive
            books.remove(book)  # Remove the book from the list
            print(f"The book '{title_to_delete}' has been removed successfully.")  # Confirmation message
            break  # Exit the loop once the book is removed
    
    else:  # If no book was found
        print('This book does not exist in the list.')

# Function to search for a book by title
def search_book(books):
    title_to_search = input('Enter the title you want to search for: \n')  # Prompt for the title to search
    isFound = False

    # Loop through the books list to search for the book
    for book in books:
        if book['title'].lower() == title_to_search.lower():  # Compare titles, case-insensitive
            isFound = True
            print(f"The book '{title_to_search}' is found in the list.")  # Book found
            break
    
    if not isFound:  # If no book was found
        print(f"We could not find the book '{title_to_search}'.")

# Function to display all books in the list
def display_books(books):
    if not books:  # If the list is empty
        print('The list is empty.')
        return

    print('\nBooks in the list:')
    # Loop through the books list and print each book's details
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Borrowed: {'Yes' if book['isBorrowed'] else 'No'}")

# Function to display borrowed books
def display_borrowed_books(books):
    borrowed_books = [book for book in books if book['isBorrowed']]  # Filter the borrowed books

    if not borrowed_books:  # If no borrowed books
        print('No borrowed books.')
        return

    print('\nBorrowed books:')
    # Loop through borrowed books and print each one
    for book in borrowed_books:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

# Main menu function to interact with the user
def menu():
    while True:
        print("\n--- Book Management ---")
        print("1. Add a new book")
        print("2. Delete a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display borrowed books")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        # Call the corresponding function based on user input
        if choice == '1':
            add_book(books)
        elif choice == '2':
            delete_book(books)
        elif choice == '3':
            search_book(books)
        elif choice == '4':
            display_books(books)
        elif choice == '5':
            display_borrowed_books(books)
        elif choice == '6':
            print("Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid option. Please choose a valid option (1-6).")  # Invalid option message

# Execute the menu function
menu()
