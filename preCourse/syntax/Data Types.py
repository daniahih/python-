# Defining variables
name = "Dania" 
age = 25
height = 5.6
is_student = True
status = None

# Displaying information
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} ft")
print(f"Student: {is_student}")
print(f"Status: {status}")

# Updating variables
status = "Active"
print(f"Updated Status: {status}")
 
 
#  you can use also the type method 
# Defining variables
name = "Dania"
age = 25
height = 5.6
is_student = True
status = None

# Displaying information and data types
print(f"Name: {name}, Type: {type(name)}")  # Output: <class 'str'>
print(f"Age: {age}, Type: {type(age)}")    # Output: <class 'int'>
print(f"Height: {height} ft, Type: {type(height)}")  # Output: <class 'float'>
print(f"Student: {is_student}, Type: {type(is_student)}")  # Output: <class 'bool'>
print(f"Status: {status}, Type: {type(status)}")  # Output: <class 'NoneType'>

# Updating variables
status = "Active"
print(f"Updated Status: {status}, Type: {type(status)}")  # Output: <class 'str'>
