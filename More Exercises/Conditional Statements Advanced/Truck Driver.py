season = input()
monthly_kilometers = float(input())
total = 0

if monthly_kilometers <= 5000:
    if season == "Spring" or season == "Autumn":
        total = monthly_kilometers * 0.75 * 4
    elif season == "Summer":
        total = monthly_kilometers * 0.9 * 4
    elif season == "Winter":
        total = monthly_kilometers * 1.05 * 4
elif 5000 < monthly_kilometers <= 10000:
    if season == "Spring" or season == "Autumn":
        total = monthly_kilometers * 0.95 * 4
    elif season == "Summer":
        total = monthly_kilometers * 1.1 * 4
    elif season == "Winter":
        total = monthly_kilometers * 1.25 * 4
elif 10000 < monthly_kilometers <= 20000:
    total = monthly_kilometers * 1.45 * 4

total = total - (total * 0.1)
print(f"{total:.2f}")