moves = int(input())

zero_to_nine = 0
ten_to_ninetee = 0
twenty_to_twentynine = 0
thirty_to_thirtynine = 0
fourty_to_fifty = 0
invalid_moves = 0
total = 0

for i in range(moves):
    number = int(input())
    if 0 <= number <= 9:
        zero_to_nine += 1
        total += number * 0.2
    elif 10 <= number <= 19:
        ten_to_ninetee += 1
        total += number * 0.3
    elif 20 <= number <= 29:
        twenty_to_twentynine += 1
        total += number * 0.4
    elif 30 <= number <= 39:
        thirty_to_thirtynine += 1
        total += 50
    elif 40 <= number <= 50:
        fourty_to_fifty += 1
        total += 100
    elif number < 0 or number > 50:
        invalid_moves += 1
        total /= 2

zero_to_nine_total = (zero_to_nine / moves) * 100
ten_to_ninetee_total = (ten_to_ninetee / moves) * 100
twenty_to_twentynine_total = (twenty_to_twentynine / moves) * 100
thirty_to_thirtynine_total = (thirty_to_thirtynine / moves) * 100
fourty_to_fifty_total = (fourty_to_fifty / moves) * 100
invalid_moves_total = (invalid_moves / moves) * 100

print(f"{total:.2f}")
print(f"From 0 to 9: {zero_to_nine_total:.2f}%")
print(f"From 10 to 19: {ten_to_ninetee_total:.2f}%")
print(f"From 20 to 29: {twenty_to_twentynine_total:.2f}%")
print(f"From 30 to 39: {thirty_to_thirtynine_total:.2f}%")
print(f"From 40 to 50: {fourty_to_fifty_total:.2f}%")
print(f"Invalid numbers: {invalid_moves_total:.2f}%")