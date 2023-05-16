fuel_type = input()
fuel_litter = float(input())
club_card = input()
total = 0

gas_price = 0.93
gasoline_price = 2.22
diesel_price = 2.33

if fuel_type == "Gasoline":
    if club_card == "Yes":
        gasoline_price -= 0.18
        total = gasoline_price * fuel_litter
    elif club_card == "No":
        total = gasoline_price * fuel_litter
    if 20 <= fuel_litter <= 25:
        total = total - (total * 0.08)
    elif fuel_litter > 25:
        total = total - (total * 0.1)
elif fuel_type == "Gas":
    if club_card == "Yes":
        gas_price -= 0.08
        total = gas_price * fuel_litter
    elif club_card == "No":
        total = gas_price * fuel_litter
    if 20 <= fuel_litter <= 25:
        total = total - (total * 0.08)
    elif fuel_litter > 25:
        total = total - (total * 0.1)
elif fuel_type == "Diesel":
    if club_card == "Yes":
        diesel_price -= 0.12
        total = diesel_price * fuel_litter
    elif club_card == "No":
        total = diesel_price * fuel_litter
    if 20 <= fuel_litter <= 25:
        total = total - (total * 0.08)
    elif fuel_litter > 25:
        total = total - (total * 0.1)

print(f"{total:.2f} lv.")
