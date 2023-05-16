locations_count = int(input())

total_average_dobiv = 0

for i in range(locations_count):
    needed_average_dobiv = float(input())
    days = int(input())
    for j in range(days):
        dobiv = float(input())
        total_average_dobiv += dobiv
    total_average_dobiv = total_average_dobiv / days
    if total_average_dobiv >= needed_average_dobiv:
        print(f"Good job! Average gold per day: {total_average_dobiv:.2f}.")
    else:
        print(f"You need {needed_average_dobiv - total_average_dobiv:.2f} gold.")
    total_average_dobiv = 0