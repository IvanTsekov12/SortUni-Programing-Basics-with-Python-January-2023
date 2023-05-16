vacation_price = float(input())
current_money = float(input())
spend_counter = 0
total_days = 0

while True:
    command = input()
    money = float(input())
    if command == "spend":
        current_money -= money
        spend_counter += 1
        total_days += 1
    if current_money < 0:
        current_money = 0
    if spend_counter >= 5:
        print(f"You can't save the money.")
        print(total_days)
        break
    if command == "save":
        current_money += money
        total_days += 1
        spend_counter = 0
    if current_money >= vacation_price:
        print(f"You saved the money for {total_days} days.")
        break
