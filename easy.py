result = ""

count = 1

while count <= 15:
    value = input("Enter value " + str(count) + ": ")
    result += value
    count += 1

print("\nConcatenated Result:")
print(result)