print("\t\t *",end=" ")
for j in range(1, 10, 1):
    for z in range(10, j, -1):
        print(" ", end= " ")
    for x in range(1, j, 1):
        print("*", end= " ")
    for g in range(1, j, 1):
        print("*", end= " ")
    print()
    

for j in range(1, 10, 1):
    for z in range(1, j, 1):
        print(" ", end= " ")
    for x in range(10, j, -1):
        print("*", end= " ")
    for g in range(10, j, -1):
        print("*", end= " ")
    print()
print("\t\t *",end=" ")