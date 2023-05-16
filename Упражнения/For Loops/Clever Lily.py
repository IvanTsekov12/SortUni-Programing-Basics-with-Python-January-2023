current_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
total_saved = 0

money_from_bdays = 0
toys = 0
money_from_toys = 0
money_for_bday = 10

for age in range(1, current_age + 1):
    if age % 2 != 0:
        toys += 1
    else:
        money_from_bdays += money_for_bday - 1
        money_for_bday += 10
money_from_toys = toy_price * toys
total_saved = money_from_toys + money_from_bdays

if total_saved >= washing_machine_price:
    print(f"Yes! {(total_saved - washing_machine_price):.2f}")
else:
    print(f"No! {(washing_machine_price - total_saved):.2f}" )