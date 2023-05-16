cake_length = int(input())
cake_width = int(input())
pieces = cake_width * cake_length
total_taken = 0

while True:
    command = input()
    if command != "STOP":
        command = int(command)
        total_taken += command
    if command == "STOP" and pieces >= total_taken:
        print(f"{pieces - total_taken} pieces are left.")
        break
    if command != "STOP" and pieces < total_taken:
        print(f"No more cake left! You need {abs(total_taken - pieces)} pieces more.")
        break
