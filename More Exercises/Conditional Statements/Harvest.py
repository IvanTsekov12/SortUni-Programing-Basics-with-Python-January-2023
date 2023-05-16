from math import floor, ceil

x = int(input())
y = float(input())
z = int(input())
workers = int(input())

total_grapes = x * y
wine = (total_grapes * 0.4) / 2.5

if wine >= z:
    wine_left = wine - z
    split_left = wine_left / workers
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(split_left)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(z - wine)} liters wine needed.")