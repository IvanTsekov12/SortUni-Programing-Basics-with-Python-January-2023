steps = 0

while True:
    steps_made = input()
    if steps_made != "Going home":
        steps_made = int(steps_made)
        steps += steps_made
        if steps >= 10000:
            print("Goal reached! Good job!")
            print(f"{abs(steps - 10000)} steps over the goal!")
            break
    if steps_made == "Going home":
        steps_to_home = int(input())
        steps += steps_to_home
        if steps >= 10000:
            print("Goal reached! Good job!")
            print(f"{abs(steps - 10000)} steps over the goal!")
            break
        else:
            print(f"{10000 - steps} more steps to reach goal.")
            break