import random


total = 0


for i in range(10):
    num = random.randint(1, 100) 
    print(f"Generated number {i+1}: {num}")
    
   
    if num % 2 == 0:
        total += num


print(f"\nSum of even numbers: {total}")
