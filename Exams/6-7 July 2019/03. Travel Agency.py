city = input()
packet_type = input()
vip_discount = input()
days = int(input())

total = 0

is_validPackage = packet_type == "noEquipment" or packet_type == "withEquipment" \
                  or packet_type == "noBreakfast" or packet_type == "withBreakfast"
is_validCity = city == "Bansko" or city == "Borovets" \
               or city == "Varna" or city == "Burgas"
if days > 7:
    days -= 1

if city == "Bansko" or city == "Borovets":
    if packet_type == "noEquipment":
        total = days * 80
        if vip_discount == "yes":
            total -= total * 0.05
    elif packet_type == "withEquipment":
        total = days * 100
        if vip_discount == "yes":
            total -= total * 0.1
elif city == "Varna" or city == "Burgas":
    if packet_type == "noBreakfast":
        total = days * 100
        if vip_discount == "yes":
            total -= total * 0.07
    elif packet_type == "withBreakfast":
        total = days * 130
        if vip_discount == "yes":
            total -= total * 0.12

if days <= 0:
    print("Days must be positive number!")
elif not is_validCity or not is_validPackage:
    print("Invalid input!")
elif city == "Bansko" or city == "Borovets":
    if packet_type == "noBreakfast" or packet_type == "withBreakfast":
        print("Invalid input!")
    else:
        print(f"The price is {total:.2f}lv! Have a nice time!")
elif city == "Varna" or city == "Burgas":
    if packet_type == "withEquipment" or packet_type == "noEquipment":
        print("Invalid input!")
    else:
        print(f"The price is {total:.2f}lv! Have a nice time!")
