veg_kilo_price = float(input())
fruit_kilo_price = float(input())
total_veg_kilos = int(input())
total_fruit_kilos = int(input())
total_veg_price = veg_kilo_price * total_veg_kilos
total_fruit_price = fruit_kilo_price * total_fruit_kilos
total = total_veg_price + total_fruit_price
price_in_euros = total / 1.94
print(f"{price_in_euros:.2f}")
