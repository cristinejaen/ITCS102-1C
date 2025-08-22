a = 16
b = 15
c = 12
d = 18

print("USER LOGIN")

username = 'gerald'
password = 'gnoe2121'

print((username == 'gerald') and (password == 'gerald2121'))

print((a > b) and (c < d))        
print((a > b) or (c < d))           
print(not (a < b) and (c < d))       
print(not (a < b) or (c < d))       

result = ((a < b) and not (c > b) or ((b == a + d and (a != d)) or (c < a)))
print(result)