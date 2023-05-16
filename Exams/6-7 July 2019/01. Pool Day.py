import math

people = int(input())
fee = float(input())
shezlong_price = float(input())
umbrella_price = float(input())

total_fee = people * fee

shezlongi_count = people * 0.75
total_shezlongi = math.ceil(shezlongi_count) * shezlong_price

umbrellas_count = people * 0.5
total_umbrellas = math.ceil(umbrellas_count) * umbrella_price

total = total_umbrellas + total_shezlongi + total_fee

print(f"{total:.2f} lv.")
