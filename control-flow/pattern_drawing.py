# pattern_drawing.py
# Ask the user to enter a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))
# Ensure the user enters a positive integer
while size <= 0:
    size = int(input("Please enter a positive integer: "))
# Use a while loop to iterate through each row
row = 0
while row < size:
    # Use a for loop to print asterisks side by side
    for _ in range(size):
        print("*", end="") # print asterisk without moving to a new line
    print() # Move to the next row
    row += 1 # Increment the row count
