voucher_value = int(input())

money_left = 0

tickets_counter = 0
others_counter = 0

while True:
    product = input()
    if product == "End":
        break
    temp_total = 0
    if len(product) > 8:
        if voucher_value < int(ord(product[0])) + int(ord(product[1])):
            break
        else:
            voucher_value = voucher_value - (int(ord(product[0])) + int(ord(product[1])))
            tickets_counter += 1
    else:
        if voucher_value < int(ord(product[0])):
            break
        else:
            voucher_value = voucher_value - int(ord(product[0]))
            others_counter += 1

print(tickets_counter)
print(others_counter)

