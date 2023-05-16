budget = float(input())
season = input()
class_car = ""
car_type = ""
total = 0

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        total = budget * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        total = budget * 0.65
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        total = budget * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        total = budget * 0.8
else:
    class_car = "Luxury class"
    car_type = "Jeep"
    total = budget * 0.9

print(class_car)
print(f"{car_type} - {total:.2f}")
