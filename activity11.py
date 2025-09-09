temp = eval(input("Enter temperature in outside --> "))
#input 33
if temp >= 1 and temp <= 20:
    print("Temperature is Considered as Extremely Cold")
elif temp >= 21 and temp <= 30:
    print("Temperature is Considered as Moderately Cold")
else:
    print("Invalid Temperature ")