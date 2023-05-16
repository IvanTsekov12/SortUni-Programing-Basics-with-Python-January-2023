tshirt_price = float(input())
needed_sum = float(input())

shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = 2 * (shorts_price + tshirt_price)

total_without_discount = tshirt_price + shoes_price + shorts_price + socks_price
total = total_without_discount - (total_without_discount * 0.15)

if total >= needed_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_sum - total:.2f} lv. more.")