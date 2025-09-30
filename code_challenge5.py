number = eval(input("Enter a number --> "))
factorial = 1 
for x in range(number, 0, -1):
    factorial *= x
print("The factorial of ",number, "is",factorial)
# Countdown Timer Simulator
print("COUNTDOWN TIMER SIMULATOR")
# Get user input for starting number
start = int(input("Enter the starting number for countdown: "))
# Validate input
print("\nCountdown started:")
for i in range(start, 0, -1):
    print(i)
# Adding a small delay for realism (optional)
print("Liftoff!")
