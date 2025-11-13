# Activity 23.1: Functions with Parameters and Return Values

def GreetWithName(name):
    print(f"Hi {name}, Hope your having a splendid day ")

def GreetPerson(name, loc, age):
    print(f"Hi {name}, from {loc}, {age} yr\'s old")

def FunctionWithReturn(number):
    print(f"This function calculates the summation from 1 to {number}")
    sum = 0
    for x in range(1, number + 1):
        sum += x
    return sum

def Factorial(number):
    print(f"This function calculates the factorial from 1 to {number}")
    fact = 1
    for x in range(number, 0, -1):
        fact *= x
    return fact

def GetTriangle():
    for i in range(1,11,1):
        for x in range(1,11,1):
            print(x,end="")
        print()