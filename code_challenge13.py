# User input
name = input("Hi, what is your name? --> ")
total_sum = 0
odd_numbers = []
print("\n++++++++++++++++++++++++++++++++++++")
print("\nODD NUMBER SELECTOR, press 0 to stop the loop.")

while True:
    try:
        random = int(input("\nInput a random number --> "))

        if random % 2 == 1:
            print("Odd number detected")
            total_sum += random
            odd_numbers.append(random)
        elif random == 0:
            print("Loop Terminated.")
            break
        else:
            print("Even number detected")
    except ValueError:
        print("Invalid input, please try again.")
        continue

print(f"Hi {name}, the summation of all the odd numbers is {total_sum}")
print(f"The Odd numbers are: {' '.join(map(str, odd_numbers))}")