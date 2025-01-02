# A variable is a name that points to a memory location where a value is stored.
# Variables in Python are dynamically typed, meaning you don't need to declare their type explicitly.

x = 5         # Integer
y = 3.14      # Float
name = "Dania" # String
is_active = True  # Boolean

# Rules for Naming Variables
# Must start with a letter or an underscore (_): e.g., name, _value.
# Cannot start with a number: e.g., 2name is invalid.
# Can only contain letters, numbers, and underscores (_).
# Case-sensitive: name and Name are two different variables.
# Cannot use reserved keywords like if, while, class.


#  Assigning Multiple Variables
a, b, c = 1, 2, 3  # Assigns 1 to a, 2 to b, and 3 to c
x = y = z = 0      # Assigns 0 to x, y, and z

# Swapping Variables
a, b = 5, 10
a, b = b, a  # Swaps the values of a and b
print(a, b)  # Output: 10, 5