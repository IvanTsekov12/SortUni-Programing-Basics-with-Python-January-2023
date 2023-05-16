income = float(input())

total = 0

while True:
    coctail_name = input()

    if coctail_name == "Party!" and total < income:
        print(f"We need {income - total:.2f} leva more.")
        break

    coctail_count = int(input())

    temp_total = 0

    temp_total += len(coctail_name) * coctail_count

    if temp_total % 2 == 1:
        temp_total -= temp_total * 0.25
    total += temp_total

    if total >= income:
        print(f"Target acquired.")
        break

print(f"Club income - {total:.2f} leva.")