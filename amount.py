amount = int(input("Enter amount to deposit ---> "))

print("Here is the breakdown of your deposit:")

# 1000
thousands = amount // 1000
print(thousands, "\t\t1000")
amount = amount - thousands * 1000

# 500
fhundreds = amount // 500
print(fhundreds, "\t\t500")
amount = amount - fhundreds * 500

# 200
thundreds = amount // 200
print(thundreds, "\t\t200")
amount = amount - thundreds * 200

# 100
hundred = amount // 100
print(hundred, "\t\t100")
amount = amount - hundred * 100

# 50
fifties = amount // 50
print(fifties, "\t\t50")
amount = amount - fifties * 50

# 20
twenties = amount // 20
print(twenties, "\t\t20")
amount = amount - twenties * 20

# 10
tens = amount // 10
print(tens, "\t\t10")
amount = amount - tens * 10

# 1
ones = amount // 1
print(ones, "\t\t1")