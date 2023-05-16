ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
austronauts_average_height = float(input())

ship_volume = ship_height * ship_length * ship_width
room_volume = (austronauts_average_height + 0.4) * 2 * 2

total_space = ship_volume // room_volume

if 3 <= total_space <= 10:
    print(f"The spacecraft holds {int(total_space)} astronauts.")
elif total_space < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")