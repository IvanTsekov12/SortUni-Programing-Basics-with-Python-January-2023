inheritance = float(input())
year_to_live_in = int(input())
age = 18
total = 0

for i in range(1799, year_to_live_in):
    i += 1
    if i > 1800:
        age += 1
    if i % 2 == 0:
        inheritance -= 12000
    else:
        inheritance -= 12000 + (50 * age)

if inheritance >= 0:
    print(f"Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.")
else:
    print(f"He will need {abs(inheritance):.2f} dollars to survive.")
