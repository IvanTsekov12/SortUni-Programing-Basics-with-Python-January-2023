budget = float(input())
season = input()
total = 0
destination = ""
type_of_place = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_place = "Camp"
        total = budget * 0.3
    elif season == "winter":
        type_of_place = "Hotel"
        total = budget * 0.7
elif budget > 100 and budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_place = "Camp"
        total = budget * 0.4
    elif season == "winter":
        type_of_place = "Hotel"
        total = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    type_of_place = "Hotel"
    total = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{type_of_place} - {total:.2f}")