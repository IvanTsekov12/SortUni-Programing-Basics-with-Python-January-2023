needed_sum = int(input())
method = 0 # нечетни - в брой; четно - с карта
total = 0
cash = 0
card = 0
cash_count = 0
card_count = 0
command = ""

while command != "End" and total < needed_sum:
    command = input()
    if command != "End":
        money = int(command)
    else:
        continue
    method += 1
    isCash = method % 2 == 1 and money <= 100
    isCard = method % 2 == 0 and money >= 10

    if isCard or isCash:
        print("Product sold!")
        total += money
        if isCash:
            cash += money
            cash_count += 1
        elif isCard:
            card += money
            card_count += 1
    else:
        print("Error in transaction!")




if total >= needed_sum:
    print(f"Average CS: {cash / cash_count:.2f}")
    print(f"Average CC: {card / card_count:.2f}")
else:
    print("Failed to collect required money for charity.")