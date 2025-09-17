# This program generates a multiplication table for a given number.
print("MULTIPLICATION TABLE MAKER")
# Get user input
num = int(input("Enter a number: "))
# Validate input
print(f"\nMultiplication table for {num}:")
# Generate multiplication table
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")