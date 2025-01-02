grades = {
    "Dania": 90,
    "Ali": 85,
    "Sara": 95,
    "Reem": 88,
    "Noor": 92
}

# Adding a new student's grade
grades["Omar"] = 80

# Accessing a grade
print("Dania's Grade:", grades["Dania"])

# Updating a grade
grades["Ali"] = 89
print("Ali's Updated Grade:", grades["Ali"])

# Iterating through the dictionary
for student, grade in grades.items():
    print(f"{student}: {grade}")

# Checking if a student exists
if "Sara" in grades:
    print("Sara's Grade:", grades["Sara"])

# Removing a student
del grades["Omar"]
print("Updated Grades:", grades)