budget = float(input())
season = input()
place = ""
location = ""
total = 0

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        total = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        total = budget * 0.45
elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        total = budget * 0.8
    elif season == "Winter":
        location = "Morocco"
        total = budget * 0.6
elif budget > 3000:
    place = "Hotel"
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"
    total = budget * 0.9

print(f"{location} - {place} - {total:.2f}")