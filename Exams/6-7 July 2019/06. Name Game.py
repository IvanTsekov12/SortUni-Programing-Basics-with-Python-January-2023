total_points = 0
winner_name = ""
second_player = ""

while True:
  player_name = input()
  if player_name != "Stop":
    second_player = player_name
  if player_name == "Stop":
    break
  temp_points = 0
  for i in range(len(player_name)):
    points = int(input())
    if points == ord(player_name[i]):
      temp_points += 10
    else:
      temp_points += 2
  if temp_points > total_points:
    total_points = temp_points
    winner_name = player_name


if temp_points == total_points:
  print(f"The winner is {second_player} with {total_points} points!")
else:
  print(f"The winner is {winner_name} with {total_points} points!")