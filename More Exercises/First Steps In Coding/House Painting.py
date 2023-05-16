wall_length = float(input())
house_height = float(input())
triangle_wall_height = float(input())
wall_volume = wall_length * house_height
window_volume = 1.5 * 1.5
both = (2 * wall_volume) - (2 * window_volume)
backWall = wall_length * wall_length
entrance = 1.2 * 2
back_and_front = (2 * backWall) - entrance
total = both + back_and_front
green_paint = total / 3.4
rectangles = 2 * wall_volume
triangles = 2 * ((wall_length * triangle_wall_height) / 2)
total2 = (2 * wall_volume) + triangles
red_paint = total2 / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")