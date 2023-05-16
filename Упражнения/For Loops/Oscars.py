actor_name = input()
academy_points = float(input())
jury = int(input())
total_points = academy_points

for points in range(jury):
    jury_name = input()
    jury_points = float(input())
    total_points += ((len(jury_name) * jury_points) / 2)
    if total_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - total_points):.1f} more!")
