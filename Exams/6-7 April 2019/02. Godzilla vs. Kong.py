budget = float(input())
models = int(input())
clothing_for_one_model = float(input())

decor = budget * 0.1
clothing = models * clothing_for_one_model

if models > 150:
    clothing *= 0.9

total = clothing + decor

if budget >= total:
    print("Action!")
    print(f"Wingard starts filming with {budget - total:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total - budget:.2f} leva more.")