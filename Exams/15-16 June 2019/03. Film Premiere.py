movie = input()
pack = input()
tickets = int(input())

total = 0

if movie == "John Wick":
    if pack == "Drink":
        total = tickets * 12
    elif pack == "Popcorn":
        total = tickets * 15
    else:
        total = tickets * 19
elif movie == "Star Wars":
    if pack == "Drink":
        total = tickets * 18
    elif pack == "Popcorn":
        total = tickets * 25
    else:
        total = tickets * 30
    if tickets >= 4:
        total = total * 0.7
else:
    if pack == "Drink":
        total = tickets * 9
    elif pack == "Popcorn":
        total = tickets * 11
    else:
        total = tickets * 14
    if tickets == 2:
        total = total * 0.85

print(f"Your bill is {total:.2f} leva.")
