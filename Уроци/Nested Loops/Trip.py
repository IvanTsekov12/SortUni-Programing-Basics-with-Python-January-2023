total = 0

while True:
    destination = input()
    if destination == "End":
        break
    needed_money = float(input())
    while True:
        saved_money = float(input())
        total += saved_money
        if total >= needed_money:
            print(f"Going to {destination}!")
            total = 0
            break
