budget = int(input())
season = input()
fishermen = int(input())
rent = 0

if season == "Spring":
    rent = 3000
    if fishermen <= 6:
        rent = rent - (rent * 0.1)
    elif fishermen >= 7 and fishermen <= 11:
        rent = rent - (rent * 0.15)
    elif fishermen >= 12:
        rent = rent - (rent * 0.25)
elif season == "Summer":
    rent = 4200
    if fishermen <= 6:
        rent = rent - (rent * 0.1)
    elif fishermen >= 7 and fishermen <= 11:
        rent = rent - (rent * 0.15)
    elif fishermen >= 12:
        rent = rent - (rent * 0.25)
elif season == "Autumn":
    rent = 4200
    if fishermen <= 6:
        rent = rent - (rent * 0.1)
    elif fishermen >= 7 and fishermen <= 11:
        rent = rent - (rent * 0.15)
    elif fishermen >= 12:
        rent = rent - (rent * 0.25)
elif season == "Winter":
    rent = 2600
    if fishermen <= 6:
        rent = rent - (rent * 0.1)
    elif fishermen >= 7 and fishermen <= 11:
        rent = rent - (rent * 0.15)
    elif fishermen >= 12:
        rent = rent - (rent * 0.25)

if season != "Autumn" and fishermen % 2 == 0:
    rent = rent - (rent * 0.05)

if budget >= rent:
    print(f"Yes! You have {budget - rent:.2f} leva left.")
else:
    print(f"Not enough money! You need {rent - budget:.2f} leva.")