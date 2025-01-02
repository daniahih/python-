student_ids = (101, 102, 103, 104, 105)

# Accessing elements
print("First Student ID:", student_ids[0])
print("All Student IDs:", student_ids)

# Checking for membership
if 101 in student_ids:
    print("Student ID 101 exists.")

# Iterating through the tuple
for student_id in student_ids:
    print(f"Student ID: {student_id}")

# Note: Tuples are immutable, so you cannot modify them directly.
