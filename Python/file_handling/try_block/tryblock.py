#Try block
try:
    with open('example.txt', 'r+') as file:  # Open the file for both reading and writing
        content = file.read()  # Read the content
        print(content)  # Print the content of the file
        file.seek(0)  # Move the cursor back to the beginning of the file before writing
        file.write("Some content to write to the file.")  # Write to the file
except FileNotFoundError:
    print('File not found')
except IOError:
    print('Input/output error')
else:
    print('File opened successfully')
finally:
    print('Task done')
