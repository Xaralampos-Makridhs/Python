print('Welcome to the Library System')

# Start an infinite loop to keep the system running until the user decides to exit
while True:
    # Display menu options
    print('1. Add Book')
    print('2. View All Books')
    print('3. Delete Book')
    print('4. Exit')

    # Get the user's choice
    choice = input('Choose an option:')

    # Option to add a new book
    if choice == '1':  # Add Book
        title = input('Enter book title:\n')  # Prompt user for book title
        author = input('Enter author:\n')  # Prompt user for author's name
        year = input('Enter year of publication:\n')  # Prompt user for year of publication

        # Open the file in append mode ('a') to add the new book details at the end
        with open('library.txt', 'a') as file:
            file.write(f"{title} , {author} , {year}\n")  # Write the book details to the file
        print('Book added successfully')  # Confirm the addition of the book

    # Option to view all books
    elif choice == '2':  # View All Books
        try:
            # Try to open the file in read mode ('r')
            with open('library.txt', 'r') as file:
                books = file.readlines()  # Read all lines (books) from the file

                # Check if the file is empty
                if not books:
                    print('No Books found\n')  # Inform the user if no books are present
                else:
                    # Loop through the list of books and print them with an index
                    for i, book in enumerate(books, 1):
                        print(f"{i}. {book.strip()}")  # Print each book's details

        except FileNotFoundError:
            print("Library file not found. No books to display.\n")  # Handle case where the file doesn't exist

    # Option to delete a book
    elif choice == '3':  # Delete Book
        title_to_delete = input('Enter title to delete:\n')  # Prompt user for the book title to delete
        try:
            # Try to open the file in read mode ('r')
            with open('library.txt', 'r') as file:
                books = file.readlines()  # Read all books from the file

            # Open the file in write mode ('w') to overwrite it
            with open('library.txt', 'w') as file:
                for book in books:
                    # If the title to delete is not found in the book, keep the book in the file
                    if title_to_delete not in book:
                        file.write(book)  # Write the book back to the file

            print(f"Book '{title_to_delete}' deleted successfully\n")  # Inform the user that the book has been deleted

        except FileNotFoundError:
            print('Library file not found.\n')  # Handle case where the file doesn't exist

    # Option to exit the program
    elif choice == '4':  # Exit
        print('Goodbye\n')  # Say goodbye
        break  # Break out of the loop to exit the program

    else:
        print('Invalid option, please try again\n')  # Inform the user that the input was invalid
