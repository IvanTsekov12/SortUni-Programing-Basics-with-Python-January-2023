budget = float(input())
ticket_type = input()
people = int(input())
total = 0
transport = 0

vip_price = 499.99
normal_price = 249.99

if ticket_type == "VIP":
    total = vip_price * people
    if 1 <= people <= 4:
        transport = budget * 0.75
        total += transport
    elif 5 <= people <= 5:
        transport = budget * 0.6
        total += transport
    elif 10 <= people <= 24:
        transport = budget * 0.5
        total += transport
    elif 25 <= people <= 49:
        transport = budget * 0.4
        total += transport
    elif people >= 50:
        transport = budget * 0.25
        total += transport
elif ticket_type == "Normal":
    total = normal_price * people
    if 1 <= people <= 4:
        transport = budget * 0.75
        total += transport
    elif 5 <= people <= 5:
        transport = budget * 0.6
        total += transport
    elif 10 <= people <= 24:
        transport = budget * 0.5
        total += transport
    elif 25 <= people <= 49:
        transport = budget * 0.4
        total += transport
    elif people >= 50:
        transport = budget * 0.25
        total += transport

if budget >= total:
    print(f"Yes! You have {budget - total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva.")