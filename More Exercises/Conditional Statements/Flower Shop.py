from math import floor, ceil

magnolii = int(input())
zyumbyuli = int(input())
roses = int(input())
cactuses = int(input())
gift_price = float(input())

magnolia_price = 3.25
zyumbyul_price = 4
rose_price = 3.5
cactus_price = 8

total_magnolii = magnolii * magnolia_price
total_zyumbyuli = zyumbyuli * zyumbyul_price
total_roses = roses * rose_price
total_cactuses = cactuses * cactus_price

total_sum = total_cactuses +\
            total_roses +\
            total_zyumbyuli +\
            total_magnolii

win = total_sum - (total_sum * 0.05)

if win >= gift_price:
    left = win - gift_price
    print(f"She is left with {floor(left)} leva.")
else:
    nedeed = gift_price - win
    print(f"She will have to borrow {ceil(nedeed)} leva.")