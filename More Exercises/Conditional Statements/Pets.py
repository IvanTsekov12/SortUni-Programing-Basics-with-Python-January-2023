from math import floor, ceil

days = int(input())
food = int(input())
dog_food_for_day = float(input())
cat_food_for_day = float(input())
turtle_food_for_day = float(input())

food_for_dog = days * dog_food_for_day
food_for_cat = days * cat_food_for_day
food_for_turtle = (days * turtle_food_for_day) / 1000

total_food_needed = food_for_cat + food_for_turtle + food_for_dog

if total_food_needed <= food:
    food_left = food - total_food_needed
    print(f"{floor(food_left)} kilos of food left.")
else:
    needed_food = total_food_needed - food
    print(f"{ceil(needed_food)} more kilos of food are needed.")