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