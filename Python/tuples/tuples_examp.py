# Create a list of students as tuples (name, age, grade)
students = [
    ("John", 20, 9.2),
    ("Alice", 22, 7.5),
    ("Bob", 21, 8.8),
    ("Carol", 23, 6.9)
]

# Add a new student to the list
new_student_name = "David"
new_student_age = 24
new_student_grade = 9.5
students.append((new_student_name, new_student_age, new_student_grade))
print(f"Added new student: {new_student_name}, Age: {new_student_age}, Grade: {new_student_grade}")

# Search for a student by name "Bob"
search_name = "Bob"
student_found = None
for student in students:
    if student[0] == search_name:
        student_found = student
        break

# If the student is found, print their details
if student_found:
    print(f"Found student {search_name}: Age: {student_found[1]}, Grade: {student_found[2]}")
else:
    print(f"Student {search_name} not found.")

# Display all students in the list
print("All students:")
for student in students:
    print(f"{student[0]}, Age: {student[1]}, Grade: {student[2]}")

# Remove a student by name "Alice"
remove_name = "Alice"
students = [student for student in students if student[0] != remove_name]
print(f"Removed student {remove_name}.")

# Calculate the average grade of all students
total_grades = sum(student[2] for student in students)
average_grade = total_grades / len(students)
print(f"Average grade of all students: {average_grade:.2f}")

# Create a list of students with grade > 8.0
high_grade_students = [student for student in students if student[2] > 8.0]
print("Students with grade > 8.0:")
for student in high_grade_students:
    print(f"{student[0]}, Age: {student[1]}, Grade: {student[2]}")
