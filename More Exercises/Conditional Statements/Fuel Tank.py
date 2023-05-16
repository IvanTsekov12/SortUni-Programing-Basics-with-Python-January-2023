fuel_type = input()
fuel_litters = float(input())

if fuel_litters >= 25:
    if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
        print("Invalid fuel!")
    else:
        print(f"You have enough {fuel_type.lower()}.")
elif fuel_litters < 25:
    if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
        print("Invalid fuel!")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
