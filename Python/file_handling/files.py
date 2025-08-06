# file handling

# open()
file = open('example.txt', 'r')  # Reading mode: opens the file for reading
file = open('example.txt', 'w')  # Writing mode: opens the file for writing, creates a new file if it doesn't exist
file = open('example.txt', 'a')  # Appending mode: opens the file for appending, creates a new file if it doesn't exist
file = open('example.txt', 'rb')  # Binary read mode: opens the file for reading in binary mode

# close()
file.close()  # Closes the file to free up resources

# read()
content = file.read()  # Reads the entire content of the file and returns it as a string
print(content)

# readline()
line = file.readline()  # Reads one line from the file and returns it
print(line)

# readlines()
lines = file.readlines()  # Reads the file and returns a list, where each element is a line from the file
print(lines)

# write()
file.write('Hello World, again')  # Writes a string to the file (overwrites if in write mode)

# writelines()
lines = ['Line1\n', 'Line2\n', 'Line3\n']  # List of lines to be written
file.writelines(lines)  # Writes a list of strings (lines) to the file

# with statement
with open('example.txt', 'r') as file:  # Automatically handles file opening and closing
    content = file.read()  # Reads the content of the file
    print(content)

# .name
print(file.name)  # Prints the name of the file, e.g., 'example.txt'

# .closed
print(file.closed)  # Prints True if the file is closed, False otherwise

# .mode
print(file.mode)  # Prints the mode in which the file was opened (e.g., 'r', 'w', 'a', 'rb')

# tell()
print(file.tell())  # Prints the current position of the file pointer in bytes

# seek()
file.seek(0)  # Moves the file pointer to the specified position (0 in this case, which is the beginning of the file)
print(file.tell())  # Prints the new position of the pointer
