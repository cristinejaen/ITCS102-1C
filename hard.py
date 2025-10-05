name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))
date_of_birth = input("Enter passenger date of birth (YYYY-MM-DD): ")
destination = input("Enter destination: ")
distance_km = float(input("Enter distance in kilometers: "))

base_fare = 3.00
fare_per_km = 1.50
tax_rate = 0.07

if age >= 60:
    discount = 0.20
elif 6 <= age <= 20:
    discount = 0.10
else:
    discount = 0.0

total_fare = base_fare + (distance_km - 1) * fare_per_km
total_fare = total_fare * (1 - discount)
total_fare = total_fare * (1 + tax_rate)

print("\n--- Fare Details ---")
print("Passenger Name:", name)
print("Age:", age)
print("Date of Birth:", date_of_birth)
print("Destination:", destination)
print("Distance:", distance_km, "km")
print("Base Fare:", base_fare)
print("Fare per km:", fare_per_km)
print("Discount Applied:", discount * 100, "%")
print("Tax Rate:", tax_rate * 100, "%")
print("Total Fare: $", round(total_fare, 2))