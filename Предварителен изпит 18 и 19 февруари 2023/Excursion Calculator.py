people = int(input())
season = input()

price_per_person = 0

if people <= 5:
    if season == "spring":
        price_per_person = 50
    elif season == "summer":
        price_per_person = 48.5
    elif season == "autumn":
        price_per_person = 60
    else:
        price_per_person = 86
else:
    if season == "spring":
        price_per_person = 48
    elif season == "summer":
        price_per_person = 45
    elif season == "autumn":
        price_per_person = 49.5
    else:
        price_per_person = 85

total = people * price_per_person

if season == "summer":
    total = total - (total * 0.15)
elif season == "winter":
    total = total + (total * 0.08)

print(f"{total:.2f} leva.")