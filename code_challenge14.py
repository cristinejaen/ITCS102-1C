fruit_list = []

print("Welcome to the Fruit Entry Program!")
print("You can type the name of your favorite fruits one by one.")
print("When you're done, type 'exit' to finish.\n")

while True:
    fruit = input("Enter the name of a fruit (or type 'exit' to finish): ").strip()
    
    if fruit.lower() == "exit":
        print("\nYou have exited the fruit entry program.")
        break

    if fruit:
        fruit_list.append(fruit)
        print(f"'{fruit}' has been added to your fruit list.")
    else:
        print("You didn't enter a fruit name. Please try again.")

if fruit_list:
    print("\nYour fruit list includes:")
    for f in fruit_list:
        print(f"- {f}")
else:
    print("\nYou did not add any fruits to your list.")

print("\nThank you for using the Fruit Entry Program! Stay healthy and eat your fruits!")