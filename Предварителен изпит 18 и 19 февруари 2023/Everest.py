days = 1

total_climbed = 5364

while True:
    nighting = input()
    if nighting == "END" and total_climbed < 8848:
        print("Failed!")
        print(total_climbed)
        break
    elif nighting == "END" and total_climbed >= 8848:
        print(f"Goal reached for {days} days!")
        break
    if nighting == "Yes":
        days += 1

    if days > 5 and total_climbed < 8848:
        print("Failed!")
        print(total_climbed)
        break
    elif days > 5 and total_climbed >= 8848:
        print(f"Goal reached for {days} days!")
        break

    climbed = int(input())
    total_climbed += climbed

    if total_climbed >= 8848 and days <= 5:
        print(f"Goal reached for {days} days!")
        break
