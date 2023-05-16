flower_type = input()
flower_count = int(input())
budget = int(input())
total = 0

if flower_type == "Roses":
    total = flower_count * 5
    if flower_count > 80:
        total = total - (total * 0.1)
elif flower_type == "Dahlias":
    total = flower_count * 3.8
    if flower_count > 90:
        total = total - (total * 0.15)
elif flower_type == "Tulips":
    total = flower_count * 2.8
    if flower_count > 80:
        total = total - (total * 0.15)
elif flower_type == "Narcissus":
    total = flower_count * 3
    if flower_count < 120:
        total = total + (total * 0.15)
elif flower_type == "Gladiolus":
    total = flower_count * 2.5
    if flower_count < 80:
        total = total + (total * 0.2)

if budget >= total:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - total:.2f} leva left.")
else:
    print(f"Not enough money, you need {total - budget:.2f} leva more.")
