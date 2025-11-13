from activity23_1 import GreetWithName, GreetPerson, FunctionWithReturn, Factorial
# from activity23_1 import GreetWithPerson

def MyFirstFunction():
    print("Hi This is my first function!")
    print("What it does is it greets people!")
    print("Hi VISITOR!")

MyFirstFunction()
GreetWithName('Jaen')
GreetWithName('Sophia')
GreetPerson('Albert Einstein', 'Quezon Province', '45')
GreetPerson('Marie Curie', 'Warsaw', '66')

print(f"I want to get the summation of {FunctionWithReturn(8)}")
print(f"I want to get the summation of {FunctionWithReturn(10) + 25}")
print(f"I want to get the factorical of {Factorial(6) / FunctionWithReturn(10) }")