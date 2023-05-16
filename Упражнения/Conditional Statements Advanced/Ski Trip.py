days = int(input())
type_of_place = input()
rating = input()
total = 0
nights = days - 1

if type_of_place == "room for one person":
    total = nights * 18
elif type_of_place == "apartment":
    total = nights * 25
    if days < 10:
        total = total - (total * 0.3)
    elif 10 <= days <= 15:
        total = total - (total * 0.35)
    else:
        total = total - (total * 0.5)
elif type_of_place == "president apartment":
    total = nights * 35
    if days < 10:
        total = total - (total * 0.1)
    elif 10 <= days <= 15:
        total = total - (total * 0.15)
    else:
        total = total - (total * 0.2)

if rating == "positive":
    total = total + (total * 0.25)
elif rating == "negative":
    total = total - (total * 0.1)

print(f"{total:.2f}")