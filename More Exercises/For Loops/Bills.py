months = int(input())
total = 0
water_total = 0
internet_total = 0
other_bills = 0
other_bills_total = 0
electricity_total = 0

for i in range(1, months + 1):
    electricity = float(input())
    water_total += 20
    internet_total += 15
    electricity_total += electricity
    other_bills = (electricity + 20 + 15) + ((electricity * 0.2) + (20 * 0.2) + (15 * 0.2))
    other_bills_total += other_bills
    total += electricity + 20 + 15 + other_bills

average = total / months

print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {internet_total:.2f} lv")
print(f"Other: {other_bills_total:.2f} lv")
print(f"Average: {average:.2f} lv")