# Activity 24: Compiler Program
from activity23_1 import *
print("WELCOME TO MY COMLIER PROGRAM")
name = input("Hi Visitor! What is your name --> ")

print(f"Hi {name}, select from the option below")
print("A - Greet Name\nb - Greet with Name, Age, Location\nC - Triangle\nE - Exit")

isCont = True

while isCont == True:
    choice = input("Select from A - E -->").lower()
    if choice == 'a':
        name = input("Please state your name --> ")
        GreetWithName(name)
        continue
    elif choice == 'b':
        number = eval(input("Input any numeber -->"))
        print(f"Factorial of {number} is {Factorial(number)}")
        continue
    elif choice == 'c':
        GetTriangle()
        continue
    elif choice == 'e':
        print("program terminated ...")
        break
    else:
        print("Invalid Input! Please try again.")
        continue