# 1. LIST: Storing a list of students
students = ["Dania", "Ali", "Sara", "Omar", "Reem"]

# Adding a new student to the list
students.append("Noor")  # Add at the end
print("Student List:", students)

# Removing a student
students.remove("Omar")  # Remove a specific student
print("Updated Student List:", students)

# Iterating over the list
for student in students:
    print(f"Hello, {student}!")

# Sorting the list
students.sort()
print("Sorted Student List:", students)

# Accessing individual elements
print("First student:", students[0])
print("Last student:", students[-1])
