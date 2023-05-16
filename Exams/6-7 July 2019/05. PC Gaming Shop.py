games_sold = int(input())

hearthstone_counter = 0
fortnite_counter = 0
overwatch_counter = 0
others_counter = 0

for _ in range(games_sold):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_counter += 1
    elif game_name == "Fornite":
        fortnite_counter += 1
    elif game_name == "Overwatch":
        overwatch_counter += 1
    else:
        others_counter += 1

hearthstone_average = (hearthstone_counter / games_sold) * 100
fortnite_average = (fortnite_counter / games_sold) * 100
overwatch_average = (overwatch_counter / games_sold) * 100
others_average = (others_counter / games_sold) * 100

print(f"Hearthstone - {hearthstone_average:.2f}%")
print(f"Fornite - {fortnite_average:.2f}%")
print(f"Overwatch - {overwatch_average:.2f}%")
print(f"Others - {others_average:.2f}%")