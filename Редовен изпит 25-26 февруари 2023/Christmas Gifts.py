adult_counter = 0
kids_counter = 0
money_for_toys = 0
money_for_sweaters = 0

while True:
    command = input()
    if command == "Christmas":
        break
    age = int(command)
    if age <= 16:
        kids_counter += 1
        money_for_toys += 5
    else:
        adult_counter += 1
        money_for_sweaters += 15


print(f"Number of adults: {adult_counter}")
print(f"Number of kids: {kids_counter}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")
