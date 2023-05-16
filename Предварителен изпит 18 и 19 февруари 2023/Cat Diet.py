maznini_percantage = int(input()) / 100
protein_percantage = int(input()) / 100
vuglehidrati_percantage = int(input()) / 100
total_calories = int(input())
water_percantage = int(input()) / 100

total_maznini = (maznini_percantage * total_calories) / 9
total_protein = (protein_percantage * total_calories) / 4
total_vuglehidratri = (vuglehidrati_percantage * total_calories) / 4

food_weight = total_maznini + total_vuglehidratri + total_protein
calories_for_one_gram = total_calories / food_weight

water = 1 - water_percantage
result = water * calories_for_one_gram

print(f"{result:.4f}")
