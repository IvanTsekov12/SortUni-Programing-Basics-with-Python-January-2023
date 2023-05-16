needed_sum = int(input())
method = 0 # нечетни - в брой; четно - с карта
total = 0
cash = 0
card = 0
cash_count = 0
card_count = 0

while True:
    method += 1
    money = input()
    if money != "End":
        money = int(money)
        if method % 2 != 0 and money >= 100:
            print("Error in transaction!")
        elif method % 2 == 0 and money <= 10:
            print("Error in transaction!")
        elif method % 2 != 0 and money <= 100:
            print("Product sold!")
            cash += money
            total += money
            cash_count += 1
        elif method % 2 == 0 and money >= 100:
            print("Product sold!")
            card += money
            total += money
            card_count += 1
    if total >= needed_sum:
        print(f"Average CS: {cash / cash_count:.2f}")
        print(f"Average CC: {card / card_count:.2f}")
        break
    elif total < needed_sum and money == "End":
        print("Failed to collect required money for charity.")
        break


