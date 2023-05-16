from math import floor

tournaments = int(input())
starting_point = int(input())
total_points = starting_point
wins = 0
average_points = 0
won_games = 0

for _ in range(tournaments):
    position = input()
    if position == "W":
        total_points += 2000
        wins += 1
    elif position == "F":
        total_points += 1200
    elif position == "SF":
        total_points += 720
average_points = (total_points - starting_point) / tournaments
won_games = wins / tournaments * 100
print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{won_games:.2f}%")
