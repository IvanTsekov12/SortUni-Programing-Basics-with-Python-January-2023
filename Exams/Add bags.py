price_over_20 = float(input())
bags_kilos = float(input())
days_to_trip = int(input())
bags = int(input())

price_for_extra = 0
total = 0

if bags_kilos < 10:
    price_for_extra = price_over_20 * 0.2
elif 10 <= bags_kilos <= 20:
    price_for_extra = price_over_20 / 2
else:
    price_for_extra = price_over_20

if days_to_trip > 30:
    total = price_for_extra + (price_for_extra * 0.1)
elif 7 <= days_to_trip <= 30:
    total = price_for_extra + (price_for_extra * 0.15)
else:
    total = price_for_extra + (price_for_extra * 0.4)

print(f"The total price of bags is: {total * bags:.2f} lv.")