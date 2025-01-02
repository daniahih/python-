# 1.1 if, elif, and else
# if: Executes code if a condition is True.
# elif: Adds more conditions if the first one is False.
# else: Executes when all other conditions are False.

# Age-based decision-making
age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
    
    # 1.2 Nested Conditionals
    # Checking eligibility for a discount
age = int(input("Enter your age: "))
membership = input("Are you a member? (yes/no): ").lower()

if age < 18:
    if membership == "yes":
        print("You get a 20% discount!")
    else:
        print("You get a 10% discount!")
else:
    print("No discount available.")
    
    
    