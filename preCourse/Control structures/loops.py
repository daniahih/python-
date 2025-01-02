# Loops are used to repeat a block of code multiple times.
# for Loop
for i in range(1, 6):  # range(start, stop) stops at stop-1
    print(f"Number: {i}")
    
    names = ["Dania", "Ali", "Sara"]
# string
for name in names:
    print(f"Hello, {name}!")
    
    # words 
    word = "Python"
for char in word:
    print(char)
    ###########################################################################################
    # while Loop
    # A while loop runs as long as a condition is True.
    counter = 5

while counter > 0:
    print(f"Countdown: {counter}")
    counter -= 1  # Decrement the counter
    
    
    #  Input Validation
number = -1
while number <= 0:
 number = int(input("Enter a positive number: "))
print(f"Valid number entered: {number}")


# Breaking Out of Loops
# break: Stops the loop immediately.
# continue: Skips the current iteration and moves to the next.

for i in range(1, 11):
    if i == 5:
        print("Found 5, stopping the loop!")
        break
    print(i)


for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")