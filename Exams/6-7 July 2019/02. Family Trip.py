import math

budget = float(input())
nights = int(input())
night_price = float(input())
expenses_percent = int(input()) / 100

if nights > 7:
    night_price = night_price - (night_price * 0.05)

total_nights = night_price * nights

expenses = budget * expenses_percent

total = expenses + total_nights

if budget >= total:
    print(f"Ivanovi will be left with {budget - total:.2f} leva after vacation.")
else:
    print(f"{math.fabs(total - budget):.2f} leva needed.")