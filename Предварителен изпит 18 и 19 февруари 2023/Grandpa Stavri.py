days = int(input())

total_rakiya = 0
degrees_for_liter = 0

for i in range(days):
    amount_rakiya = float(input())
    alcohol_degrees = float(input())
    total_rakiya += amount_rakiya
    degrees_for_liter += amount_rakiya * alcohol_degrees

average_degrees = degrees_for_liter / total_rakiya

print(f"Liter: {total_rakiya:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
elif average_degrees > 38:
    print("Dilution with distilled water!")
