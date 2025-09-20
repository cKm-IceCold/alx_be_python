# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern:"))

# Initialize row counter
row = 0

# Loop through each row
while row < size:
    # Loop through each column in the current row
    for col in range(size):
        print("*", end="")  # Print * without newline
    print()  # Move to the next row
    row += 1  # Increment row counter

