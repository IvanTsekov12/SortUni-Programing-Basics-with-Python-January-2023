team_name = input()
matches = int(input())

total_points = 0
wins_counter = 0
draw_counter = 0
loose_counter = 0

for _ in range(matches):
    match_result = input()
    if match_result == "W":
        wins_counter += 1
        total_points += 3
    elif match_result == "D":
        total_points += 1
        draw_counter += 1
    else:
        loose_counter += 1

if matches == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    print(f"{team_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins_counter}")
    print(f"## D: {draw_counter}")
    print(f"## L: {loose_counter}")
    print(f"Win rate: {(wins_counter / matches)*100:.2f}%")